from dataclasses import dataclass


@dataclass
class DownloadDocumentRequest:
    descriptor_id: str
