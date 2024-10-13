from uuid import uuid4
import chromadb
from constants import DATABASE_PATH
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings


class VectorStore:
    
    @classmethod
    def get_instance(cls, db_name: str):
        client = chromadb.PersistentClient(DATABASE_PATH)
        
        return Chroma(
            client=client, 
            collection_name=db_name,
            embedding_function=GoogleGenerativeAIEmbeddings(model="models/embedding-001")
            )
        
    @classmethod
    def store_documents(cls, db_name: str, documents: list):
        vectorstore = cls.get_instance(db_name)
        vectorstore.add_documents(
            documents=documents, 
            ids=[str(uuid4()) for _ in range(len(documents))],
        )
        
    @classmethod
    def get_number_of_documents(cls, db_name: str):
        vectorstore = cls.get_instance(db_name)
        return len(vectorstore.get()['documents'])