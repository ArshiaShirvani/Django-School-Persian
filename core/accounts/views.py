from django.forms import BaseModelForm
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.views import LoginView
from django.views.generic import DetailView
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse_lazy,reverse
from django.views.generic.edit import CreateView,FormView

from .models import Profile,User,UserManager
from .forms import UserRegisterForm

def login_view(request):
    if not request.user.is_authenticated:
            if request.method=='POST':
                username_received=request.POST['national_code']
                password_received=request.POST['password']
                # user = User.objects.get(national_code=username,password = password_sent)
                # if user is not None:
                #     login(request,user)
                #     # return HttpResponseRedirect(reverse('accounts:profile-view', kwargs={"pk": user.national_code}))
                #     # return HttpResponseRedirect(reverse('accounts:profile-view'))
                #     return redirect ('/accounts/profile')
                user = authenticate(national_code=username_received, password=password_received)
                if user is not None:
                    login(request, user)
                    if user.is_superuser == True:
                        return redirect('/panel/users')
                    else:
                        return redirect ('/accounts/profile')
                    
            return render(request,'accounts/login.html')
    else:
        user_id = request.user.id
        user = User.objects.get(id = user_id)
        if user.is_superuser == True:
            return redirect('/panel/users')
        else:
            return redirect('/accounts/profile')
        
    
def user_profile(request):
    if request.user.is_authenticated:
        user = get_object_or_404(Profile,pk=request.user.id)
        context = {'user':user}
        return render(request,'accounts/profile.html',context)
    else:
        return redirect('/accounts/login/')
    
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/accounts/login/')
    else:
        return redirect('/accounts/login/')
    
def complete_profile(request):
    if request.user.is_authenticated:
        user = get_object_or_404(Profile,user_id=request.user.id)
        if request.method == "POST":
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            phone_number = request.POST['phone_number']
            email = request.POST['email']
            grade = request.POST['grade']
            field_of_study = request.POST['field_of_study']
            user.first_name = first_name
            user.last_name = last_name
            user.phone_number = phone_number
            user.email = email
            user.grade = grade
            user.field_of_study = field_of_study
            user.save()
            return redirect('/accounts/profile')
        else:
            return render(request,'accounts/complete-register.html')
    else:
        return redirect('/accounts/login/')

def register_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                username_sent = request.POST['national_code']
                password_sent = request.POST['password']
                form.save()
                user = User.objects.get(national_code = username_sent,password = password_sent)
                if user is not None:
                    login(request,user)
                    return redirect('/accounts/complete-profile')
        form=UserRegisterForm()
        return render(request,'accounts/register.html')
    else:
        return redirect('/accounts/profile')

def forget_password_view(request):
    pass