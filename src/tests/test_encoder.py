from customtypes.invoice import Amount, InvoiceId, PricePerUnit, Summary, Unit
from entity.encoder import to_json
from entity.entities import Invoice
from entity.valueobject import InvoiceItem


def test_encode_custom_types():

    data = {"amount": Amount(42), "points": 11.1}
    json = to_json(data)
    assert json == '{"amount":42,"points":11.1}'


def test_encode_invoice_entity():
    items = (
        InvoiceItem(
            amount=Amount(85),
            unit=Unit.PCS,
            summary=Summary("A"),
            price_per_unit=PricePerUnit(32.0),
        ),
    )
    invoice = Invoice(id=InvoiceId(2), items=items)

    json = to_json(invoice.as_dict())

    assert (
        json
        == '{"type":"Invoice","id":2,"attributes":{"items":[{"amount":85,"unit":"pcs","summary":"A","price_per_unit":32.0}],"state":"new"}}'
    )
