from django.test import TestCase
from .models import foodType, userDetail, guestReview, hostReview

from .views import index, getTypes, getUsers
from django.urls import reverse
from django.contrib.auth.models import User

# Create your tests here.
class FoodTypeTest(TestCase):
   def test_string(self):
       type=foodType(typeName="Vegetarian")
       self.assertEqual(str(type), type.typeName)

   def test_table(self):
       self.assertEqual(str(foodType._meta.db_table), 'foodType')


class memberTest(TestCase):
   #set up one time sample data
   def setup(self):
       type = foodType(typeName='vegetarian')
       username=userDetail(userName='guest2', foodType=type, userLocation='Seattle')
       return username
   def test_string(self):
       user = self.setup()
       self.assertEqual(str(user), user.userName)
  
   #test the discount property
   
   def test_type(self):
       user=self.setup()
       self.assertEqual(str(user.foodType), 'vegetarian')

   def test_table(self):
       self.assertEqual(str(userDetail._meta.db_table), 'member')

class guestReviewTest(TestCase):
   def test_string(self):
       rev=guestReview(guestReviewTitle="Best Host Review")
       self.assertEqual(str(rev), rev.guestReviewTitle)

   def test_table(self):
       self.assertEqual(str(hostReview._meta.db_table), 'hostUserReview')

class hostReviewTest(TestCase):
   def test_string(self):
       rev=hostReview(hostReviewTitle="Best Host Review")
       self.assertEqual(str(rev), rev.hostReviewTitle)

   def test_table(self):
       self.assertEqual(str(hostReview._meta.db_table), 'hostUserReview')

class IndexTest(TestCase):
   def test_view_url_accessible_by_name(self):
       response = self.client.get(reverse('index'))
       self.assertEqual(response.status_code, 200)
  
class GetMemberTest(TestCase):
   def test_view_url_accessible_by_name(self):
       response = self.client.get(reverse('members'))
       self.assertEqual(response.status_code, 200)

   def setUp(self):
       self.u=User.objects.create(username='myuser')
       self.type=foodType.objects.create(typeName='vegetarian')
       self.user = userDetail.objects.create(userName='user1', foodType=self.type, user=self.u, userLocation="Idaho", userJoinDate='2019-04-02', userDescription="a user")
       self.rev1=guestReview.objects.create(guestReviewTitle='guestreview', guestReviewDate='2019-04-03', guestUser=self.user, guestReviewrating=4, guestReviewText='some review')
       self.rev1.user.add(self.u)
       self.rev2=Review.objects.create(hostReviewTitle='hostreview', hostReviewDate='2019-04-03', hostuser=self.user,  hoststReviewRating=4, hostReviewText='some other review')
       self.rev2.user.add(self.u)

   def test_product_detail_success(self):
       response = self.client.get(reverse('userDetails', args=(self.user.id,)))
       # Assert that self.post is actually returned by the post_detail view
       self.assertEqual(response.status_code, 200)

        
   def test_number_of_reviews(self):
       reviews=guestReview.objects.filter(user=self.user).count()
       self.assertEqual(reviews, 2)