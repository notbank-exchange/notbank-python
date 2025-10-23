from dataclasses import dataclass
from typing import Dict, Optional, List

from notbank_python_sdk.constants import ReportRequestStatus


@dataclass
class GetUserReportTicketsByStatusRequest:
    request_statuses: Optional[List[ReportRequestStatus]] = None


def convert_to_get_user_report_tickets_by_status_request_internal(get_user_report_tickets_by_status_request: GetUserReportTicketsByStatusRequest) -> List:
    if get_user_report_tickets_by_status_request.request_statuses is None:
        return []
    statuses = [
        {"RequestStatus": item.value}
        for item
        in get_user_report_tickets_by_status_request.request_statuses]
    return statuses
