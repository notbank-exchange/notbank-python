from typing import Any, List
import simplejson as json
from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Level1TickerSummaryMin:
    instrument_id: int
    instrument_symbol: str
    last_traded_px: Decimal
    rolling_24hr_volume: Decimal
    rolling_24hr_px_change: Decimal
    rolling_24hr_px_change_percent: Decimal


def level1_ticker_summary_min_list_from_json_list_str(json_list: str) -> List[Level1TickerSummaryMin]:
    list_of_summaries_lists = json.loads(json_list, use_decimal=True)
    return [level1_ticker_summary_min_from_str(item) for item in list_of_summaries_lists]


def level1_ticker_summary_min_from_str(json_list: List[Any]) -> Level1TickerSummaryMin:
    return Level1TickerSummaryMin(
        instrument_id=json_list[0],
        instrument_symbol=json_list[1],
        last_traded_px=json_list[2],
        rolling_24hr_volume=json_list[3],
        rolling_24hr_px_change=json_list[4],
        rolling_24hr_px_change_percent=json_list[5],
    )
