from langchain import hub
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from utils.llm_manager import LLMManager
from vectorstore.context import VectorStore


class RAGManager:
    
    
    @staticmethod
    def indexing(filepath: str, file_id: str):
        if VectorStore.get_number_of_documents(file_id) > 0:
            return
        
        # LOAD
        loader = PyPDFLoader(filepath)
        docs = loader.load()
        
        # SPLIT
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000, chunk_overlap=100, add_start_index=True
            )
        chunks = text_splitter.split_documents(docs)
        
        # STORE
        VectorStore.store_documents(file_id,chunks)
        
    @staticmethod
    def retrieve_and_generate(file_id: str, query: str,  n_results: int = 5) -> str:
        vectorstore = VectorStore.get_instance(file_id)
        
        total_docs = VectorStore.get_number_of_documents(file_id)
        if total_docs < n_results:
            n_results = total_docs
        
        retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": n_results})

        prompt = hub.pull("rlm/rag-prompt")

        def format_docs(docs):
            return "\n\n".join(doc.page_content for doc in docs)
        
        rag_chain = (
            {"context": retriever | format_docs, "question": RunnablePassthrough()}
            | prompt
            | LLMManager.get_gemini_llm()
            | StrOutputParser()
        )
        
        return rag_chain.invoke(query)
        