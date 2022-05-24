"""
Value Objects part of business logic

It is adding structure to data with basic business logic as what data type data should be by using custom types.
Difference in between Value Object and Entity is that Value Object does not represent any data in real world.
"""
from dataclasses import dataclass

from customtypes.invoice import Amount, PricePerUnit, Summary, Unit


@dataclass(frozen=True)
class InvoiceItem:
    amount: Amount
    unit: Unit
    summary: Summary
    price_per_unit: PricePerUnit
