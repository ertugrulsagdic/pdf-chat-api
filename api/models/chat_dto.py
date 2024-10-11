from pydantic import BaseModel

class ChatReqDTO(BaseModel):
    id: str
    name: str
    message: str

class ChatDTO(BaseModel):
    answer: str