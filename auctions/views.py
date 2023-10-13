from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages

import re
from datetime import date # todayDate = date.today()

from .models import User, Auctions, Comments, Bids

def newListing(request):
    #if request.method == "GET":
    #    return render(request, "auctions/newListing.html")

    if request.method == "POST":  ##here strangely if you post it
        auctionName = request.POST['auctionName']
        auctionPrice = request.POST['auctionPrice']
        auctionDescription = request.POST['auctionDescription']

        if re.search(r"^[a-zA-Z].{2}.*$", auctionName) and re.search(r"^[1-9]+$", auctionPrice) and re.search(r"^[a-zA-Z]*$", auctionDescription):
            return render(request, "auctions/index.html",)
        else:
            return render(request, "auctions/newListing.html", {
                "error": "Invalid Input"
            })
 
    return render(request, "auctions/newListing.html",)

def index(request):
    return render(request, "auctions/index.html", {"auctions": Auctions.objects.all()})


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
