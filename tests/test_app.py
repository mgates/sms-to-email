import unittest
import os
import base64
from mock import MagicMock

os.environ['USER'] = "foo"
os.environ['PASSWORD'] = "bar"

import sms2email


class TestSms2Email(unittest.TestCase):
    def setUp(self):
        self.app = sms2email.app.test_client()

    def test_unauthenticated_response_gets_401(self):
        resp = self.app.post('/message')
        self.assertEqual(resp.status, "401 UNAUTHORIZED")

    def test_authenticated_response_does_not_get_401(self):
        resp = self.app.post('/message', headers=self.make_headers())
        self.assertNotEqual(resp.status, "401 UNAUTHORIZED")

    def test_it_sends_a_message(self):
        self.app.send_message = MagicMock(return_value=True)
        resp = self.app.post('/message', headers=self.make_headers())
        self.app.send_message.assert_called()

    def make_headers(self):
        auth = base64.b64encode("foo" + b':' + "bar")
        return {'Authorization': b'Basic ' + auth}

if __name__ == '__main__':
    unittest.main()
