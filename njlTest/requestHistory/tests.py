"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test import Client 

from requestHistory.middleware import HistoryMiddleware

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)


class HistoryMiddlewareTest(TestCase):
    def test_process_request(self):
        h_m = HistoryMiddleware()
        client = Client()
        client.get('/asdf')
        self.assertEqual( '', '')
        response = client.get('/requests')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.content.find('http://testserver/asdf'), -1)
