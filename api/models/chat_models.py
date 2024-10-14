from pydantic import BaseModel

class ChatReqDTO(BaseModel):
    query: str

class ChatDTO(BaseModel):
    response: str