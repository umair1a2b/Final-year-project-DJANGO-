from django.db import models

# Create your models here.
class User(models.Model):
    first_name=models.CharField('first_name',max_length=20)
    last_name=models.CharField('last_name',max_length=20)
    password = models.TextField('password', max_length=20)
    email = models.TextField('email', max_length=50)
    phone=models.IntegerField('phone')
    type=models.IntegerField('type')

class Hall(models.Model):
    user_id= models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='images/')
    name= models.CharField('name', max_length=20)
    capacity = models.IntegerField('capacity')
    address = models.TextField('address' , max_length=50)
    phone = models.IntegerField('phone')
    description = models.TextField('description')
    video=models.TextField('video')
    dj = models.TextField('dj')
    flourist= models.TextField('flourist')
    type= models.TextField('type')
    separation= models.TextField('separation')
    menu=models.TextField('menu')

class Book(models.Model):
    user_id= models.ForeignKey(User,on_delete=models.CASCADE)
    hall_id = models.ForeignKey(Hall, on_delete=models.CASCADE)
    capacity=models.IntegerField('capacity')
    event= models.TextField('event')
    videographer = models.TextField('videographer')
    package = models.TextField('package')
    menu=models.TextField('menu')
    decor = models.TextField('decor')
    separate = models.TextField('separate')
    dj = models.TextField('dj')
    date= models.TextField('date')