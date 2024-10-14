from typing import Generic, TypeVar

from pydantic import BaseModel
from pydantic.generics import GenericModel

T = TypeVar('T', bound=BaseModel)


class BaseModelDTO(GenericModel, Generic[T]):
    status: str
    message: str
    data: T