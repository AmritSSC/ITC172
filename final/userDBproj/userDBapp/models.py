from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class foodType(models.Model):
    typeName=models.CharField(max_length=64)
    typeDescription=models.CharField(max_length=10241)

    def __str__(self):
        return self.typeName
    
    class Meta:
        db_table='foodType'
        verbose_name_plural='foodTypes'


class userDetail(models.Model):
    userName=models.CharField(max_length=64)
    foodType=models.ForeignKey(foodType, on_delete=models.DO_NOTHING)
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    userLocation=models.CharField(max_length=255)
    userJoinDate=models.DateField()
    userAllergies=models.CharField(max_length=1024)
    userFavorites=models.CharField(max_length=1024)
    userDescription=models.TextField()

    def __str__(self):
        return self.userName
    
    class Meta:
        db_table='member'
        verbose_name_plural='members'


class guestReview(models.Model):
    guestReviewTitle=models.CharField(max_length=255)
    guestReviewDate=models.DateField()
    guestUserReviewed=models.ForeignKey(userDetail, on_delete=models.CASCADE)
    guestUser=models.ManyToManyField(User)
    guestreviewRating=models.SmallIntegerField()
    guestreviewText=models.TextField()

    def __str__(self):
        return self.guestReviewTitle
    
    class Meta:
        db_table='guestUserReview'
        verbose_name_plural='guestUserReviews'

class hostReview(models.Model):
    hostReviewTitle=models.CharField(max_length=255)
    hostReviewDate=models.DateField()
    hostUserReviewed=models.ForeignKey(userDetail, on_delete=models.CASCADE)
    hostUser=models.ManyToManyField(User)
    hostReviewRating=models.SmallIntegerField()
    hostReviewText=models.TextField()

    def __str__(self):
        return self.hostReviewTitle
    
    class Meta:
        db_table='hostUserReview'
        verbose_name_plural='hostUserReviews'