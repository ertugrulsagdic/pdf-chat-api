import chromadb
from constants import DATABASE_PATH
from vectorstore.gemini_embedding import GeminiEmbeddingFunction

class VectorStore:
    @classmethod
    def get_instance(cls, db_name: str):
        db_path = DATABASE_PATH
        client = chromadb.PersistentClient(db_path)
            # Check if collection exists
        existing_collections = client.list_collections()
        collection_names = [col.name for col in existing_collections]
        print(f"Existing collections: {collection_names}")
        
        if db_name not in collection_names:
            instance = client.create_collection(
                db_name,
                embedding_function=GeminiEmbeddingFunction()
            )
        else:
            instance = client.get_collection(name=db_name, embedding_function=GeminiEmbeddingFunction())
        return instance
    
    
    