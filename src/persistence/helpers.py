from random import randint
from typing import Iterable, Union

from customtypes.invoice import Amount, InvoiceId, PricePerUnit, Summary, Unit
from entity.entities import Invoice
from entity.valueobject import InvoiceItem


def _create_dummy_invoice(identifier: Union[InvoiceId, None]) -> Invoice:
    items = (
        InvoiceItem(
            amount=Amount(randint(1, 100)),
            unit=Unit.PCS,
            summary=Summary("Something"),
            price_per_unit=PricePerUnit(randint(4, 300)),
        ),
    )
    invoice = Invoice(id=identifier, items=items)
    return invoice


def _create_dummy_invoice_list() -> Iterable[Invoice]:
    for identifier in range(1, 21):
        yield _create_dummy_invoice(identifier=InvoiceId(identifier))


def _rand_id() -> InvoiceId:
    return InvoiceId(randint(1, 1000))
