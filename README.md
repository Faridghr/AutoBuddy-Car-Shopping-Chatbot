# AutoBuddy: A Car Shopping Search Chatbot

Welcome to AutoBuddy, a car shopping search chatbot designed to simplify your car buying experience. This project leverages advanced AI techniques to provide personalized car recommendations based on user preferences.

## Table of Contents

- [Introduction](#introduction)
- [Objectives and Goals](#objectives-and-goals)
- [Project Architecture](#project-architecture)
- [Technologies Used](#technologies-used)
- [Data Collection and Preprocessing](#data-collection-and-preprocessing)
- [RAG Pipeline Implementation](#rag-pipeline-implementation)
- [Performance Metrics](#performance-metrics)
- [Deployment Plan](#deployment-plan)
- [Future Work](#future-work)

## Introduction

AutoBuddy is designed to assist users in finding the perfect car based on their preferences, budget, and specific criteria. It offers a personalized and efficient car search experience by understanding user queries and providing tailored recommendations.

## Objectives and Goals

- Develop a user-friendly chatbot for car shopping.
- Integrate advanced search capabilities tailored to user needs.
- Provide a seamless and engaging user experience.

## Project Architecture

![Project Architecture](png/architecture-diagram.png)

### Explanation

- **User Interface**: Chatbot interface for user interactions, built using Streamlit.
- **Backend**: Handles user queries, processes requests, and retrieves data using LangChain and RAG.
- **Data Sources**: Integration with car listings databases and dealer information, stored in Pinecone for fast retrieval.
- **LLM**: OpenAI API for natural language processing and generating responses.

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

The RAG pipeline combines retrieval-based and generative models to provide accurate and contextually relevant responses.

### Steps Involved

1. Query Understanding: NLP techniques to parse user queries.
2. Document Retrieval: Retrieve relevant documents or data snippets using Pinecone.
3. Response Generation: Generate responses based on retrieved data using OpenAI API.
4. Integration: Combine retrieval and generation outputs for final response using LangChain.

## Performance Metrics

- **Response Accuracy**: Measure of how accurately the chatbot provides relevant information.
- **User Satisfaction**: User feedback and ratings on the chatbot’s performance.
- **Response Time**: Average time taken to respond to user queries.

## Deployment Plan

1. **Development**: Finalize and test the chatbot application.
2. **Containerization**: Use Docker for creating a deployable image.
3. **Hosting**: Deploy on AWS for scalability and reliability.

## Future Work

- Integrate with more car listing platforms.
- Add more advanced search filters.
- Implement voice interaction capabilities.
- Expand to other markets (e.g., used cars, electric vehicles).
