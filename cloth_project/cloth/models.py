from django.db import models

# Create your models here.

class clothModel(models.Model):
    """Cloths details"""
    cloth_img = models.ImageField(upload_to='cloth_img', null=False, default='cloth_img/default.png')
    cloth_name = models.CharField(max_length=255,blank=True, null=True)
    cloth_type = models.CharField(max_length=255,blank=True,null=True)
    price = models.CharField(max_length=255, blank=True,null=True)

    def __str__(self):
        return self.cloth_name