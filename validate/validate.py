from typing import Optional
from pydantic import ValidationError
from models.models import ModelPayload, ScrapeRequest

class ValidateDict:
    def __init__(self, data_dict: dict):
        self.data_dict = data_dict
    
    def validate_dict(self) -> Optional[ModelPayload]:
        try:
            model_instance = ModelPayload(**self.data_dict)
            return model_instance
        except ValidationError as e:
            print("Validation error ", e)


class ValidateRequest:
    def __init__(self, scrape_request):
        self.scrape_request = scrape_request

    def validate_dict(self):
        if self.scrape_request.url and isinstance(self.scrape_request.page_no, int):
            return True
        return False

