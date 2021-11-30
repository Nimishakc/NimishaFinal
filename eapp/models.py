from django.db import models

class Onlinepayment(models.Model):
    name = models.TextField(max_length=20)
    address = models.TextField(max_length=20)
    city = models.TextField(max_length=20)
    ph = models.TextField(max_length=12,default='123')
    mail = models.TextField(max_length=35)
    item = models.TextField(max_length=20)
    imo = models.TextField(max_length=20)
    credit = models.TextField(max_length=12,default='123')

class Offlinepayment(models.Model):
    name = models.TextField(max_length=20)
    address = models.TextField(max_length=20)
    city = models.TextField(max_length=20)
    ph = models.TextField(max_length=12,default='123')
    mail = models.TextField(max_length=35)
    item = models.TextField(max_length=20)
    imo = models.TextField(max_length=20)

class Onlineapproval(models.Model):
    name = models.TextField(max_length=20)
    address = models.TextField(max_length=20)
    city = models.TextField(max_length=20)
    ph = models.TextField(max_length=12,default='123')
    mail = models.TextField(max_length=35)
    item = models.TextField(max_length=20)
    imo = models.TextField(max_length=20)
    credit = models.TextField(max_length=12,default='123')

class Offlineapproval(models.Model):
    name = models.TextField(max_length=20)
    address = models.TextField(max_length=20)
    city = models.TextField(max_length=20)
    ph = models.TextField(max_length=12,default='123')
    mail = models.TextField(max_length=35)
    item = models.TextField(max_length=20)
    imo = models.TextField(max_length=20)

class Send(models.Model):
    email = models.CharField(max_length=35)
    otpcheck = models.TextField(max_length=6)