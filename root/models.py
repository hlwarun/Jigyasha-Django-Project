from django.db import models

# Create your models here.

class Banner(models.Model):
    medium_text = models.CharField(max_length=25)
    large_text1 = models.CharField(max_length=15)
    large_text2 = models.CharField(max_length=15)
    small_text = models.CharField(max_length=50)

    def __str__(self):
        return "Edit Your Banner Text"
