
from models.file_dto import FileDTO

import os
import uuid

async def create_file(file) -> FileDTO | None:
    contents = await file.read()
    uplad_path = "./api/uploads/"
    if not os.path.exists(uplad_path):
        os.makedirs(os.path.dirname(uplad_path))

    file_id = uuid.uuid4()
    file_extension = file.filename.split('.')[-1]

    with open(f"{uplad_path}/{file_id}.{file_extension}", 'wb') as f:
        f.write(contents)

    return FileDTO(pdf_id=str(file_id))