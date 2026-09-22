## RAG Practice

A modular Retrieval-Augmented Generation (RAG) practice project built to understand the complete RAG pipeline — from loading documents and generating embeddings to storing vectors in FAISS and generating answers using an LLM.

The project currently runs through the command line/console.
## RAG Pipeline

The project follows this workflow:
- Documents
- Document Loader
- Text Chunks
- Embeddings
- FAISS Vector Store
- Similarity Search
- Relevant Context
- LLM
- Generated Answer

## Features
- Load documents from multiple file formats
- Support for:
  - PDF
  - TXT
  - DOCX
- Split documents into smaller chunks
- Generate vector embeddings for document chunks
- Store embeddings in a FAISS vector database
- Perform similarity-based document retrieval
- Retrieve relevant context for a user query
- Use an LLM to generate an answer based on retrieved context
- Modular RAG architecture with separate components for loading, embedding, storage, and search
- Console-based interaction
