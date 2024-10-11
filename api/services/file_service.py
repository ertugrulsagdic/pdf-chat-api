
from fastapi import UploadFile
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
    file_id = HashingManager.md5_file_hashing(contents)

    metadata = FilesMetadataManager.get_metadata(file_id)

    if metadata is None:
        metadata = FileMetadata(
            pdf_id=str(file_id),
            file_name=file.filename,
            file_size=file.size,
            file_type=file.content_type,
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
    else:
        metadata.updated_at = datetime.now()

    FilesMetadataManager.save_metadata(metadata)

    file_extension = file.filename.split('.')[-1]

    # We could have uploaded the file to a cloud storage service (AWS S3, Google Cloud Storage etc.)
    # but for simplicity, I stored the file in the local filesystem
    with open(f"{UPLOAD_PATH}/{file_id}.{file_extension}", 'wb') as f:
        f.write(contents)

    return FileDTO(pdf_id=str(file_id))