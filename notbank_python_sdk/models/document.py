from dataclasses import dataclass


@dataclass
class Document:
    descriptor_id: str
    doc_name: str
    num_slices: int
    status_code: str
    status_message: str
