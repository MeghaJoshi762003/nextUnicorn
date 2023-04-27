from email.policy import default
from django.contrib.auth.models import User
from unittest.util import _MAX_LENGTH
from django.db import models
class log(models.Model):
    username=models.CharField(max_length=30)
    userid=models.CharField(max_length=115,primary_key=True,default='7')
    email=models.EmailField(max_length=122)
    password=models.CharField(max_length=30)
    post=models.CharField(max_length=20,default='User')

class feedback(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=122)
    opinion=models.TextField()

class nuser(models.Model):
    profilepic=models.ImageField(upload_to="myapp/images",null=True,blank=True)
    userid=models.CharField(max_length=30,primary_key=True)
    bio=models.TextField(null=True,blank=True)
    skills=models.TextField(null=True,blank=True)
    facebook=models.URLField( max_length=200,null=True,blank=True,default="https://www.linkedin.com/feed/")
    twitter=models.URLField( max_length=200,null=True,blank=True,default="https://www.linkedin.com/feed/")
    instagram=models.URLField( max_length=200,null=True,blank=True,default="https://www.linkedin.com/feed/")
    linkedin=models.URLField( max_length=200,null=True,blank=True,default="https://www.linkedin.com/feed/")
    

    def __str__(self):
        return self.userid

class Image(models.Model):
   photo = models.ImageField(upload_to="images", default="")
   date = models.DateTimeField(auto_now_add=True )
   caption = models.CharField(max_length = 200 ,default="")
   userid=models.CharField(max_length=30)
#    post_like=models.ManyToManyField(User,related_name='likes')

class startup(models.Model):
    profilepic=models.ImageField(upload_to="images",null=True,blank=True)
    coverphoto=models.ImageField(upload_to="images",null=True,blank=True)
    startupid=models.CharField(max_length=30,primary_key=True)
    startuplink=models.URLField(null=True,blank=True)
    pitch=models.ImageField(upload_to="images",null=True,blank=True)
    email=models.EmailField(null=True,blank=True)
    phoneno=models.CharField(max_length=12,null=True,blank=True)
    about=models.TextField(null=True,blank=True)
    facebook=models.URLField( max_length=200,null=True,blank=True,default="https://www.linkedin.com/feed/")
    twitter=models.URLField( max_length=200,null=True,blank=True,default="https://www.linkedin.com/feed/")
    instagram=models.URLField( max_length=200,null=True,blank=True,default="https://www.linkedin.com/feed/")
    linkedin=models.URLField( max_length=200,null=True,blank=True,default="https://www.linkedin.com/feed/")
    form=models.URLField( max_length=200,null=True,blank=True,default="https://www.linkedin.com/feed/")

class suggestion(models.Model):
    date=models.DateTimeField(auto_now=True)
    to=models.CharField(max_length=30)
    by=models.CharField(max_length=30)
    opinion=models.TextField(null=True,blank=True)

class entrepreneur(models.Model):
    profilepic=models.ImageField(upload_to="myapp/images",null=True,blank=True)
    coverphoto=models.ImageField(upload_to="myapp/images",null=True,blank=True)
    entrepreneurid=models.CharField(max_length=30,primary_key=True)
    startup=models.TextField(null=True,blank=True)
    about=models.TextField(null=True,blank=True)
    email=models.EmailField(null=True,blank=True)
    facebook=models.URLField( max_length=200,null=True,blank=True,default="https://www.linkedin.com/feed/")
    twitter=models.URLField( max_length=200,null=True,blank=True,default="https://www.linkedin.com/feed/")
    instagram=models.URLField( max_length=200,null=True,blank=True,default="https://www.linkedin.com/feed/")
    linkedin=models.URLField( max_length=200,null=True,blank=True,default="https://www.linkedin.com/feed/")
    phoneno=models.CharField(max_length=12,null=True,blank=True)
    form=models.URLField( max_length=200,null=True,blank=True,default="https://www.linkedin.com/feed/")

class Comment(models.Model):
    comment=  models.CharField(max_length=500)  
    date = models.DateTimeField(auto_now_add=True )
    userid=models.CharField(max_length=30)
    post_id =models.IntegerField(max_length=20 ,default=0)

