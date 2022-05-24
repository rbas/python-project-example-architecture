from entity.base import AbstractEntity
from entity.entities import Invoice
from entity.events import EventInterface
from persistence.helpers import _create_dummy_invoice


class DummyEvent(EventInterface):
    async def fire(self, entity: AbstractEntity) -> None:
        pass


def create_new_test_invoice() -> Invoice:
    return _create_dummy_invoice(identifier=None)
