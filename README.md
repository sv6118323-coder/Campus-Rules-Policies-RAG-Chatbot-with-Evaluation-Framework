# Campus Rules & Policies RAG Chatbot with Evaluation Framework

A production-style Retrieval-Augmented Generation (RAG) chatbot that answers student queries about campus rules and policies — built with LangChain, ChromaDB, Groq (LLaMA 3.3 70B), and Gradio, with a built-in LLM-as-a-judge evaluation pipeline.
# How it works

# The system is split into three components:

# 1. ingest.py — Document Ingestion Pipeline

Loads campus rules from a .txt file, splits them into 300-character overlapping chunks using LangChain's 
RecursiveCharacterTextSplitter, converts each chunk into vector embeddings using the all-MiniLM-L6-v2 sentence transformer, and 
stores them in a persistent ChromaDB vector database.

# 2. chatbotev.py — RAG Engine + Evaluation Core

On each query, it performs semantic similarity search over ChromaDB to retrieve the top 3 most relevant rule chunks, then passes them as context to LLaMA 3.3 70B via the Groq API to generate a grounded answer. A second LLM call runs an automated evaluation using the same model as a judge, scoring the response across four metrics:

MetricDescriptionFaithfulnessIs the answer grounded in the retrieved context?RelevanceDid the retrieval fetch the right rules?ConfidenceHow clear and direct is the answer?HallucinationDid the answer include anything not in the context?

# 3. appev.py — Gradio Chat Interface

Wraps everything in a clean conversational UI. Every response is displayed alongside its evaluation scorecard rendered as a markdown table — giving you real-time observability into RAG quality.

# Tech Stack

LangChain — document loading, chunking, retrieval orchestration

ChromaDB — local persistent vector store

SentenceTransformers (all-MiniLM-L6-v2) — lightweight, free embeddings

Groq API + LLaMA 3.3 70B — fast LLM inference for both answering and evaluation

Gradio — chat UI

# Key Features


End-to-end RAG pipeline from raw .txt to deployable chatbot

LLM-as-a-judge evaluation framework (no external eval library needed)

Hallucination detection on every response

Persistent vector DB — ingest once, query forever

Conversation history support for multi-turn context