from dataclasses import dataclass
from typing import List, Optional


@dataclass
class UserReportTicket:
    requesting_user: int
    oms_id: int
    report_flavor: str
    create_time: str
    initial_run_time: str
    interval_start_time: str
    interval_end_time: str
    request_status: str
    report_frequency: str
    interval_duration: int
    request_id: str
    last_instance_id: Optional[str]
    account_ids: List[int]
