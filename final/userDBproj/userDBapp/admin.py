from django.contrib import admin
from django.contrib import admin
from .models import foodType, userDetail, guestReview, hostReview

# Register your models here.
admin.site.register(foodType)
admin.site.register(userDetail)
admin.site.register(guestReview)
admin.site.register(hostReview)
