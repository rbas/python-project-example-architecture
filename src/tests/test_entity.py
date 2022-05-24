from dataclasses import dataclass

from entity.base import AbstractEntity


@dataclass
class SomeValueObject(AbstractEntity):
    id: int
    summary: str


def test_entity_as_dict():
    entity = SomeValueObject(id=1, summary="Blah")
    assert entity.as_dict() == {
        "type": "SomeValueObject",
        "id": 1,
        "attributes": {"summary": "Blah"},
    }
