from django.contrib import admin
from django.contrib.auth.models import User
from .models import *
# Register your models here.

admin.site.register(module)
admin.site.register(openings)
# admin.site.register(Topic)
# admin.site.register(Tag)
# admin.site.register(Article)
# admin.site.register(SubTopic)
admin.site.register(profile)
admin.site.register(Interview)
admin.site.register(InterviewQuestions)

