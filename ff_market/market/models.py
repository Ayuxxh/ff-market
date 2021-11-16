from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
from account.models import User

class Tag(models.Model):
    id =  models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name    

class Product(models.Model):
    id =  models.AutoField(primary_key=True)
    offer_detail = models.CharField(max_length=255, default="No name")
    description = models.CharField(max_length=2000)
    price = models.IntegerField() 
    seller = models.ForeignKey(User, on_delete=models.CASCADE),
    tag = models.ManyToManyField(Tag,related_name='products')
    delivery = models.CharField(choices=[
        ("INSTANT","Instant delivary."),
        ("1HOUR","May take upto a hour."),
        ("2HOUR", "May take upto 2 hours."),
        ("5HOUR","May take upto 5 hours"),
        ("1DAY","May take upto a day."),
        ("2DAY", "May take upto 2 days."),  
         ]),
    post_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.offer_detail