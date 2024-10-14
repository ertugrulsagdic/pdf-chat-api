from controllers import chat_controller, file_controller
from dotenv import load_dotenv
from fastapi import FastAPI

app = FastAPI(
    root_path="/v1",
    title="Document Chat API",
    summary="API for uploading and chatting with documents using Gemini",
)
    
load_dotenv()
    
app.include_router(file_controller.router)
app.include_router(chat_controller.router)