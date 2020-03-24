from django import forms
from .models import foodType, userDetail, guestReview, hostReview

class userForm(forms.ModelForm):  
    class Meta:
        model=userDetail
        fields='__all__'
        

