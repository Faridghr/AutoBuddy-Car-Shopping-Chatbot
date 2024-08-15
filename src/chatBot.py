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

        # Load fine-tuned model ID
        with open('./Fine-Tune/fine_tuned_model_id.txt', "r") as f:
            fine_tuned_model_id = f.read().strip()

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
        # model_name = "gpt-4o"
        model_name = fine_tuned_model_id
        self.llm = ChatOpenAI(model_name=model_name, organization='org-G8UtpAEtkeLatwCgEhQGaPOw')

        # Define refined prompt template
        template = """
            You are an advanced car shopping assistant chatbot. Your goal is to help users find the perfect car based on their preferences and requirements. You will ask for user preferences step-by-step and use the information provided to give personalized recommendations. Start by introducing yourself and then proceed with the following steps:

            1. Greet the user and introduce yourself.
            2. Ask the user for their budget range.
            3. Ask about the type of car they are interested in (e.g., sedan, SUV, truck, etc.).
            4. Inquire about the preferred brand or any specific brands they have in mind.
            5. Ask about the primary use of the car (e.g., daily commute, family trips, off-roading, etc.).
            6. Determine any must-have features (e.g., fuel efficiency, safety features, technology, etc.).
            7. Ask if they have any other specific requirements or preferences.
            8. Summarize the user's preferences and provide a few car recommendations based on their answers with the link of company website that can buy the car.
            9. Offer to provide more details about any of the recommended cars or answer any additional questions.

            Use the user's answers and the following combined context to answer the question accurately and concisely. If the user is unsure about something, offer suggestions or ask follow-up questions to help them clarify their needs.

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
        
