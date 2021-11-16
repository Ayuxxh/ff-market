from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.db.models.fields import AutoField
from django.utils import timezone
from django.utils.translation import gettext_lazy as _



class User( models.Model):
    id = AutoField(primary_key=True)
    profile_picture = models.ImageField(upload_to='static/account/images/profile_picture/', default="static/account/images/profile_picture/default.jpeg'")
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    phone_number = models.IntegerField()
    email = models.EmailField(_('email address'), )
    date_joined = models.DateTimeField(default=timezone.now)
    password = models.CharField(max_length=26)
    confirm_password = models.CharField(max_length=26)
    rank = models.CharField(choices=[
        ("customer",'customer'),
        ("seller", 'seller'),
        ], max_length=20, default='customer')

    def __str__(self):
        return self.id, self.username

    def upgrade_to_seller(self):
        if self.rank == 'customer':
            self.rank = 'seller'
        else:
            print("user already seller")