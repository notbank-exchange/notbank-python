from dataclasses import dataclass


@dataclass
class DocumentSlice:
    descriptor_id: str
    base64_bytes: str
    status_code: str
    status_message: str
