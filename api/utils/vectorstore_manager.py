from langchain.text_splitter import RecursiveCharacterTextSplitter
from vectorstore.context import VectorStore
from langchain_community.document_loaders import PyPDFLoader

class VectorStoreManager:
    
    @staticmethod
    def save_file_chunks(filepath: str, file_id: str):
        vectorstore = VectorStore.get_instance(file_id)

        if vectorstore.count() > 0:
            return
        
        loader = PyPDFLoader(filepath)
        docs = loader.load()

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000, chunk_overlap=100, add_start_index=True
            )
        chunks = text_splitter.split_documents(docs)
        
        for i, chunk in enumerate(chunks):
            vectorstore.add(
                documents=[chunk.page_content],
                ids=[f"chunk_{i}"],
            )
                        
    @staticmethod
    def retrieve_similar_chunks(query: str, file_id: str, n_results: int = 5):
        vectorstore = VectorStore.get_instance(file_id)
        return vectorstore.similarity_search(query, n_results=n_results, metadatas={"file_id": file_id})

    @staticmethod
    def get_chunks(file_id: str, query: str):
        vectorstore = VectorStore.get_instance(file_id)
        print(vectorstore.peek(5))
        return vectorstore.query(query_texts=[query], n_results=1)