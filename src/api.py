"""
Bootstrap for API by using Starlette (https://www.starlette.io)

Responsibilities are
    * Routing
    * Process http Request
    * Set up dependencies for use case
    * Encode Entity from use case
    * Return response
    * Handle potential errors
"""
from http import HTTPStatus

from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import Response
from starlette.routing import Route

from customtypes.invoice import InvoiceId
from entity.encoder import encode_to_json_response
from entity.events import InvoiceCreated
from persistence.helpers import _create_dummy_invoice
from persistence.mapper.dummy import DummyInvoiceMapper
from persistence.repository import InvoiceRepository
from usecases import create_invoice, get_invoice_by_id


async def get_invoice(request: Request) -> Response:
    # Read data from http request and do its validation
    invoice_id = InvoiceId(request.path_params["id"])

    # UseCase dependencies initialization
    mapper = DummyInvoiceMapper()
    repository = InvoiceRepository(mapper=mapper)

    # Running specific UseCase for getting an Invoice by its ID
    invoice = await get_invoice_by_id(invoice_id=invoice_id, repository=repository)

    # Encoding Invoice entity to JSON response according JSON:API specification (https://jsonapi.org)
    content = encode_to_json_response(entity=invoice)

    return Response(content=content, media_type="application/json")


async def create_new_invoice(request: Request) -> Response:
    # TODO Decode request and create invoice from data
    entity = _create_dummy_invoice(identifier=None)

    # UseCase dependencies initialization
    mapper = DummyInvoiceMapper()
    repository = InvoiceRepository(mapper=mapper)
    event = InvoiceCreated()

    # Running specific UseCase for creating new Invoice.
    # This UseCase also have dependency to Event (`InvoiceCreated`) what should be fired after Invoice is created.
    invoice = await create_invoice(invoice=entity, repository=repository, event=event)

    # Encoding Invoice entity to JSON response according JSON:API specification (https://jsonapi.org)
    content = encode_to_json_response(entity=invoice)

    return Response(
        content=content, status_code=HTTPStatus.CREATED, media_type="application/json"
    )


app = Starlette(
    debug=True,
    routes=[
        Route("/invoices/", create_new_invoice, methods=["POST"]),
        Route("/invoices/{id:int}/", get_invoice, methods=["GET"]),
    ],
)
