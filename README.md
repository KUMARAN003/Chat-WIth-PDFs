# Chat with Multiple PDFs
This Streamlit app allows users to engage in a conversational chat about multiple PDF documents. The application utilizes natural language processing and retrieval-based chat models to provide responses to user questions. Users can upload PDF files, ask questions, and receive answers based on the content of the uploaded documents.

# How to Use
## Upload PDFs:

Use the sidebar to upload multiple PDF documents.
Click the "Process" button to extract text from the uploaded PDFs. 

## Ask Questions:

Enter your questions in the text input box.
Click on the "Ask" button to receive responses based on the content of the PDF documents.

## Chat History:

The chat history is displayed in the main section, showing both user and bot messages.
Code Overview
The application is built using Streamlit, a Python library for creating web applications with minimal code. Here are some key components of the code:

## PDF Processing :

The get_pdf_text function extracts text from the uploaded PDF documents using the PyPDF2 library.
Text Chunking:

The get_text_chunks function splits the extracted text into chunks for processing.

## Vector Store:

The get_vectorstore function uses language embeddings (Hugging Face Instructor model) and FAISS to create a vector store for efficient retrieval.

## Conversation Chain:

The get_conversation_chain function sets up a conversational retrieval chain using a language model (Hugging Face Hub) and a memory buffer.

## User Interface:

Streamlit is used to create the user interface, allowing users to upload PDFs, ask questions, and view the chat history.
Chat Handling:

The handle_userinput function processes user questions, updates the chat history, and displays messages in the UI.

## Dependencies :

Streamlit: Used for creating the web application.
PyPDF2: Used for extracting text from PDF documents.
Hugging Face Transformers: Provides access to pre-trained language models.
LangChain: Custom library for text processing, embeddings, and vector stores.