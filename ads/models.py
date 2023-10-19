from django.db import models


class Ad(models.Model):
    name = models.TextField()
    date = models.DateField()
    price = models.IntegerField()
    img = models.ImageField(upload_to='ads/images/')

    def __str__(self):
        return self.name


class Person(models.Model):
    verif = models.BooleanField()
    date = models.DateField()
    phone = models.TextField()
    link = models.TextField()
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)

    STATUS = [
        ('моментально', 'моментально'),
        ('за 5 минут', 'за 5 минут'),
        ('за пол часа', 'за пол часа'),
        ('окола часа', 'окола часа'),
        ('в течении дня', 'в течении дня'),
    ]

    #response = models.PositiveSmallIntegerField(('status'), choices=STATUS, default=4)
    response = models.CharField(max_length=30,choices=STATUS, default='в течении дня')

    def __str__(self):
        return self.phone
