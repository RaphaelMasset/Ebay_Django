from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Auctions(models.Model):
    auctionId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=500)
    sprice = models.IntegerField()
    picture = models.CharField(max_length=500)
    #auctionTime = models.DateField()

    def __str__(self):
        return f"{self.auctionId}: {self.name} - Price: {self.sprice} - Description: {self.description}"

#<img src="{% static 'encyclopedia/'%}{{title}}{{'logo.png'}}" style="height: 100px;" default="Auction picture">


class Comments(models.Model):
    commentId = models.AutoField(primary_key=True)
    actionId = models.ForeignKey(Auctions, on_delete=models.CASCADE, related_name="Avis") 

    userName = models.CharField(max_length=64)
    comment = models.CharField(max_length=500)
    commentTime = models.DateField()

class Bids(models.Model):
    actionId = models.AutoField(primary_key=True)
    bidsId = models.ForeignKey(Auctions, on_delete=models.CASCADE) 

    bid = models.IntegerField()
    bidTime = models.DateField()

    #aa = Auctions(name="Chaise", description="Belle chaise", sprice=15)