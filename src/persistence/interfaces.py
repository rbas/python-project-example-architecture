from abc import ABCMeta, abstractmethod
from typing import Iterable, List, Type, Union

from customtypes.basic import ID
from customtypes.invoice import InvoiceId
from entity.base import AbstractEntity
from entity.entities import Invoice


class InvoiceMapperInterface(metaclass=ABCMeta):
    @abstractmethod
    async def get(self, invoice_id: InvoiceId) -> Invoice:
        pass

    @abstractmethod
    async def all(self) -> Iterable[Invoice]:
        pass

    @abstractmethod
    async def save(self, entity: Invoice) -> Invoice:
        pass


class RepositoryInterface(metaclass=ABCMeta):
    @abstractmethod
    async def get(self, id: Type[ID]) -> Type[AbstractEntity]:
        pass

    @abstractmethod
    async def all(
        self,
    ) -> Union[List[Type[AbstractEntity]], Iterable[Type[AbstractEntity]]]:
        pass

    @abstractmethod
    async def save(self, entity: Type[AbstractEntity]) -> Type[AbstractEntity]:
        pass
