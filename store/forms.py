from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm , PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation
from .models import Customer


class CustomerRegistrationForm(UserCreationForm):
    password1 = forms.CharField( widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))
    password2 = forms.CharField( widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm Password'}))
    email = forms.EmailField( widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}))
    username = forms.CharField( widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}))
    first_name = forms.CharField( widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name','style':'margin-right:5px;'}))
    last_name = forms.CharField( widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name','style':'margin-left:5px;'}))
    class Meta:
        model = User
        fields = ['username','email','password1','password2','first_name','last_name']


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
    password = forms.CharField( strip=False,widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))


class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField( widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Current Password'}))
    new_password1 = forms.CharField( widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'New Password'}))
    new_password2 = forms.CharField( widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm Password'}))


class MyPasswordResetForm(PasswordResetForm):
   email = forms.EmailField( widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}))


class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(strip=False,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'New Password'}),help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(strip=False,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm Password'}))

class CustomerProfileView(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name','address','city','state','zipcode']
        widget = {
            'name':forms.TextInput(attrs={'class':'inputt'}),'address':forms.TextInput(attrs={'class':'inputt'}),'city':forms.TextInput(attrs={'class':'inputt'}),'state':forms.TextInput(attrs={'class':'inputt'}),'zipcode':forms.NumberInput(attrs={'class':'inputt'})
            }