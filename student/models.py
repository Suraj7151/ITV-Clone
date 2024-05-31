from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class module(models.Model):
    image = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=50,null=True)
    progress = models.CharField(max_length=50,null=True)
    status = models.CharField(max_length=50,null=True)
    link = models.CharField(max_length=100,null=True)


    def __str__(self):
        return self.name
    
    class Meta:
        db_table='module'


class openings(models.Model):
    role = models.CharField(max_length=30,null=True)
    salary = models.CharField(max_length=50,null=True)
    location = models.CharField(max_length=50,null=True)
    company_name = models.CharField(max_length=100,null=True)
    # logo = models.ImageField(null=True,blank=True)
    # added_on = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.company_name

    class Meta:
        db_table='openings'

class profile(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    firstname=models.CharField(max_length=100,null=True)
    middlename=models.CharField(max_length=100,null=True)
    lastname=models.CharField(max_length=100,null=True)
    email=models.CharField(max_length=100,null=True)
    email=models.CharField(max_length=100,null=True)
    mobile=models.CharField(max_length=20,null=True)
    dob=models.DateField()
    gender=models.CharField(max_length=1, choices=GENDER_CHOICES)
    address=models.TextField(max_length=300,)
    guardian=models.CharField(max_length=30)
    contact=models.CharField(max_length=12)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.firstname

    class Meta:
        db_table='profile'

from django import forms

class profileForm(forms.ModelForm):
    class Meta:
        model=profile
        fields='__all__'

class Interview(models.Model):
    img = models.ImageField(null=True,blank=True)
    name = models.CharField(max_length=50,null=True)
    link = models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table='interview'

class LoginForm(forms.ModelForm):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=30, widget=forms.PasswordInput)


class InterviewQuestions(models.Model):
    ques = models.CharField(max_length=100,null=True)
    ans = models.CharField(max_length=1500,null=True)

    def __str__(self):
        return self.ques

    class Meta:
        db_table='interviewQuestions'    

    
    