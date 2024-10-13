
from io import BytesIO
import io
from fastapi import UploadFile
from utils.rag_manager import RAGManager
from models.file_models import FileDTO, FileMetadata

import os
from utils.hashing_manager import HashingManager
from utils.files_metadata_manager import FilesMetadataManager
from datetime import datetime

from constants import UPLOAD_PATH

async def create_file(file: UploadFile) -> FileDTO | None:
    if not os.path.exists(UPLOAD_PATH):
        os.makedirs(os.path.dirname(UPLOAD_PATH))

    contents = await file.read()

    # generate file id according to file contents using md5 hash
    # since we limited the file size to 1MB, this should be performant
    # for larger files, we should consider using a different approach
    pdf_id = HashingManager.md5_file_hashing(contents)

    metadata = FilesMetadataManager.get_metadata(pdf_id)

    file_extension = file.filename.split('.')[-1]

    if metadata is None:
        metadata = FileMetadata(
            pdf_id=str(pdf_id),
            file_path=UPLOAD_PATH,
            file_extension=file_extension,
            actual_file_name=file.filename,
            file_size=file.size,
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
    else:
        metadata.updated_at = datetime.now()

    FilesMetadataManager.save_metadata(metadata)

    pdfname = f"{UPLOAD_PATH}{pdf_id}.{file_extension}"
    # We could have uploaded the file to a cloud storage service (AWS S3, Google Cloud Storage etc.)
    # but for simplicity, I stored the file in the local filesystem
    with open(pdfname, 'wb') as f:
        f.write(contents)

    RAGManager.indexing(pdfname, pdf_id)

    return FileDTO(pdf_id=str(pdf_id))
