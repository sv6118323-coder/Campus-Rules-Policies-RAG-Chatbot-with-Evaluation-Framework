#langchain is used for connecting llm+databse+tretieval
#this file loads your campus rules and stores them in a searchable database
from langchain_community.document_loaders import TextLoader

from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_chroma import Chroma

from langchain_community.embeddings import SentenceTransformerEmbeddings

import os

#step1 load the document
#text loader reads you .txt file and loads it into memory
print("📄 Loading campus rules document...")
loader = TextLoader("documents/campus_rules.txt")
documents = loader.load()
print(f"✅ Loaded {len(documents)} document(s)")


#step2 split into chunks like big text into small pieces 
#like this :
#1Minimum attendance required is 75%.
#2Library allows borrowing 3 books.
#3Hostel curfew is 9 PM.
#to this :
#Chunk 1 → Attendance rule
#Chunk 2 → Library rule
#Chunk 3 → Hostel rule
print('splitting document into chunks...')
splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)#chunk size is like denoting each chunk can have 300 characters long 300-500 is good range
#overlap is to add the last 50 characters  of previous chunk to next chunk so that context cannot be missed 
# basically overlap is to be 10-20% of chunk size
chunks = splitter.split_documents(documents)
print(f"✅ Created {len(chunks)} chunks") #f string like these are usefull while debug 
 
#step3 creat embeddings (converts text into numbers)
print("🔢 Creating embeddings (converting text to numbers)...")

embeddings = SentenceTransformerEmbeddings(
    model_name="all-MiniLM-L6-v2"
)#"all-Mini....." this small embedding model that accurate and free used widely for chatbots

#step4 store in chromadb 
print("💾 Saving to ChromaDB database...")
vectordb = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="./campus_db"
)
print("✅ Database created successfully!")
print("📁 Saved in: ./campus_db")
print("🎉 Ingest complete! Now run chatbot.py")
#this will create searchable dataset 
#chrom.formdocuments means create database from documents
#persistdirectory=... means save database to campus_db folder so nect time it can reload no need to rebuild
