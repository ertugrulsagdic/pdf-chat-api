from fastapi import APIRouter, status, UploadFile, HTTPException
import os

from models.base_dto import BaseModelDTO
from models.file_dto import FileDTO

import services.file_service as file_service


router = APIRouter(
    prefix="/pdf",
    tags=["PDF"]
)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=FileDTO)
async def create_file(file: UploadFile):

    allowed_file_types = ['pdf', 'doc', 'docx']
    file_extension = file.filename.split('.')[-1]
    if file_extension not in allowed_file_types:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'{file_extension} File type not allowed',
        )

    try:
        contents = await file.read()
        uplad_path = "./api/uploads/"
        if not os.path.exists(uplad_path):
            os.makedirs(os.path.dirname(uplad_path))

        with open(f"{uplad_path}/{file.filename}", 'wb') as f:
            f.write(contents)
        
        file_response = file_service.create_file()

        if file_response is None:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="File could not be created") 

        return file_response
    
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='There was an error uploading the file',
        )
    finally:
        await file.close()