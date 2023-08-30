from django.db import models

class university(models.Model):
    name = models.CharField(max_length=190, default='')
    filiallari = models.PositiveIntegerField(default=1)
    kantrakti = models.PositiveIntegerField(default=1)
    

    def __str__(self) -> str:
        return self.name


class sumka(models.Model):
    color = models.CharField(max_length=201, default='')
    invented_country = models.CharField(max_length=201, default='')

    def __str__(self) -> str:
        return self.color