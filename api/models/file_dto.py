from datetime import datetime

from pydantic import BaseModel
from pydantic import Field

class FileDTO(BaseModel):
    pdf_id: str