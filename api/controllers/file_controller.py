import services.file_service as file_service
from fastapi import APIRouter, HTTPException, UploadFile, status
from models.file_models import FileDTO

router = APIRouter(
    prefix="/pdf",
    tags=["PDF"]
)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=FileDTO)
async def create_file(file: UploadFile):

    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")

    # check if filr type is allowed
    allowed_file_types = ['pdf']
    file_extension = file.filename.split('.')[-1]
    if file_extension not in allowed_file_types:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'{file_extension} File type not allowed',
        )
    
    # check if file size is greater than 1MB
    if file.size > 1000000:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='File size should not exceed 1MB',
        )
    file_response = await file_service.create_file(file)

    if file_response is None:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="File could not be created") 

    return file_response
    # try:
    #     file_response = await file_service.create_file(file)

    #     if file_response is None:
    #         raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="File could not be created") 

    #     return file_response
    
    # except Exception as e:
    #     print(e)
    #     raise HTTPException(
    #         status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    #         detail='There was an error uploading the file',
    #     )
    # finally:
    #     await file.close()