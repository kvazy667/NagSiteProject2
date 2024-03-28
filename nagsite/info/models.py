from django.db import models

# Create your models here.

class project(models.Model):
    name = models.CharField('название', max_length=100)
    description = models.TextField('описание')
    team_quantity = models.IntegerField ('количество участников')


    def __str__(self):
        return self.name


class person(models.Model):
    fio = models.CharField('ФИО', max_length=100)
    image = models.ImageField('фото')
    file = models.FileField('файл')

    def __str__(self):
        return self.fio
