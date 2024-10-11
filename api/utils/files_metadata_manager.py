import json

from models.file_models import FileMetadata
from constants import UPLOAD_PATH, METADATA_FILE

# We could have used a database (MongoDB, Postgres etc.) to store metadata
# but for simplicity I used a json file to store metadata of uploaded files
class FilesMetadataManager:
    @staticmethod
    def save_metadata(metadata):
        file_path = f"{UPLOAD_PATH}/{METADATA_FILE}"

        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {}

        data[metadata.pdf_id] = metadata.dict()

        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4, default=str)

    @staticmethod
    def get_metadata(pdf_id):
        file_path = f"{UPLOAD_PATH}/{METADATA_FILE}"

        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            return None
        
        if pdf_id not in data:
            return None

        return FileMetadata(**data.get(pdf_id))
