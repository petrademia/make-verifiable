import unittest

from serializer import serialize_event
from shared_oracle import expected_wire


class UnitSerializerTests(unittest.TestCase):
    def test_created_event(self):
        event = {"type": "created", "id": 7}
        self.assertEqual(serialize_event(event), expected_wire(event))


if __name__ == "__main__":
    unittest.main()
