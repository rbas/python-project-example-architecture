"""
UseCase is aggregating and orchestrating business logic.

Business logic is agnostic from all implementation layers. It means that changing database engine or using
different 3rd party service should not affect business logic.

For example UseCase below named `mark_invoice_as_paid`.
Its business logic is
    1) load `Invoice` by `InvoiceId`
    2) change `Invoice` state to "paid"
    3) save invoice
    4) trigger event that invoice was marked as "paid"

Question: What changes you will make in `mark_invoice_as_paid` if you will decide to use 3rd party API
instead of database for storing `Invoices`?

Answer: Nothing, business logic will remain same. Changes should be done on `Mapper` layer.

Essential for UseCase is work with `Entities` or `ValueObjects` never with raw data. Translating raw data to
`Entity` or `ValueObject` belongs to upper or lower layer.
That is keeping UseCase layer agnostic from outer implementation.

Follow always this scheme:
    `Entity` -> UseCase -> `Entity`
"""
from typing import Iterable

from customtypes.invoice import InvoiceId, InvoiceState
from entity.entities import Invoice
from entity.events import EventInterface
from persistence.error import PersistenceError
from persistence.repository import InvoiceRepository


class UseCaseError(Exception):
    pass


async def create_invoice(
    invoice: Invoice, repository: InvoiceRepository, event: EventInterface
) -> Invoice:
    try:
        invoice = await repository.save(entity=invoice)

        await event.fire(entity=invoice)

        return invoice
    except PersistenceError as error:
        # Handle specific errors and raise descriptive error to know what happened
        raise UseCaseError(error)


async def get_invoice_by_id(
    invoice_id: InvoiceId, repository: InvoiceRepository
) -> Invoice:
    try:
        return await repository.get(id=invoice_id)
    except PersistenceError as error:
        # Handle specific errors and raise descriptive error to know what happened
        raise UseCaseError(error)


async def get_all_invoices(repository: InvoiceRepository) -> Iterable[Invoice]:
    try:
        return await repository.all()
    except PersistenceError as error:
        # Handle specific errors and raise descriptive error to know what happened
        raise UseCaseError(error)


async def mark_invoice_as_paid(
    invoice_id: InvoiceId, repository: InvoiceRepository, event: EventInterface
) -> Invoice:
    try:
        invoice = await repository.get(id=invoice_id)
        invoice.state = InvoiceState.PAID

        saved_invoice = await repository.save(entity=invoice)

        await event.fire(entity=saved_invoice)

        return saved_invoice
    except PersistenceError as error:
        # Handle specific errors and raise descriptive error to know what happened
        raise UseCaseError(error)
