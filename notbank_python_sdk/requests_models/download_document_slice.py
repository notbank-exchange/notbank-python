from dataclasses import dataclass
from typing import Optional


@dataclass
class DownloadDocumentSliceRequest:
    descriptor_id: str
    slice_num: Optional[int] = 0
