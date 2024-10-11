from typing import Union

from fastapi import APIRouter, FastAPI

from controllers import file_controller
from controllers import chat_controller

app = FastAPI(root_path="/v1")

app.include_router(file_controller.router)
app.include_router(chat_controller.router)