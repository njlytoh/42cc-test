"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client


from info.models import Info


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

class TestInfoModel(TestCase):
    
    def test_model(self):
        """
        Tests info model. Tests also its Singleton property status(only one item should be created in the db)
        """

        obj_0 = Info.objects.create(name='Asdf', surname='Tom', date_of_birth="1983-11-02")
        obj_1 = Info.objects.create(name='Asd1', surname='T1m', date_of_birth="1983-11-02")
        self.assertEqual(Info.objects.count(), 1)
        self.assertEqual(Info.objects.all()[0].surname, 'T1m')
        self.assertEqual(Info.objects.all()[0].name, 'Asd1')

        obj = Info.objects.create(name='Andriy', surname='Tomchuk', date_of_birth="1983-11-02", 
                                            bio='Some biographic info about myself',    
                                            email='njlytoh@gmail.com', jabber='njlytoh@gmail.com',
                                            skype='njlytoh', other_contacts='phone: +3809374736283')
        
        self.assertEqual(Info.objects.count(), 1)
        self.assertEqual(Info.objects.all()[0].name, obj.name)
        self.assertEqual(Info.objects.all()[0].other_contacts, obj.other_contacts)

    def test_view(self):
        
        c = Client()
        response = c.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(   response.content.find('Some biographic info about myself'), -1)



