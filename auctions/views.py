from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib import messages

import re
from datetime import datetime, date # todayDate = date.today()

from .models import User, Auctions, Comments, Bids, Watchlist

def newListing(request):
    #if request.method == "GET":
    #    return render(request, "auctions/newListing.html")

    if request.method == "POST":  ##here strangely if you post it
        auctionName = request.POST['auctionName']
        auctionPrice = request.POST['auctionPrice']
        auctionDescription = request.POST['auctionDescription']
        auctionImageUrl = request.POST['auctionDescription']

        if re.search(r"^[a-zA-Z].{2}.*$", auctionName) and re.search(r"^[0-9]+$", auctionPrice) and re.search(r"^[a-zA-Z]*.*$", auctionDescription):
            NewAuction = Auctions(name=auctionName, description=auctionDescription, sprice=auctionPrice, picture=auctionImageUrl, userName=request.user)
            NewAuction.save()
            return HttpResponseRedirect(reverse(index))
        else:
            return render(request, "auctions/newListing.html", {
                "error": "Invalid Input"
            })
 
    return render(request, "auctions/newListing.html",)

def index(request):
    return render(request, "auctions/index.html", {"auctions": Auctions.objects.all()})

def item(request, title):

    if request.method == "POST":

        if 'newComment' in request.POST:
            newComment = request.POST['newComment']
            #Auctions.objects.get(name=title)
            auction_instance = Auctions.objects.get(name=title)
            user_instance = request.user
            newComment = Comments(auctionId=auction_instance, userName=user_instance, comment=newComment, commentTime=timeNow())
            newComment.save()

        if 'newBid' in request.POST:
            auction_instance = Auctions.objects.get(name=title)
            if request.POST['newBid'].isnumeric() and auction_instance.sprice < int(request.POST['newBid']):
                
                user_instance = request.user
                auction_instance.sprice = int(request.POST['newBid'])
                auction_instance.save()
                NewBid = Bids(auctionId=auction_instance, userName=user_instance, bid=request.POST['newBid'])
                NewBid.save()

        if 'delate' in request.POST:
            Auctions.objects.get(name=title).delete()
            return HttpResponseRedirect(reverse("index"))
        
        if 'watchlist' in request.POST:
            auction_instance = Auctions.objects.get(name=title)
            newFav = Watchlist(auctionId=auction_instance, userName=request.user)
            newFav.save()

    auction = get_object_or_404(Auctions, name=title)
    # Retrieve comments related to the specific auction
    comments = Comments.objects.filter(auctionId=auction)
    return render(request, "auctions/item.html", {
        "auction": Auctions.objects.get(name=title),
        "comments": comments
    })

def watchlist(request):
    user_watchlist = Watchlist.objects.filter(userName=request.user)
    
    auctions_in_watchlist = Auctions.objects.filter(Id__in=user_watchlist.values('auctionId'))

    return render(request, "auctions/watchlist.html", {
        "auctions": auctions_in_watchlist
    })

def categories(request):
    return render(request, "auctions/categories.html", {
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def timeNow():
    actualDate = datetime.now()
    # Formatez la date selon le format "Oct. 15, 2023"
    actualDate = datetime.now()
    formatted_date = actualDate.strftime("%Y-%m-%d")
    return formatted_date