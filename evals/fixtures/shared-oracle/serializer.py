import json


def serialize_event(event: dict[str, object]) -> bytes:
    return json.dumps(event, separators=(",", ":"), sort_keys=True).encode("utf-8")
