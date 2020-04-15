from django.conf import settings
from django.test import Client
from unittest import TestCase
from urllib.parse import urlencode
import json

class LoginTest(TestCase):

    client = Client()

    def test(self):

        data = {
            'username': settings.USER_TEST,
            'password': settings.PASSWORD_TEST
        }

        response = self.client.post('/login/', urlencode(data), content_type='application/x-www-form-urlencoded')

        self.assertEqual(response.status_code, 200)

        token = json.loads(response.content)['token']

        return token