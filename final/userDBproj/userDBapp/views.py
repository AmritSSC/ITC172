from django.shortcuts import render
from .models import foodType, userDetail, guestReview, hostReview

# Create your views here.
def index (request):
    return render(request, 'userDBapp/index.html')

def getTypes(request):
    type_list=foodType.objects.all()
    return render(request, 'userDBapp/types.html' ,{'type_list' : type_list})

def getUsers(request):
    members_list=userDetail.objects.all()
    return render(request, 'userDBapp/members.html', {'member_list': members_list})

def userDetails(request, id):
    userName=get_object_or_404(userDetail, pk=id)
    userFoodType=userName.foodType
    userLoc=userName.userLocation
    guestReviews=guestReview.objects.filter(product=id).count()
    hostReviews=hostReview.objects.filter(product=id).count()
    context={
        'Member' : userName,
        'Location' : userLoc,
        'Food Type' : userFoodType,
        'Guest Reviews' : guestReviews,
        'Host Reviews' : hostReviews,
    }
    return render(request, 'userDBapp/userDetails.html', context=context)