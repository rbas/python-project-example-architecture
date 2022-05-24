import pytest

from customtypes.basic import PositiveFloat, PositiveInt


def test_positive_float_type():
    number = PositiveFloat(42.69)
    assert str(number) == "42.69"
    assert repr(number) == "<PositiveFloat:42.69>"
    assert number == PositiveFloat(42.69)


def test_raise_error_when_positive_float_type_is_not_positive_number():
    with pytest.raises(TypeError):
        PositiveFloat(-1)

    with pytest.raises(TypeError):
        PositiveFloat(0)


def test_positive_int_type():
    number = PositiveInt(42)
    assert str(number) == "42"
    assert repr(number) == "<PositiveInt:42>"
    assert number == PositiveInt(42)


def test_raise_error_when_positive_int_type_is_not_positive_number():
    with pytest.raises(TypeError):
        PositiveInt(-1)

    with pytest.raises(TypeError):
        PositiveInt(0)
