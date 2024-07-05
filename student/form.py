from django import forms
from django.contrib.auth.forms import SetPasswordForm, PasswordResetForm, PasswordChangeForm

class MyPasswordResetForm(PasswordResetForm):
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))


class MySetPasswordForm(SetPasswordForm):

    new_password1=forms.CharField(label='new Password',widget=forms.PasswordInput(attrs=
    {'autofocus': 'True' , 'autocomplete': 'current-password', 'class': 'form-control'}))

    new_password2=forms.CharField(label='confirm Password',widget=forms.PasswordInput(attrs=
    {'autofocus': 'True' , 'autocomplete': 'current-password', 'class' : 'form-control'}))