import pytest
from typing import Iterable

from customtypes.invoice import InvoiceId
from entity.entities import Invoice
from persistence.error import ItemNotFound, MapperError, PersistenceError
from persistence.helpers import _create_dummy_invoice
from persistence.interfaces import InvoiceMapperInterface
from persistence.mapper.dummy import DummyInvoiceMapper
from persistence.repository import InvoiceRepository


class ErrorInvoiceMapper(InvoiceMapperInterface):
    def get(self, invoice_id: InvoiceId) -> Invoice:
        raise ItemNotFound("Item was not found")

    def all(self) -> Iterable[Invoice]:
        raise MapperError("Error while data loading")

    def save(self, entity: Invoice) -> Invoice:
        raise MapperError("Error while data saving")


def _repository_factory(error_type: bool) -> InvoiceRepository:
    if error_type:
        mapper = ErrorInvoiceMapper()
    else:
        mapper = DummyInvoiceMapper()

    return InvoiceRepository(mapper=mapper)


@pytest.mark.asyncio
async def test_get_item_not_found_error():
    repository = _repository_factory(error_type=True)

    with pytest.raises(ItemNotFound):
        await repository.get(id=InvoiceId(42))


@pytest.mark.asyncio
async def test_get_persistence_error_while_loading_all_invoices():
    repository = _repository_factory(error_type=True)

    with pytest.raises(PersistenceError):
        await repository.all()


@pytest.mark.asyncio
async def test_get_persistence_error_while_invoice_saving():
    repository = _repository_factory(error_type=True)
    invoice = _create_dummy_invoice(identifier=InvoiceId(42))
    with pytest.raises(PersistenceError):
        await repository.save(entity=invoice)
