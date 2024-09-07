from django import forms
from .models import User,Profile

class UserRegisterForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('national_code','password',)

