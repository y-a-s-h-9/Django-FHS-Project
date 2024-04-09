from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q
from django.shortcuts import render, redirect
from .forms import SignUpForm, RestaurantsForm, ManagerForm
from .models import SignUp, Admin, Restaurants, Manager, Cus


# Create your views here.
def index(request):
    return render(request,"index.html")

def signup(request):
    form = SignUpForm()
    if request.method == "POST":
        formdata = SignUpForm(request.POST)
        if formdata.is_valid():
            formdata.save()

            msg="Successfully Registered"
            return render(request,"index.html",{"msg":msg})
        else:
            msg="Failed to signup"
            return render(request,"signup.html",{"signupform":form,"msg":msg})
    return render(request,"signup.html",{"signupform":form})





def login(request):
    return render(request, "login.html")


"""def checklogin(request):
    uname = request.POST["uname"]
    pwd = request.POST["password"]

    flag = SignUp.objects.filter(Q(username=uname) & Q(password=pwd))
    print(flag)

    if flag:
        user = SignUp.objects.get(username=uname)
        print(user)
        print(user.id, user.fullname, user.gender)  # other fields also
        request.session["uname"] = user.username
        return render(request, "admin.html", {"uname": user.username})
    else:
        msg = "Login Failed"
        return render(request, "login.html", {"msg": msg})"""


def admin(request):

    return render(request,"admin.html")

def manager(request):

    return render(request,"manager.html")

def logout(request):
    return render(request,"login.html")
def adres(request):
    form = RestaurantsForm()
    if request.method == "POST":
        formdata = RestaurantsForm(request.POST,request.FILES)
        if formdata.is_valid():
            formdata.save()
            msg="Product Added Successfully"
            return render(request, "adres.html", {"restaurantsform": form,"msg":msg})
        else:
            msg = "Failed to Add Product"
            return render(request, "adres.html", {"restaurantsform": form, "msg": msg})
    return render(request,"adres.html",{"restaurantsform":form})

def addma(request):
    form = ManagerForm()
    if request.method == "POST":
        formdata = ManagerForm(request.POST)
        if formdata.is_valid():
            formdata.save()
            msg="Employee Registered Successfully"
            return render(request, "addma.html", {"managerform": form,"msg":msg})
        else:
            msg = "Failed to Register Employee"
            return render(request, "addma.html", {"managerform": form, "msg": msg})
    return render(request,"addma.html",{"managerform":form})

def viewcus(request):
    username = request.session["username"]
    cuslist = SignUp.objects.all()
    count = SignUp.objects.count()
    return render(request, "viewcus.html", {"username": username, "cuslist": cuslist, "count": count})

def makereservation(request):
    return render(request,"makereservation.html")

def restaurant(request):
    return render(request,"restaurant.html")


def chefdetails(request):
    return render(request,"chefdetails.html")

def fooditems(request):
    return render(request,"fooditems.html")

def orderdetails(request):
    return render(request,"orderdetails.html")


def viewres(request):

    username=request.session["username"]
    restaurantslist = Restaurants.objects.all()
    count = Restaurants.objects.count()
    return render(request,"viewres.html",{ "username": username,"restaurantslist":restaurantslist,"count": count})

def cus(request):
    return render(request,"cus.html")
def cart(request):
    return render(request,"cart.html")
def checkout(request):
    return render(request,"checkout.html")


def deleteman(request,mid):
    Manager.objects.filter(id=mid).delete()
    return redirect("viewma.html")

def deletecust(request,cid):
    SignUp.objects.filter(id=cid).delete()
    return redirect("viewcus.html")


def deleterest(request,rid):
    Restaurants.objects.filter(id=rid).delete()
    return redirect("viewres.html")


"""def checklogin(request):
        username = request.POST["username"]
        password = request.POST["password"]

        flag = SignUp.objects.filter(Q(username=username) & Q(password=password))
        print(flag)

        if flag:
            user = SignUp.objects.get(username=username)
            print(user)
            print(user.id, user.username, user.gender)  # other fields also
            request.session["username"] = user.username
            return render(request, "cus.html", {"username": user.username})
        elif flag:
            admin = Admin.objects.get(username=username)
            print(admin)
            request.session["username"] = admin.username
            return render(request, "adminhome.html", {"useruname": admin.username})

        else:
            msg = "Login Failed"
            return render(request, "login.html", {"msg": msg})"""
def checklogin(request):
    username = request.POST["username"]
    password = request.POST["password"]
    users = SignUp.objects.filter(Q(username=username))
    for user in users:
        if user.password == password:
            request.session["username"] = user.username
            if username == "admin" and password == "admin" or username == "yash" and password == "Yash":

                return render(request, "admin.html", {"username": user.username})
            else:
                return render(request, "cus.html", {"username": user.username})
    msg = "Login Failed"
    return render(request, "login.html", {"msg": msg})

def viewma(request):
    managerlist = Manager.objects.all()
    count = Manager.objects.count()
    return render(request,"viewma.html",{"managerlist":managerlist,"count":count})


def setcookies(request):
    response=HttpResponse("COOKIES DEMO")

    response.set_cookie("username","klu") #non persistent
    response.set_cookie("location","vijayawada",max_age=10) #persistent

    return response

def getcookies(request):

    uname=request.COOKIES.get("username")
    loc=request.COOKIES.get("location")

    if uname is not None and loc is not None:
        response=uname+","+loc
    elif uname is not None and loc is None:
        response = uname
    elif loc is not None and uname is None:
        response = loc
    else:
        response="COOKIES NOT FOUND"

    return HttpResponse(response)
