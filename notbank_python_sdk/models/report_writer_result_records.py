from dataclasses import dataclass

from notbank_python_sdk.constants import ReportResultStatus



@dataclass
class ReportWriterResultRecords:
    requesting_user: int
    result_status: ReportResultStatus
    report_execution_start_time: str
    report_execution_complete_time: str
    report_output_file_pathname: str
    report_descriptive_header: str
    descriptor_id: str
    urt_ticket_id: str 
    
    