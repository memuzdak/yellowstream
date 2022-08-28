from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .models import *
from django.contrib import messages
from django.contrib.sessions.models import Session


def index(request):
    if request.session.has_key('session_login'):
        return render(request, 'home/index.html')
    return redirect('login')

def login(request):
    if request.session.has_key('session_login'):
        return render(request, 'home/index.html')
    if request.POST:
        email = request.POST['email']
        password = request.POST['password']
        count = User.objects.filter(email=email, password=password).count()
        if count>0:
            request.session['session_login'] = True
            return redirect('home')
        else:
            messages.error(request,"Invalid email or password")
            return redirect("login")
    return render(request,'entry/login.html')


def logout(request):
    # if request.session.has_key('session_login'):
    #     return render(request, 'home/index.html')

    del request.session['session_login']
    return redirect('login')


def signup(request):
    return render(request, 'entry/signup.html')


def user_register(request):
    if request.POST:
        username = request.POST['form_username']
        email = request.POST['form_email']
        password = request.POST['form_password']

        obj_user = User(username = username, password=password, email =email)
        obj_user.save()
        messages.success(request, "You have created account successfully")
        return redirect("login")


def expenseclaim(request):
    if request.session.has_key('session_login'):
        # return render(request, 'home/index.html')
        return render(request,'home/formexpense.html')
    return redirect("login")


def onClick_formExpense(request):
    if request.POST:
        name = request.POST['form_name']
        description = request.POST['form_description']
        amount = request.POST['form_amount']
        file = request.POST['form_file']
        obj_expense_form_user = Expense(name=name, description =description, amount=amount, file =file)
        obj_expense_form_user.save()
        messages.success(request, "Expense submitted Successfully.")
        return redirect('expenseclaim')


