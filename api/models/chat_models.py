from pydantic import BaseModel

class ChatReqDTO(BaseModel):
    pdf_id: str
    message: str

class ChatDTO(BaseModel):
    answer: str