from django import forms
from .models import SignUp,Admin,Manager,Restaurants
class DateInput(forms.DateInput):
    input_type = "date"


class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = "__all__"
        widgets = {"dateofbirth":DateInput(),"password":forms.PasswordInput(),'fullname': forms.TextInput(attrs={'placeholder': 'Enter Full Name'}),'email': forms.TextInput(attrs={'placeholder': 'Enter Email Address'})}

class AdminLoginForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = "__all__"
        widgets = {"password":forms.PasswordInput()}

class ManagerForm(forms.ModelForm):
    class Meta:
        model = Manager
        fields = "__all__"
        widgets = {"dateofbirth":DateInput(),"password":forms.PasswordInput(),'fullname': forms.TextInput(attrs={'placeholder': 'Enter Full Name'}),'email': forms.TextInput(attrs={'placeholder': 'Enter Email Address'})}

class RestaurantsForm(forms.ModelForm):
    class Meta:
        model = Restaurants
        fields = "__all__"
        labels = {"category":"Select Category"}