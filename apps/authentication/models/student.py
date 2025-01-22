from django.db import models
from apps.base.models import BaseModel
from django.contrib.auth.models import AbstractBaseUser


class UserMaster(AbstractBaseUser, BaseModel):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    password = models.CharField()
    phone_number = models.BigIntegerField()
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"

    class Meta:
        db_table = "user_master"
