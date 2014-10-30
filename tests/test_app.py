import unittest
import os
import base64

os.environ['USERNAME'] = "foo"
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


    def make_headers(self):
        auth = base64.b64encode("foo" + b':' + "bar")
        return {'Authorization': b'Basic ' + auth}

if __name__ == '__main__':
    unittest.main()
