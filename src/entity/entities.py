"""
Entities are business objects representing real world data

They are essential for transfer data in between different application layers. Entities contain basic business logic.
Application is able to load and store entities by their ID.

What business logic entities can contain?
Except that Entity is using custom data types and value objects to define structures. They can also know
basic validation.

For example:
    Entity `Invoice` contains `InvoiceItems` as tuple.
    What about if in real world we would validate its number?
    We should not work with an Invoice what have more items than 50 or less than 1.
    Item count validation should be inside entity. Otherwise, we are in risk that data may be wrong.

"""
from dataclasses import dataclass, field
from typing import Tuple, Union

from customtypes.invoice import InvoiceId, InvoiceState
from entity.base import AbstractEntity
from entity.valueobject import InvoiceItem


@dataclass
class Invoice(AbstractEntity):
    id: Union[InvoiceId, None]
    items: Tuple[InvoiceItem]

    state: InvoiceState = field(default=InvoiceState.NEW)
