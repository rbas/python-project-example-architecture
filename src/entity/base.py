from abc import ABCMeta
from dataclasses import asdict, dataclass
from typing import Dict, Type, Union

from customtypes.basic import ID


@dataclass
class AbstractEntity(metaclass=ABCMeta):
    id: Union[Type[ID], None]

    def as_dict(self) -> Dict:
        raw_data = asdict(self)
        attributes = raw_data
        del attributes["id"]
        return {
            "type": self.entity_type(),
            "id": self.entity_identifier,
            "attributes": attributes,
        }

    @classmethod
    def entity_type(cls) -> str:
        return cls.__name__

    @property
    def entity_identifier(self) -> Type[ID]:
        return self.id
