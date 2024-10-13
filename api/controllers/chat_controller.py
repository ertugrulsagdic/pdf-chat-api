
from fastapi import APIRouter, status, HTTPException
from utils.files_metadata_manager import FilesMetadataManager

from models.chat_models import ChatReqDTO, ChatDTO

import services.chat_service as chat_service

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ChatDTO)
async def chat_w_file(body: ChatReqDTO):

    metadata = FilesMetadataManager.get_metadata(body.pdf_id)

    if metadata is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="File not found")

    chat_response = chat_service.chat_w_file(metadata)

    if chat_response is None:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Chat could not be created")

    return chat_response
