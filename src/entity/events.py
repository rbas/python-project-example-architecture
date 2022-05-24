"""
Events are being triggered once in app is happening something what outer world may care about

For example:
    Event `InvoiceWasPaid`. As name is suggesting that is event triggered after an Invoice was
    marked as paid. In outer world (means not in this microservice) somebody may want knows that it happen, and
    do some their actions.

    Events here are publicly facing. It should just trigger event in Pub-Sub components. Who wants to listen, can.
    Do not mix it with job/queue tasks.
"""
from abc import ABCMeta, abstractmethod

from entity.base import AbstractEntity
from entity.entities import Invoice


class EventInterface(metaclass=ABCMeta):
    @abstractmethod
    async def fire(self, entity: AbstractEntity) -> None:
        pass


class InvoiceCreated(EventInterface):
    """
    Trigger event for listeners who need to know that new Invoice was created

    There is many use cases what should happen after new Invoice is created.
    For example:
        accounting department would be notified
        analytics department needs to update their data
        etc...
    """

    async def fire(self, entity: Invoice) -> None:
        pass


class InvoiceWasPaid:
    """
    Trigger event for listeners who need to know that existing Invoice was paid

    There is many use cases what should happen after Invoice was paid.
    For example:
        accounting department would be notified
        analytics department needs to update their data
        CEO would get notification into mobile device
        etc...
    """

    async def fire(self, entity: Invoice) -> None:
        pass
