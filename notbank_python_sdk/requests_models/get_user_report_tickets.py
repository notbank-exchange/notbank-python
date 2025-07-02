from dataclasses import dataclass


@dataclass
class GetUserReportTicketsRequest:
    user_id: int
