
from utils.vectorstore_manager import VectorStoreManager
from models.chat_models import ChatDTO
from models.file_models import FileMetadata

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def chat_w_file(metadata: FileMetadata) -> ChatDTO | None:

   return