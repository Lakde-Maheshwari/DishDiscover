from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('Username')
        pass1 = request.POST.get('Password')

        user = authenticate(username=username, password=pass1)

        if request.user.is_authenticated:
            current_username = request.user.username
            if current_username != username:
                return render(request,'loginfailed.html')

        if user is not None:
            login(request,user)
            recipes = user.recipes_set.all()
            fname = user.first_name
            context = {
                'user' : user,
                'recipes' : recipes,
                'fname' : fname,
            }
            return render(request,"profile.html",context)
        else:
            messages.error(request,"Bad Credentials")
            return redirect("home")
    return render(request,'login.html')

def register(request):
    if request.method == "POST":
        username = request.POST.get('Username')
        email = request.POST.get('Email')
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('cpass')

        if pass1 != pass2:
            return redirect('passwordinc')

        myuser = User.objects.create_user(username,email,pass1)


        myuser.fname = firstname
        myuser.lname = lastname

        myuser.save()
        return redirect("afterregister")
    
    return render(request,'register.html')


def signout(request):
    logout(request)
    return render(request,'logout.html')


def profile(request,id):
    user = get_object_or_404(User,id=id)
    recipes = user.recipes_set.all()

    context = {
        'user' : user,
        'recipes' : recipes,
    }
    return render(request,"profile.html",context)

def afterregister(request):
    return render(request,'afterRegister.html')


def passwordinc(request):
    return render(request,'passwordinc.html')


def loginfailed(request):
    return render(request,'loginfailed.html')
