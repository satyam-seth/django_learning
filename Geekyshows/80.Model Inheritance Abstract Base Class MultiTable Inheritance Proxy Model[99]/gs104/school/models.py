from django.db import models

# Create your models here.

class ExamCenter(models.Model):
    cname=models.CharField(max_length=70)
    city=models.CharField(max_length=70)

class MyExamCenter(ExamCenter):
    class Meta:
        proxy=True
        # ordering=['id']
        ordering=['city']