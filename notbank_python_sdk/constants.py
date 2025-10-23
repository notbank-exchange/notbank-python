from enum import Enum, IntEnum


class MakerTaker(str, Enum):
    UNKNOWN = "Unknown"
    MAKER = "Maker"
    TAKER = "Taker"


class TimeInForce(IntEnum):
    GTC = 1
    OPG = 2
    IOC = 3
    FOK = 4
    GTX = 5
    GTD = 6


class Side(IntEnum):
    BUY = 0
    SELL = 1
    SHORT = 2
    UNKNOWN = 3


class OrderType(IntEnum):
    MARKET = 1
    LIMIT = 2
    STOP_MARKET = 3
    STOP_LIMIT = 4
    TRAILING_STOP_MARKET = 5
    TRAILING_STOP_LIMIT = 6
    BLOCK_TRADE = 7


class PegPriceType(IntEnum):
    LAST = 1
    BID = 2
    ASK = 3


class InstrumentState(str, Enum):
    BOTH = "Both"
    INACTIVE = "Inactive"


class ReportFrequency(str, Enum):
    ON_DEMAND = "onDemand"
    HOURLY = "Hourly"
    DAILY = "Daily"
    WEEKLY = "Weekly"
    MONTHLY = "Monthly"
    ANNUALLY = "Annually"


class ReportResultStatus(str, Enum):
    NOT_STARTED = "NotStarted"
    NOT_COMPLETE = "NotComplete"
    ERROR_COMPLETE = "ErrorComplete"
    SUCCESS_COMPLETE = "SuccessComplete"
    CANCELLED = "Cancelled"


class ReportRequestStatus(str, Enum):
    SUBMITTED = "Submitted"
    VALIDATING = "Validating"
    SCHEDULED = "Scheduled"
    IN_PROGRESS = "InProgress"
    COMPLETED = "Completed"
    ABORTING = "Aborting"
    ABORTED = "Aborted"
    USER_CANCELLED = "UserCancelled"
    SYS_RETIRED = "SysRetired"
    USER_CANCELLED_PENDING = "UserCancelledPending"
