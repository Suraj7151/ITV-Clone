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
admin.site.register(Cart)


class StudyMaterialAdmin(admin.ModelAdmin):
    list_display=['id','material_id','title','content','studytopic']
    list_filter=['material_id','studytopic']
    ordering=['material_id']
admin.site.register(StudyMaterial,StudyMaterialAdmin)
admin.site.register(StudyTopic)
admin.site.register(CourseCategories)
admin.site.register(Course)
admin.site.register(CourseSubCategory)
admin.site.register(Order)
admin.site.register(OrderItem)

