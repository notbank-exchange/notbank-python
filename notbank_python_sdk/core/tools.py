from decimal import Decimal


def truncate_dec(value: Decimal, decimals: Decimal) -> Decimal:
    exp = Decimal(1/decimals)
    return Decimal(int(value * exp)) / Decimal(exp)


def dec_to_str_stripped(val: Decimal) -> str:
    if val == Decimal("0"):
        return "0"
    dec_str = "{0:f}".format(val)
    return dec_str.rstrip("0").rstrip(".") if "." in dec_str else dec_str
