
from utils.rag_manager import RAGManager
from models.chat_models import ChatDTO, ChatReqDTO

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def chat_w_file(pdf_id, query) -> ChatDTO | None:
      
   response = RAGManager.retrieve_and_generate(pdf_id, query)
   
   return ChatDTO(response=response)