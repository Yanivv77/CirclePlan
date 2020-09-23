from django.db import models
from datetime import datetime

from django.contrib.auth.models import User

class Instructor(models.Model):

    name = models.CharField(max_length = 200)
    password = models.CharField(max_length = 200)
    password  = models.CharField(max_length=50)
    usertype = 'Instructor'
    photo =models.ImageField(upload_to = 'photos/%Y/%m/%d/' ,blank = True)
    description = models.TextField(max_length = 500)
    phone = models.CharField(max_length = 20)
    email = models.CharField(max_length = 50)
    active = models.BooleanField(default=False)
    hire_date = models.DateTimeField(default = datetime.now ,blank = True)
    


   
    def __str__(self):
        return self.name

