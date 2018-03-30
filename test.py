import unittest
import uuid

from okta_uuid import OktaUserId

class TestOktaUserId(unittest.TestCase):
    fake_id = '00ABCD1234wxyz5678pq'

    def test_instance(self):
        oid = OktaUserId(self.fake_id)
        self.assertEqual(str(oid), self.fake_id)
        self.assertEqual(eval(repr(oid)), oid)
        self.assertIsInstance(oid.uuid, uuid.UUID)

    def test_from_uuid(self):
        oid = OktaUserId(self.fake_id)
        new_oid = OktaUserId.from_uuid(oid.uuid)
        self.assertEqual(oid, new_oid)


if __name__ == '__main__':
    unittest.main()
