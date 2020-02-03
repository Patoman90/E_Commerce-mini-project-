from django.test import TestCase
from .models import Product
# Create your tests here.


class ProductTests(TestCase):
    """Here is where I wrote the tests for the Product Models"""
    def test_str(self):
        test_name = Product(name='A product')
        self.assertEqual(str(test_name), 'A product')
