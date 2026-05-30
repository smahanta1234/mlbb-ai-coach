from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

import os
KNOWLEDGE_BASE_PATH="Knowledge_base"

def load_documents():
    documents=[]
    for filename in os.listdir(KNOWLEDGE_BASE_PATH):
        filepath=os.path.join(KNOWLEDGE_BASE_PATH, filename)

        with open(filepath,"r", encoding="utf-8") as file:
            text=file.read()
            documents.append(text)

        return documents

def create_vector_store():
    documents=load_documents()

    splitter=RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks=[]

    for doc in documents:
        split_chunks=splitter.split_text(doc)

        chunks.extend(split_chunks)

    embeddings=HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_store=FAISS.from_texts(
        chunks,
        embedding=embeddings
    )

    return vector_store

vector_store=create_vector_store()

def retrieve_context(query, k=3):
    results=vector_store.similarity_search(
        query,
        k=k
    )

    context="\n\n".join(
        [doc.page_content for doc in results]
    )

    return context