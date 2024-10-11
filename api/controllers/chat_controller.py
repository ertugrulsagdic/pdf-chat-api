
from fastapi import APIRouter, status, HTTPException
import os

from models.chat_dto import ChatReqDTO, ChatDTO

import services.chat_service as chat_service


router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ChatDTO)
async def chat_w_file(body: ChatReqDTO):

    chat_response = chat_service.chat_w_file()

    if chat_response is None:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Chat could not be created")

    return chat_response
