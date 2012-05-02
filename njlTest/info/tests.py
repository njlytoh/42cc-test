"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase

from info.models import InfoSingleton


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

        obj_0 = InfoSingleton.objects.create(name='Asdf', surname='Tom', date_of_birth="1983-11-02")
        self.assertEqual(InfoSingleton.objects.count(), 1)
        self.assertEqual(InfoSingleton.objects.all()[0].surname, 'Tom')
        self.assertEqual(InfoSingleton.objects.all()[0].name, 'Asdf')

        obj = InfoSingleton.objects.create(name='Andriy', surname='Tomchuk', date_of_birth="1983-11-02", 
                                            bio='Some biographic info about myself',    
                                            email='njlytoh@gmail.com', jabber='njlytoh@gmail.com',
                                            skype='njlytoh', other_contacts='phone: +3809374736283')
        
        self.assertEqual(InfoSingleton.objects.count(), 1)
        self.assertEqual(InfoSingleton.objects.all()[0].name, obj.name)
        self.assertEqual(InfoSingleton.objects.all()[0].other_contacts, obj.other_contacts)

