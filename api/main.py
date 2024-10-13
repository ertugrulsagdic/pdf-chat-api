from fastapi import FastAPI

from vectorstore.context import VectorStore
from controllers import file_controller
from controllers import chat_controller

from dotenv import load_dotenv

app = FastAPI(
    root_path="/v1",
    title="Document Chat API",
    summary="API for uploading and chatting with documents using Gemini",
)

# import os
# from constants import UPLOAD_PATH

# if os.path.exists(UPLOAD_PATH):
#     # remove all files in the uploads directory
#     for file in os.listdir(UPLOAD_PATH):
#         os.remove(f"{UPLOAD_PATH}/{file}")

#     os.rmdir(UPLOAD_PATH)
    
load_dotenv()
    
app.include_router(file_controller.router)
app.include_router(chat_controller.router)