from json import JSONEncoder, dumps

from typing import Any

from entity.base import AbstractEntity


class EntityToJsonEncoder(JSONEncoder):
    def default(self, o: Any) -> Any:
        if hasattr(o, "value"):
            return o.value
        return JSONEncoder.default(self, o)


def to_json(data: dict) -> str:
    return dumps(
        data,
        cls=EntityToJsonEncoder,
        ensure_ascii=False,
        allow_nan=False,
        indent=None,
        separators=(",", ":"),
    )


def encode_to_json_response(entity: AbstractEntity) -> bytes:
    return to_json(entity.as_dict()).encode("utf-8")
