from django.db import models
from django.shortcuts import render
# Create your models here.
from django.db import models


class new_user( models.Model):
    username=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    pin_code=models.CharField(max_length=200)
    phone_no=models.CharField(max_length=200)
    job_type=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
