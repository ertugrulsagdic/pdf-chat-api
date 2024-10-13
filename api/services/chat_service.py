
from utils.rag_manager import RAGManager
from models.chat_models import ChatDTO, ChatReqDTO

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def chat_w_file(body: ChatReqDTO) -> ChatDTO | None:
   
   file_id, query = body.pdf_id, body.query
   
   response = RAGManager.retrieve_and_generate(file_id, query)
   
   return ChatDTO(response=response)