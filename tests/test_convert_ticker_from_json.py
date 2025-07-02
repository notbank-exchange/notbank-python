import simplejson as json
import unittest
from notbank_python_sdk.models.ticker import ticker_from_list


class ConvertTickerFromJsonTestCase(unittest.TestCase):
    def test_ticker_from_list(self):
        tickers_as_list_str = "[[1750743900000,104701.54,104701.54,104701.54,104701.54,0,0,0,154,1750743840000],[1750743960000,104701.54,104701.54,104701.54,104701.54,0,0,0,154,1750743900000],[1750744020000,104701.54,104701.54,104701.54,104701.54,0,0,0,154,1750743960000]]"
        tickers_as_list = json.loads(tickers_as_list_str, use_decimal=True)
        level2_tickers = [ticker_from_list(
            ticker_as_list) for ticker_as_list in tickers_as_list]
