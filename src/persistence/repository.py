"""
Repository layer is interface for persistence data.

No matter where data are stored (database, 3rd party API, filesystem etc..) it should be accessed by Persistence layer.
As I mentioned earlier `Repository` is playing important role here, it is interface in between
specific storage (database, filesystem, API) and rest application layers. It keeps all query patterns
for different use-cases at one place. It helps with optimisations and potential future changes in persistence layer.

Since it is an interface for specific model, `Repository` does not contain any implementations/mapping to any storage.
That is responsibility for `Mapper`.

Below is easy `InvoiceRepository` what does not have any specific logic yet, but it is giving us an interface for
`Invoice` persistence layer. When we will change to different storage, Interface will remain same including errors.
 Repository is NEVER propagating any error from `Mapper`. The reason is that different mapper backend
 like database, API etc... have different errors. Those should NEVER be propagated upper.
Basically `Repository` repository does not need to know about any specific IOError if it is reading or storing data.
There is either success or error. Application layers what are using Repository will decide what to do in those cases.


Repository also could be bit more complex than `InvoiceRepository`.
It can use more `Mappers` for more sophisticated queries.
For example:
 Imagine that for storing `Invoices` we are using 3rd party service. The reason is that accounting is done by 3rd party.
 Our query patterns are eiter get invoice by its ID or via sophisticated queries what accounting system doesn't support.
 What will be the solution?
    For getting an invoice by its ID we will query directly 3rd party API via Mapper.
    For other queries we will use ElasticSearch, also via Mapper.
    It means that query like: "get me invoices for users who are paying 14 days after due date", will have its own
    method what will work with two mappers one for ES and one for 3rd party API to be able return data.

 If all this logic will be encapsulated in Repository none of its implementation logic will be cross
 Persistence layer boundaries. So if we will decide to migrate data from our example to another provider
 or 3rd party service will start supporting our queries. Do the changes will affect just persistence
 layer, not rest of the application and its business logic.


 Keep in mind that data manipulation in storage is not a business logic. It is implementation.
 Business logic work with data returned from methods like: "get me invoices for users who are paying 14 days
 after due date"
 no matter where they are coming from.


Repository ALWAYS works with `Entities` it never accepts or return raw data like a `dict`.
Working with raw data is responsibility of upper or lower layer.

Follow always this scheme:
    `Entity` -> `Repository` -> `Entity`

"""
from typing import Iterable

from customtypes.invoice import InvoiceId
from entity.entities import Invoice
from persistence.error import MapperError, PersistenceError
from persistence.interfaces import InvoiceMapperInterface, RepositoryInterface


class InvoiceRepository(RepositoryInterface):

    _mapper: InvoiceMapperInterface

    def __init__(self, mapper: InvoiceMapperInterface):
        self._mapper = mapper

    async def get(self, id: InvoiceId) -> Invoice:
        try:
            return await self._mapper.get(invoice_id=id)
        except MapperError as error:
            raise PersistenceError(error)

    async def all(self) -> Iterable[Invoice]:
        try:
            return await self._mapper.all()
        except MapperError as error:
            raise PersistenceError(error)

    async def save(self, entity: Invoice) -> Invoice:
        try:
            return await self._mapper.save(entity=entity)
        except MapperError as error:
            raise PersistenceError(error)
