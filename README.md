# AutoBuddy: A Car Shopping Search Chatbot

Welcome to AutoBuddy, a car shopping search chatbot designed to simplify your car buying experience. This project leverages advanced AI techniques to provide personalized car recommendations based on user preferences.

## Project Architecture

- **src/materials/**: Contains data that our model will use to answer questions.
- **src/FetchData/**: Contains Python-based script for scraping car's information.
- **src/Fine-Tune/**: Contains Python-Notebook for fine-tune the GPT-4o-mini.
- **src/Evaluation/**: Contains Python-Notebook for evaluating chatbot context relevance and answer relevance.
- **src/chatBot.py**: Python-based chatbot script.
- **src/mainStreamlitUI.py**: Python-based Streamlit main script.
- **doc/**: Stores [Report](doc) files.
- **video/**: Contains [video](video) presentation. You can also watch the video on [YouTube](https://youtu.be/uWGa-fNuLiY).
- **.env**: Contains API keys.

## Table of Contents

- [Introduction](#introduction)
- [Objectives and Goals](#objectives-and-goals)
- [Technologies Used](#technologies-used)
- [Data Collection and Preprocessing](#data-collection-and-preprocessing)
- [RAG Pipeline Implementation](#rag-pipeline-implementation)
- [Fine Tuning Steps](#fine-Tuning-Steps)
- [Dependencies](#dependencies)
- [Usage](#usage)
- [Setting Up OpenAI API](#Setting-Up-OpenAI-API)
- [Setting up Pinecone](#Setting-up-Pinecone)
- [Contact](#Contact)
- [License](#License)

## Introduction

In this project, we aim to develop a domain-specific chatbot application that utilizes a Large Language Model (LLM) for natural language understanding and processing, combined with the efficiency and scalability of a vector database for data storage and retrieval. The application will implement the Advanced Retrieval-Augmented Generation (RAG) method to enhance the chatbot's ability to provide accurate and relevant responses by integrating retrieved information with generative AI capabilities. We also fine-tune GPT-4o-mini in this project with related data to achieve optimal performance. The front-end of the application will be developed using Streamlit, a popular Python framework for creating interactive web applications.


## Objectives and Goals

- **Personalized Car Recommendations** based on user preferences (e.g., budget, car type, brand).
- **Advanced Retrieval-Augmented Generation (RAG) pipeline** for contextually relevant responses.
- **Fine-Tuned LLM (GPT-4o-mini)** for precise, domain-specific car shopping insights.
- **Performance Evaluation** using context relevance and human-assessed answer relevance.
- **Interactive Interface** built with Streamlit for a user-friendly experience.
- **Scalable Vector Database** leveraging Pinecone for fast and efficient data retrieval.


## Technologies Used

- **Natural Language Processing (NLP)**: OpenAI API
- **Machine Learning**: Retrieval-Augmented Generation (RAG)
- **APIs**: For data retrieval from car listings
- **Vector Database**: Pinecone
- **User Interface**: Streamlit
- **Deployment**: Docker, AWS

## Data Collection and Preprocessing

- **Source and Nature of Data**: Data is collected from various online car listing platforms and dealer inventories.
- **Steps for Data Collection**: Web scraping from car listing websites, API integration with car dealer databases.
- **Data Preprocessing Techniques**: Data cleaning, normalization, feature extraction.

## RAG Pipeline Implementation

The RAG pipeline combines retrieval-based and generative models to provide accurate and contextually relevant responses. To improve my RAG pipeline and the performance of our chatbot, I employed advanced RAG techniques such as Auto-Merging Retrieval, which enhances the relevance of context retrieval.

![Project Architecture](png/architecture-diagram.png)

## Fine Tuning Steps
- Prepare Training Data: We create datasets representative of the desired tasks. 
- Uploading a Training File for Fine-Tuning: Uploading our training data is a crucial step.
- Train a New Fine-Tuned Model: Create a Fine-Tuning Job and Monitor Job Progress.


## Dependencies
- Python 3.7+
- langchain
- pinecone-client
- python-dotenv
- streamlit
- pypdf

## Usage
1. Clone the repository: `git clone https://github.com/Faridghr/AutoBuddy-Car-Shopping-Chatbot.git`
2. Navigate to the project directory: `cd AutoBuddy-Car-Shopping-Chatbot`
3. Install dependencies: `pip install -r requirements.txt`
4. Set up your LLM.
5. Set up your Pinecone API key in `.env` file.
5. Navigate to src directory: `cd src`
6. Run the Streamlit application: `streamlit run mainStreamlitUI.py`
7. Open your web browser and navigate to the URL provided by Streamlit (usually http://localhost:8501).
8. Interact with the chatbot by typing messages and receiving responses from the local LLM service.

## Setting Up OpenAI API
1. Enter our OpenAI account and navigate to [OpenAI Platform](https://platform.openai.com/apps). 
2. Navigate to the API section.
3. Proceed to create a new API key by pressing '+ Create' new secret key.
4. Select a suitable name to remember and press the Create secret key button.
5. Copy the secret key and add your OpenAI API Keys in a file called `.env`.

## Setting up Pinecone
1. To create a PineCone account, sign up via this link: [Pinecone](https://www.pinecone.io/)
2. After registering with the free tier, go into the project, and click on Create a Projec.
3. Fill in the Project Name, Cloud Provider, and Environment. In this case, I have used “SimpleRAGChatbot Application” as a Project Name, GCP as Cloud Provider, and Iowa (gcp-starter) as an Environment.
4. After the project is created, go into the API Keys section, and make sure you have an API key available. Do not share this API key.
5. After completing the account setup, you can add your Pinecone API Keys in a file called `.env`.

## Contact Us
Farid Ghorbani
GitHub: https://github.com/Faridghr
Email: faridghr.cs@gmail.com
LinkedIn: https://www.linkedin.com/in/farid-ghorbanii/

## License
This project is licensed under the MIT License. See the LICENSE file for details.