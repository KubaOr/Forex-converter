from forex_python.converter import CurrencyRates
from forex_python.converter import CurrencyCodes
def convert(amount_from, amount_to, amount):
    """
    converts from USD to INR
    >>> convert('USD','INR',10)
    ₹ 725.06

    """
    currency = CurrencyRates()
    codes=CurrencyCodes()
    result = currency.convert(amount_from, amount_to, int(amount))
    result = str(round(result, 2))
    return codes.get_symbol(amount_to) + ' ' + result