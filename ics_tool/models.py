# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# Database Tables should be defined as class object
class Customer(models.Model):
    CustomerId = models.IntegerField(unique=True)
    CustomerName = models.CharField(max_length=200)
