
from models.file_dto import FileDTO


def create_file() -> FileDTO | None:
    return None
    return FileDTO(name="file.pdf")