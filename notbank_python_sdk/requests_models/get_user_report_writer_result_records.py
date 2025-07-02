from dataclasses import dataclass
from typing import Optional


@dataclass
class GetUserReportWriterResultRecordsRequest:
    user_id: int
    depth: Optional[int] = None
    start_index: Optional[int] = None
