from django.db import models


class Snock(models.Model):
    ticker = models.CharField(max_length=10)

    def __str__(self):
        return self.ticker
    

# Create your models here.
