import simplejson as json
import unittest
from notbank_python_sdk.models.level2_ticker_feed import level2_ticker_feed_from_list


class ConvertLevel2FromJsonTestCase(unittest.TestCase):
    def test_level_2_ticker_from_list(self):
        tickers_as_list_str = "[[1,0,1750691160212,0,104701.54,1,104350,154,0.00047,0],[2,0,1750691160212,0,104701.54,2,104300.00,154,0.00014,0],[3,0,1750691160212,0,104701.54,2,102300,154,0.00013,0],[4,0,1750691160212,0,104701.54,1,105000,154,0.00007,1]]"
        tickers_as_list = json.loads(tickers_as_list_str, use_decimal=True)
        level2_tickers = [level2_ticker_feed_from_list(
            ticker_as_list) for ticker_as_list in tickers_as_list]
