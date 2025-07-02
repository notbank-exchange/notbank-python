from dataclasses import dataclass
from typing import Optional, Union

from notbank_python_sdk.requests_models.with_oms_id import WithOMSId


@dataclass
class GetProductsRequest(WithOMSId):
    attribute: Optional[str] = None
    attribute_value: Optional[str] = None
    get_disabled: Optional[Union[bool, int]] = None
    depth: Optional[int] = None
    start_index: Optional[int] = None
