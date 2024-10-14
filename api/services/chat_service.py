
from models.chat_models import ChatDTO
from utils.rag_manager import RAGManager


def chat_w_file(pdf_id, query) -> ChatDTO | None:
      
   response = RAGManager.retrieve_and_generate(pdf_id, query)
   
   return ChatDTO(response=response)