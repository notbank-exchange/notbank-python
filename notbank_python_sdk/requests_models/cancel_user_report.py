from dataclasses import dataclass


@dataclass
class CancelUserReportRequest:
    user_report_id: str
