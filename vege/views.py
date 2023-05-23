from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="/login/")
def receipe(request):
    if request.method == "POST":

        data = request.POST
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')

        Receipe.objects.create(
            receipe_image=receipe_image,
            receipe_name=receipe_name,
            receipe_description=receipe_description,
        )

        return redirect('/receipe/')

    queryset = Receipe.objects.all()
    context = {'receipe': queryset}
    return render(request, 'receipe.html', context)

@login_required(login_url="/login/")
def update_receipe(request, id):

    queryset = Receipe.objects.get(id=id)
    context = {'receipe': queryset}

    if request.method == 'POST':
        data = request.POST

        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')

        queryset.receipe_name = receipe_name
        queryset.receipe_description = receipe_description

        if receipe_image:
            queryset.receipe_image = receipe_image

        queryset.save()
        return redirect('/receipe/')

    return render(request, 'update_receipe.html', context)

@login_required(login_url="/login/")
def delete_receipe(request, id):

    queryset = Receipe.objects.get(id=id)
    queryset.delete()

    # return HttpResponse("a")
    return redirect('/receipe/')

@login_required(login_url="/login/")
def Update_receipe(request, id):

    queryset = Receipe.objects.get(id=id)
    queryset.Update()

    # return HttpResponse("a")
    return redirect('/receipe/')


def login_page(request):
        if request.method == "POST":
          username = request.POST.get('username')
          password = request.POST.get('password')

          if not User.objects.filter(username = username).exists():
            messages.error(request, "Invaild username")
            return redirect('/login/')
          
          user = authenticate(username = username, password = password)

          if user is None:
              messages.error(request, 'Invaild Password')
              return redirect('/login/')

          else:
              login(request, user)
              return redirect('/receipe/')




        return render(request, 'login.html')


def logout_page(request):
    logout(request)
    return redirect('/login/')



def register(request):

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username = username)

        if user.exists():
            messages.error(request, "Username already taken")
            return redirect('/register/')

        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
        )

        user.set_password(password)
        user.save()

        messages.info(request, "Account Created Successfully ")

        return redirect("/register/")

    return render(request, 'register.html')
