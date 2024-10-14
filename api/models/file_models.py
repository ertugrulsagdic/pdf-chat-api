from datetime import datetime

from pydantic import BaseModel, Field


class FileDTO(BaseModel):
    pdf_id: str

class FileMetadata(BaseModel):
    pdf_id: str
    file_path: str
    file_extension: str
    actual_file_name: str
    file_size: int
    created_at: datetime = Field(default_factory=datetime)
    updated_at: datetime = Field(default_factory=datetime)