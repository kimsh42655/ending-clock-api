from django.db import models

# Create your models here.
class Notice(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    link = models.CharField(max_length=200, default='')

    def  __str__(self):
        return self.title

