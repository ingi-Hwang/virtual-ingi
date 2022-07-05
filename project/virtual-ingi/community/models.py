from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
# Create your models here.

class Tag(models.Model): # 태그 모델
    name = models.CharField(max_length=12)
    def __str__(self):
        return self.name

class Users(models.Model): # 유저 모델
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=30, null=True)
    password = models.CharField(max_length=20, null=True)
    name = models.CharField(max_length=10)
    GENDERS = (
        ('M', '남성'),
        ('W', '여성'),
    )
    gender = models.CharField(verbose_name='성별', max_length=2, choices=GENDERS, default = '')

class Input(models.Model): # 처음 입력 모델
    #user_id = models.OneToOneField(Users, on_delete=models.CASCADE)

    id = models.AutoField(primary_key=True)
    startperiod = models.DateField(null=True)
    endperiod = models.DateField(null=True)
    startime = models.TimeField(null=True)
    tag = models.ManyToManyField(Tag, blank=True)

    area = models.CharField(max_length=20,default='')


class Tour(models.Model): # 관광지 모델
    name = models.CharField(max_length=30)
    tag = models.ManyToManyField(Tag, blank=True)
    tourTime = models.FloatField(null=True)
    tourLatitude = models.FloatField(blank=True)
    tourLongitude = models.FloatField(blank=True)
    tour_url = models.URLField('관광지 URL', max_length=400, blank=True,null=True,default='')
    visitCnt = models.IntegerField(null=True)
    def __str__(self):
        return self.name

class Restaurant(models.Model): # 식당 모델
    name = models.CharField(max_length = 20)
    restaurantTime = models.IntegerField(null=True)
    restaurantLatitude = models.FloatField(blank=True)
    restaurantLognitude = models.FloatField(blank=True)
    restaurant_url = models.URLField('식당 URL', max_length=400, blank=True,null=True,default='')
    image_file = models.ImageField('식당 이미지', upload_to='restaurants', blank=True, null=True)
    def __str__(self):
        return self.name

class Stay(models.Model): # 숙소 모델
    name = models.CharField(max_length=20)
    stayLatitude = models.FloatField(blank=True)
    stayLognitude = models.FloatField(blank=True)
    restaurant_url = models.URLField('숙소 UR', max_length=400, blank=True,null=True, default='')
    image_file = models.ImageField('숙소 이미지', upload_to='stays', blank=True, null=True)
    def __str__(self):
        return self.name

class Schedule(models.Model): # 일정리스트 모델
    user_id = models.OneToOneField(Users, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, blank=True)
    tour = models.ManyToManyField(Tour, blank=True)
    restaurant = models.ManyToManyField(Restaurant, blank=True)
    stay = models.ManyToManyField(Stay, blank=True)
