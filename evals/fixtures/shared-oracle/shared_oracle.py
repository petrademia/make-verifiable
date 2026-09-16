from serializer import serialize_event


def expected_wire(event: dict[str, object]) -> bytes:
    return serialize_event(event)
