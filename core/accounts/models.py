from typing import Any
from django.db import models
from django.contrib.auth.models import (AbstractBaseUser,BaseUserManager,PermissionsMixin)
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserManager(BaseUserManager):

    '''
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.

    '''
    
    def create_user(self,national_code,password,**extra_fields):
        '''
        Create and save a user with the given email and password and extra data.
        '''
        if not national_code:
            raise ValueError('Email must be set')
        user = self.model(national_code=national_code,**extra_fields)
        user.set_password(password)
        user.save()
        return user
    


    def create_superuser(self,national_code,password,**extra_fields):
        '''
        Create and save a SuperUser with the given email and password and extra data.
        '''
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True")
        return self.create_user(national_code,password,**extra_fields)

class User(AbstractBaseUser,PermissionsMixin):

    '''
    Custom User Model for our project
    '''

    national_code=models.IntegerField(max_length=10,unique=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    #is_verified = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'national_code'
    REQUIRED_FIELDS = []

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    objects = UserManager()


    def __str__(self):
        return str(self.national_code)
    
class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=255)
    phone_number = models.IntegerField(max_length=11,unique=True,null=True)
    email = models.EmailField(unique=True,null=True)
    grade = models.CharField(max_length=100)
    field_of_study = models.CharField(max_length=100)
    image = models.ImageField(blank=True,null=True)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user.national_code)
    
@receiver(post_save, sender=User)
def save_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
