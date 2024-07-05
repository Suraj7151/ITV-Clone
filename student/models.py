from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Module Model #

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

# Module Model Ends #

# Main Topic Starts #

from tinymce.models import HTMLField

class StudyTopic(models.Model):
    module=models.ForeignKey(module,on_delete=models.CASCADE)
    topic=models.CharField(max_length=100)

    def __str__(self):
        return self.topic
    
    class Meta:
        db_table='StudyTopic'

# Main Topic Model Ends #

# Subtopic Model Starts#

class StudyMaterial(models.Model):
    material_id=models.IntegerField(null=True)
    title = models.CharField(max_length=200)
    content =HTMLField()
    studytopic = models.ForeignKey(StudyTopic,on_delete=models.CASCADE,default=1)

    def __str__(self):
        return self.title
    
    class Meta:
        db_table='studyMaterial'

# Subtopic Model Ends#

# Subtopic Progress Model Starts#

class SubtopicProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(StudyTopic, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.completed
    
    class Meta:
        db_table='subtopicprogress'
    
# Subtopic Progress Model Ends#

# Openings Model Starts#

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

# Opening Model Ends #

# Profile Model Starts #

class profile(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    firstname=models.CharField(max_length=100,null=True)
    middlename=models.CharField(max_length=100,null=True)
    lastname=models.CharField(max_length=100,null=True)
    email=models.CharField(max_length=100,null=True)
    email=models.CharField(max_length=100,null=True)
    mobile=models.CharField(max_length=20,null=True)
    dob=models.DateField(null=True)
    gender=models.CharField(max_length=6, choices=GENDER_CHOICES)
    address=models.TextField(max_length=300,)
    guardian=models.CharField(max_length=30)
    contact=models.CharField(max_length=12)
    img=models.ImageField(blank=True,null=True)
    course = models.CharField(max_length=100,null=True)
    file = models.FileField(upload_to='documents',null=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE,unique=True)
    def __str__(self):
        return self.firstname

    class Meta:
        db_table='profile'

from django import forms

class profileForm(forms.ModelForm):
    class Meta:
        model=profile
        fields='__all__'

# Profile Model and Form Ends #

# Interview Questions Model Starts #

class Interview(models.Model):
    img = models.ImageField(null=True,blank=True)
    name = models.CharField(max_length=50,null=True)
    link = models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table='interview'

# Interview Questions Model Ends #

# Login Form Starts #

class LoginForm(forms.ModelForm):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=30, widget=forms.PasswordInput)

# Login Form Ends #

# Interview Questions&Answers Model Starts #

class InterviewQuestions(models.Model):
    moduleName = models.ForeignKey(Interview, on_delete=models.CASCADE)
    ques = models.CharField(max_length=100,null=True)
    ans = models.CharField(max_length=1500,null=True)
    

    def __str__(self):
        return self.ques

    class Meta:
        db_table='interviewQuestions'    

# Interview Questions&Answers Model Ends #

# Course and Course Categories Model Starts #

class CourseCategories(models.Model):
    name = models.CharField(max_length=100,null=True)
    details = models.TextField(max_length=200,null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'courseCategories'

class CourseSubCategory(models.Model):
    name = models.CharField(max_length=100,null=True)
    category = models.ForeignKey(CourseCategories,on_delete=models.CASCADE)

    class Meta:
        db_table='courseSubcategory'

    def __str__(self):
        return self.name
    


class Course(models.Model):
    category = models.ForeignKey(CourseCategories,on_delete=models.CASCADE)
    image = models.ImageField(null=True,blank=True)
    name = models.CharField(max_length=100,null=True)
    details = models.CharField(max_length=100,null=True)
    date = models.DateField()
    price = models.IntegerField()
    teacher = models.CharField(max_length=100,null=True)
    subcategory=models.ForeignKey(CourseSubCategory,on_delete=models.CASCADE)
    # user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'course'



# Course and Course Categories Model Ends #

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        db_table='cart'


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    payment_id = models.CharField(max_length=100, null=True, blank=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()