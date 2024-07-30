from dotenv import load_dotenv
import os
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Pinecone
from langchain.llms import HuggingFaceHub
from pinecone import Pinecone, ServerlessSpec
from langchain import PromptTemplate
from langchain.chains import ConversationalRetrievalChain, RetrievalQA
from langchain_pinecone import PineconeVectorStore
import ollama
from openai import OpenAI
from langchain_openai import ChatOpenAI



class ChatBot():
    load_dotenv()
    # material_file_path = 'src\Materials\CarsInformation.txt'
    def __init__(self, material_file_path):
        # Load and split documents
        loader = TextLoader(material_file_path)
        documents = loader.load()
        text_splitter = CharacterTextSplitter(chunk_size=1500, chunk_overlap=300)  # Adjusted chunk size and overlap
        docs = text_splitter.split_documents(documents)

        # Initialize embeddings
        embeddings = HuggingFaceEmbeddings()

        # Initialize Pinecone instance
        pc = Pinecone(api_key=os.getenv('PINECONE_API_KEY'))

        index_name = "langchain-demo"

        if index_name not in pc.list_indexes().names():
            pc.create_index(
                name=index_name,
                dimension=768,
                metric="cosine",
                spec=ServerlessSpec(
                    cloud="aws",
                    region="us-east-1"
                )            
            )
        index = pc.Index(index_name)
        self.docsearch = PineconeVectorStore.from_documents(docs, embeddings, index_name=index_name)

        # Initialize ChatOpenAI
        model_name = "gpt-4o"
        self.llm = ChatOpenAI(model_name=model_name, organization='org-G8UtpAEtkeLatwCgEhQGaPOw')

        # Define refined prompt template
        template = """
        You are a Toronto travel assistant. Users will ask you questions about their trip to Toronto. Use the following combined context to answer the question accurately and concisely.
        If the combined context does not contain the answer, simply state that you don't know.

        Combined Context: {context}
        Question: {question}
        Answer:
        """

        self.prompt = PromptTemplate(template=template, input_variables=["context", "question"])

    # Define a function for combining contexts
    def merge_contexts(self, contexts):
        # Combine the contexts into a single string
        return "\n\n".join([ctx.page_content for ctx in contexts])

    # Create a function to retrieve and merge contexts
    def retrieve_and_merge_contexts(self, query, retriever):
        # Retrieve multiple contexts
        retrieved_docs = retriever.get_relevant_documents(query)
        # Merge contexts
        combined_context = self.merge_contexts(retrieved_docs)
        return combined_context

    # Create a RetrievalQA chain with the refined prompt and custom retrieval
    def generate_response(self, question):
        # Retrieve and merge context
        combined_context = self.retrieve_and_merge_contexts(question, self.docsearch.as_retriever())
        # Format the prompt
        formatted_prompt = self.prompt.format(context=combined_context, question=question)

        # Generate response
        response = self.llm.invoke(formatted_prompt)
        return response.content
        
