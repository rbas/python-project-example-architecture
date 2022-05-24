import pytest
from typing import Iterable

from customtypes.invoice import InvoiceId, InvoiceState
from entity.entities import Invoice
from persistence.helpers import _create_dummy_invoice
from tests.helpers import DummyEvent, create_new_test_invoice
from tests.persistence.test_repository import _repository_factory
from usecases import (
    UseCaseError,
    create_invoice,
    get_all_invoices,
    get_invoice_by_id,
    mark_invoice_as_paid,
)


###
# Testing all error cases in use cases


@pytest.mark.asyncio
async def test_invoice_creating_error_handling():
    repository = _repository_factory(error_type=True)
    invoice = _create_dummy_invoice(identifier=InvoiceId(42))

    with pytest.raises(UseCaseError):
        await create_invoice(invoice=invoice, repository=repository, event=DummyEvent())


@pytest.mark.asyncio
async def test_get_invoice_by_id_error_handling():
    repository = _repository_factory(error_type=True)

    with pytest.raises(UseCaseError):
        await get_invoice_by_id(invoice_id=InvoiceId(42), repository=repository)


@pytest.mark.asyncio
async def test_get_all_invoices_error_handling():
    repository = _repository_factory(error_type=True)

    with pytest.raises(UseCaseError):
        await get_all_invoices(repository=repository)


@pytest.mark.asyncio
async def test_mark_invoice_as_paid_error_handling():
    repository = _repository_factory(error_type=True)

    with pytest.raises(UseCaseError):
        await mark_invoice_as_paid(
            invoice_id=InvoiceId(42), repository=repository, event=DummyEvent()
        )


###
# Testing use cases input/output


@pytest.mark.asyncio
async def test_create_invoice_input_output():
    repository = _repository_factory(error_type=False)
    event = DummyEvent()

    new_invoice = create_new_test_invoice()

    invoice = await create_invoice(
        invoice=new_invoice, repository=repository, event=event
    )

    assert isinstance(invoice, Invoice)
    assert invoice.id is not None, "Invoice should have an identifier after saving"


@pytest.mark.asyncio
async def test_get_invoice_by_id_input_output():
    repository = _repository_factory(error_type=False)

    invoice_id = InvoiceId(42)

    invoice = await get_invoice_by_id(invoice_id=invoice_id, repository=repository)

    assert isinstance(invoice, Invoice), "UseCase should return `Invoice` entity"


@pytest.mark.asyncio
async def test_get_all_invoices_input_output():
    repository = _repository_factory(error_type=False)

    invoices = await get_all_invoices(repository=repository)

    assert isinstance(invoices, Iterable), "UseCase should return Iterable[Invoice]"

    assert all(
        map(lambda x: isinstance(x, Invoice), invoices)
    ), "Not all returned data are instance of Invoice"


@pytest.mark.asyncio
async def test_mark_invoice_as_paid_input_output():
    repository = _repository_factory(error_type=False)
    event = DummyEvent()
    invoice_id = InvoiceId(42)

    invoice = await mark_invoice_as_paid(
        invoice_id=invoice_id, repository=repository, event=event
    )

    assert isinstance(invoice, Invoice)
    assert invoice.id == invoice_id
    assert (
        invoice.state == InvoiceState.PAID
    ), "Invoice state should be changed to `paid`"
