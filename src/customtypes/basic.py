class PositiveFloat:
    value: float

    def __init__(self, value: float):
        if value <= 0:
            raise TypeError(
                f"Value {value} is not valid for type `{self.__class__.__name__ }`. Type should contain just "
                f"positive float values. "
            )

        self.value = float(value)

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f"<{self.__class__.__name__}:{self.value}>"

    def __eq__(self, other) -> bool:
        return self.value == other.value


class PositiveInt:
    value: int

    def __init__(self, value: int):
        if value <= 0:
            raise TypeError(
                f"Value {value} is not valid for type `{self.__class__.__name__}`. Type should contain just positive "
                f"int values. "
            )

        self.value = int(value)

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f"<{self.__class__.__name__}:{self.value}>"

    def __eq__(self, other) -> bool:
        return self.value == other.value


class ID(PositiveInt):
    """
    ID should be always positive number.
    """

    pass
