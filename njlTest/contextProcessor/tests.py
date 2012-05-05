"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)


from django.test import TestCase
from django.template import RequestContext
from django.http import HttpRequest

class ContextProcessorTestCase(TestCase):
    """
    Populate this class with unit tests for your application
    """
    urls = 'contextProcessor.test_urls'

    def testProcessor(self):
        context = RequestContext(HttpRequest())
        self.assertTrue('django_settings' in context)
