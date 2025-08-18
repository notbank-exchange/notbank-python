from typing import Dict, List, Optional

from notbank_python_sdk.models.instrument import Instrument
from notbank_python_sdk.models.product import Product


class NotbankClientCache:
    _instrument_by_symbol: Dict[str, Instrument]
    _product_by_symbol: Dict[str, Product]

    def __init__(self):
        self._instrument_by_symbol = {}

    def get_instrument_id(self, symbol: str) -> Optional[int]:
        opt_instrument = self.get_instrument(symbol)
        if opt_instrument is None:
            return opt_instrument
        return opt_instrument.instrument_id

    def get_instrument(self, symbol: str) -> Optional[Instrument]:
        return self._instrument_by_symbol.get(symbol)

    def update_instruments(self, instruments: List[Instrument]) -> None:
        for instrument in instruments:
            self._instrument_by_symbol[instrument.symbol] = instrument

    def get_product(self, symbol: str) -> Optional[Product]:
        return self._product_by_symbol.get(symbol)

    def update_products(self, products: List[Product]) -> None:
        for product in products:
            self._product_by_symbol[product.product] = product
