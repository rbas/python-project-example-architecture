"""
Custom data types are essential for work accordingly DDD patterns (https://www.domaindrivendesign.org).

It helps to reflect real world language. Application own data types helps to read and maintain code better.
We as IT developers are used to use terms as `integer`, `string`, `float` etc... But they are not exists in
real world and even more it is not always right that we are using `integer` as data type for object id.
The reason why is not always right is that most likely we never want to have negative id for object. Same case
for Invoice amount. It could be `int`. But in real world we never want to have negative amount on invoice, or maybe we
would also validate maximum amount for invoice. That will never happen with native data type `int`.
If we use `int` as data type of invoice entity instead of our own data type `Amount`.
This business logic for validation should be delegated somewhere out of Entity, and we should believe that
data were validated in correct way. That can cause errors or inconsistency.

So basically making application own data types ir part of business logic.

Python is really nice with possibility to create own data types with all the dunder methods. It could not be easier.

"""
from enum import Enum

from customtypes.basic import ID, PositiveFloat, PositiveInt


class Amount(PositiveInt):
    pass


class Summary(str):
    pass  # TODO Validate max and min length


class PricePerUnit(PositiveFloat):
    pass


class Unit(Enum):
    PCS = "pcs"
    HRS = "hrs"


class InvoiceState(Enum):
    NEW = "new"
    PAID = "paid"


class InvoiceId(ID):
    pass
