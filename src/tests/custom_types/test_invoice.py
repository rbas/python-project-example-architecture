from customtypes.basic import PositiveFloat, PositiveInt
from customtypes.invoice import Amount, PricePerUnit


def test_amount_type():
    amount = Amount(24)
    assert isinstance(
        amount, PositiveInt
    ), "Amount type should be instance of PositiveFloat"


def test_price_per_unit_type():
    price = PricePerUnit(13)
    assert isinstance(
        price, PositiveFloat
    ), "PricePerUnit type should be instance of PositiveFloat"
