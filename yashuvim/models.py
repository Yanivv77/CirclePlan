from django.db import models


class Yashuv(models.Model):
    name = models.CharField(max_length =200)
    photo_main = models.ImageField(upload_to = 'photos/%Y/%m/%d/',blank = True)
    Location = models.URLField(max_length =2000,blank=True)
    

    def __str__(self):
        return self.name
    
