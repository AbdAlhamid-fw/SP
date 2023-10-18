from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils import timezone


class UserManager(BaseUserManager):
    def create_user( self, username, password=None ):
        if not username:
            raise ValueError("Users must have a username.")

        user = self.model(
            username=self.normalize_email(username),
            last_login=timezone.now(),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser( self, username, password=None ):
        user = self.create_user(username, password)
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    email = models.EmailField()
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'username'
    objects = UserManager()



class SalesPerson(models.Model):

    northern_region = "northern"
    southern_region = "southern"
    coastal_region = "coastal"
    lebanese_region = "lebanese"
    REGION_STATE = [
        (northern_region, 'northern'),
        (southern_region, 'southern'),
        (coastal_region, 'coastal'),
        (lebanese_region, 'lebanese'),
    ]
    region = models.CharField(
        max_length=25,
        choices=REGION_STATE,

    )
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    img = models.FileField(upload_to='img')


class Sales(models.Model):
    date = models.CharField(max_length=50)
    sales_person = models.ForeignKey(SalesPerson, on_delete=models.CASCADE)
    northern = models.FloatField(default=0)
    southern = models.FloatField(default=0)
    coastal = models.FloatField(default=0)
    lebanese = models.FloatField(default=0)
    financial = models.FloatField(default=0)