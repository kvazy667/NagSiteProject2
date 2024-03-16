from django.db import models

# Create your models here.

class project(models.Model):
    name = models.CharField('название', max_length=100)
    description = models.TextField('описание')
    team_quantity = models.IntegerField ('количество участников')


    def __str__(self):
        return self.name