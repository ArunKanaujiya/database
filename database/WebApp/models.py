from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()

    def __str__(self):
        return self.name


class ClassModel(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    class_name=models.CharField(max_length=100)
    class_eligibility=models.IntegerField()
    def __str__(self):
        return str(self.id)+' '+self.class_name

    