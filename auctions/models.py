from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Auctions(models.Model):
    Id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    userName = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="auction_author")
    description = models.CharField(max_length=500)
    sprice = models.IntegerField()
    picture = models.CharField(max_length=500)
    #auctionTime = models.DateField()

    def __str__(self):
        return f"{self.Id}: {self.name} - Price: {self.sprice} - Description: {self.description}"


class Comments(models.Model):
    commentId = models.AutoField(primary_key=True)
    auctionId = models.ForeignKey(Auctions, on_delete=models.CASCADE, related_name="Avis") 
    userName = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="comment_author")
    comment = models.CharField(max_length=500)
    commentTime = models.DateField()
    def __str__(self):
        return f"{self.commentId} - Auction: {self.auctionId} by {self.userName}"

class Bids(models.Model):
    bidsId = models.AutoField(primary_key=True)
    auctionId = models.ForeignKey(Auctions, on_delete=models.CASCADE) 
    userName = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="bid_author")

    bid = models.IntegerField()

class Watchlist(models.Model):
    userName = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="waList_author")
    auctionId = models.ForeignKey(Auctions, on_delete=models.CASCADE) 


    #bidTime = models.DateField()

    #aa = Auctions(name="Chaise", description="Belle chaise", sprice=15)
    