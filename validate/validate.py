from typing import Optional
from pydantic import ValidationError
from models.models import ModelPayload

class ValidateDict:
    def __init__(self, data_dict: dict):
        self.data_dict = data_dict
    
    def validate_dict(self) -> Optional[ModelPayload]:
        try:
            model_instance = ModelPayload(**self.data_dict)
            return model_instance
        except ValidationError as e:
            print("Validation error ", e)

