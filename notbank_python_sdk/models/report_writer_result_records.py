from dataclasses import dataclass


@dataclass
class ReportWriterResultRecords:
    requesting_user: int
    urt_ticket_id: str
    descriptor_id: str
    result_status: str
    report_execution_start_time: str
    report_execution_complete_time: str
    report_output_file_pathname: str
    report_descriptive_header: str
