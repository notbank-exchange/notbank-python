from dataclasses import dataclass
from typing import Optional, List


@dataclass
class GetUserReportTicketsByStatusRequestItem:
    request_status: str


@dataclass
class GetUserReportTicketsByStatusRequestInternal:
    request_statuses: Optional[List[GetUserReportTicketsByStatusRequestItem]] = None


@dataclass
class GetUserReportTicketsByStatusRequest:
    request_statuses: Optional[List[str]] = None


def convert_to_get_user_report_tickets_by_status_request_internal(get_user_report_tickets_by_status_request: GetUserReportTicketsByStatusRequest) -> GetUserReportTicketsByStatusRequestInternal:
    if get_user_report_tickets_by_status_request.request_statuses is None:
        return GetUserReportTicketsByStatusRequestInternal()
    statuses = [GetUserReportTicketsByStatusRequestItem(
        item) for item in get_user_report_tickets_by_status_request.request_statuses]
    return GetUserReportTicketsByStatusRequestInternal(statuses)
