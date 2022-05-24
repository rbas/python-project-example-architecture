import pytest
from typing import Iterable

from customtypes.invoice import Amount, InvoiceId, PricePerUnit, Summary, Unit
from entity.entities import Invoice
from entity.valueobject import InvoiceItem
from persistence.mapper.dummy import DummyInvoiceMapper


@pytest.mark.asyncio
async def test_get_invoice_from_dummy_mapper():
    mapper = DummyInvoiceMapper()
    invoice = await mapper.get(invoice_id=InvoiceId(11))

    assert isinstance(invoice, Invoice)


@pytest.mark.asyncio
async def test_get_all_invoices_from_dummy_mapper():
    mapper = DummyInvoiceMapper()
    invoices = await mapper.all()

    assert isinstance(invoices, Iterable)

    invoice_list = [item for item in iter(invoices)]
    assert 20 == len(invoice_list)

    assert isinstance(invoice_list[0], Invoice)


@pytest.mark.asyncio
async def test_save_invoice_dummy_mapper():
    invoice = Invoice(
        id=None,
        items=(
            InvoiceItem(
                amount=Amount(11),
                unit=Unit.HRS,
                summary=Summary("Blah"),
                price_per_unit=PricePerUnit(333),
            ),
        ),
    )

    mapper = DummyInvoiceMapper()
    entity = await mapper.save(entity=invoice)

    assert isinstance(entity.id, InvoiceId)
