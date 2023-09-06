from django.contrib import admin
from WebApp.models import Student,ClassModel

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','age']
admin.site.register(Student)

class ClassAdmin(admin.ModelAdmin):
    list_display=['class_name','class_eligibility']
admin.site.register(ClassModel)