from django.db import models
from realtors.models import Realtor

class Yashuv(models.Model):
    name = models.CharField(max_length =200)
    photo_main = models.ImageField(upload_to = 'photos/%Y/%m/%d/',blank = True)
    
