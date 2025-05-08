from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    #number = 
    #profile_pic = 
    pass

class Categories(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Currency(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Post(models.Model):
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    price = models.IntegerField(null=True)
    currency = models.ForeignKey(Currency, default='som', on_delete= models.SET_DEFAULT)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    adress = models.TextField(null=True)
    categorie = models.ForeignKey(Categories, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title

class Message(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
