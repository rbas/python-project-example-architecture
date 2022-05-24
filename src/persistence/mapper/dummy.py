"""
Mapper is an implementation for specific service.

It contains logic how to convert `Entity` to specific storage.

For example:
    For storing invoices is used 3rd party API service.
    In our application we have several query patters for invoices.
        * Get Invoice By ID
        * Get Invoice By User
        * Get Users Unpaid Invoices
        * Get Users After Due Date Invoices
        * Create New Invoice

    First, all those query/stor patterns should be in `Repository` interface for `Invoice` aggregate.
    Pls check `Repository` first if you didn't do that yet!

    `Mapper` will implement the specific logic to map `Entities` to 3rd party service.
    All the communication will be here.

    If later we will decide to store Invoices in our own database we will change just `Mapper`. Rest of application
    will remain exactly the same. It means change will be done faster and safer.

"""
from typing import Iterable

from customtypes.invoice import InvoiceId
from entity.entities import Invoice
from persistence.helpers import (
    _create_dummy_invoice,
    _create_dummy_invoice_list,
    _rand_id,
)
from persistence.interfaces import InvoiceMapperInterface


class DummyInvoiceMapper(InvoiceMapperInterface):
    """
    Creating and returning invoices on demand none of them are stored anywhere
    """

    async def get(self, invoice_id: InvoiceId) -> Invoice:
        invoice = _create_dummy_invoice(identifier=invoice_id)
        return invoice

    async def all(self) -> Iterable[Invoice]:
        return _create_dummy_invoice_list()

    async def save(self, entity: Invoice) -> Invoice:
        identifier = entity.id or _rand_id()
        invoice = Invoice(id=identifier, items=entity.items, state=entity.state)
        return invoice
