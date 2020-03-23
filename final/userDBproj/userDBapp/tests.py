from django.test import TestCase
from .models import foodType, userDetail, guestReview, hostReview

# Create your tests here.
class FoodTypeTest(TestCase):
   def test_string(self):
       type=foodType(typeName="Vegetarian")
       self.assertEqual(str(type), type.typeName)

   def test_table(self):
       self.assertEqual(str(foodType._meta.db_table), 'foodtype')