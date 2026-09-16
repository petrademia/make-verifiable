import unittest

from serializer import serialize_event
from shared_oracle import expected_wire


class IntegrationSerializerTests(unittest.TestCase):
    def test_deleted_event_wire_payload(self):
        event = {"type": "deleted", "id": 9, "reason": "expired"}
        emitted_payload = serialize_event(event)
        self.assertEqual(emitted_payload, expected_wire(event))


if __name__ == "__main__":
    unittest.main()
