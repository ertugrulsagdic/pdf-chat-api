from datetime import datetime

from pydantic import BaseModel
from pydantic import Field

class FileDTO(BaseModel):
    name: str = Field(..., min_length=3, max_length=100)