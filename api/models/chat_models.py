from pydantic import BaseModel

class ChatReqDTO(BaseModel):
    pdf_id: str
    query: str

class ChatDTO(BaseModel):
    response: str