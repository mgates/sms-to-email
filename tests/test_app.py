import unittest
import os
import base64
import re
from mock import MagicMock
from mock import patch

os.environ['USER'] = "foo"
os.environ['PASSWORD'] = "bar"

import sms2email
#import mail_sender

class TestSms2Email(unittest.TestCase):
    def setUp(self):
        self.app = sms2email.app.test_client()

    def test_unauthenticated_response_gets_401(self):
        resp = self.app.get(self.request())
        self.assertEqual(resp.status, "401 UNAUTHORIZED")

    @patch("sms2email.send_mail")
    def test_authenticated_response_gets_200(self, _mock):
        resp = self.app.get(self.request(), headers=self.make_headers())
        self.assertEqual(resp.status, "200 OK")

    @patch("sms2email.send_mail")
    def test_it_sends_a_message(self, m):
        resp = self.app.get(self.request(), headers=self.make_headers())
        m.assert_called

    @patch("sms2email.send_mail")
    def test_the_message_has_a_link_to_the_picture(self, m):
        resp = self.app.get(self.request(), headers=self.make_headers())
        print m.call_args[0][1]
        self.assertTrue(re.compile('.*https://api.twilio.com.*').search(m.call_args[0][1]))


    def make_headers(self):
        auth = base64.b64encode("foo" + b':' + "bar")
        return {'Authorization': b'Basic ' + auth}

    def request(self):
        return "/message?ToCountry=US&MediaContentType0=image/jpeg&ToState=IL&SmsMessageSid=MMb24ebf0febf6dec63f93689f53a76be7&NumMedia=1&ToCity=LOMBARD&FromZip=21204&SmsSid=MMb24ebf0febf6dec63f93689f53a76be7&FromState=MD&SmsStatus=received&FromCity=TOWSON&Body=&FromCountry=US&To=%2B13126464623&ToZip=60148&MessageSid=MMb24ebf0febf6dec63f93689f53a76be7&AccountSid=ACa48df91e3da71788edf77af601009a28&From=%2B14438243329&MediaUrl0=https://api.twilio.com/2010-04-01/Accounts/ACa48df91e3da71788edf77af601009a28/Messages/MMb24ebf0febf6dec63f93689f53a76be7/Media/ME503fd32f587bd15cb37ea1778b4fa2c4&ApiVersion=2010-04-01"



if __name__ == '__main__':
    unittest.main()
