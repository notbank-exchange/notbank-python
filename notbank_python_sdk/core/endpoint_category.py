from enum import Enum
from typing import Any


class Wrapper:
    wrapped_value: str

    def __init__(self, value: Any):
        self.wrapped_value = value


class EndpointCategory( Enum):
    AP = Wrapper('ap')
    NB = Wrapper('api/nb')
    NB_PAGE = Wrapper('api/nb')

    @property
    def val(self):
        return self.value.wrapped_value
