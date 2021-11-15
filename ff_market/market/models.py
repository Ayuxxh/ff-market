from functools import _Descriptor
from django.db import models
from django.db.models.deletion import CASCADE

class Tag(models.Model):
    id =  models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name    

class Product(models.Model):
    id =  models.AutoField(primary_key=True)
    offer_detail = models.CharField(max_length=255),
    description = models.CharField(max_length=2000)
    price = models.IntegerField(max_length=100) ,
    seller = models.ForeignKey("modelname", on_delete=models.CASCADE),
    tag = models.ForeignKey(Tag,on_delete=CASCADE),
    delivery = models.CharField(choices=[
        "INSTANT",
        "1HOUR",
        "2HOUR",
        "5HOUR",
        "1DAY",
        "2DAY",  
         ]),
    post_time = models.DateField()

    def __str__(self):
        return self.offer_detail