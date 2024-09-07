from django.forms import BaseModelForm
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.views import LoginView
from django.views.generic import DetailView
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse_lazy,reverse
from .models import Profile,User
from django.views.generic.edit import CreateView,FormView
from .forms import UserRegisterForm

def login_view(request):
    if not request.user.is_authenticated:
          if request.method=='POST':
               username=request.POST['username']
               password=request.POST['password']
               user = authenticate(request,username=username, password=password)
               if user is not None:
                    login(request,user)
                    # return HttpResponseRedirect(reverse('accounts:profile-view', kwargs={"pk": user.national_code}))
                    return HttpResponseRedirect(reverse('accounts:profile-view'))
                    
          return render(request,'accounts/login.html')
    else:
        return redirect('/accounts/profile')
        
    
def user_profile(request):
    if request.user.is_authenticated:
        user = get_object_or_404(Profile,pk=request.user.id)
        context = {'user':user}
        return render(request,'accounts/profile.html',context)
    
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/accounts/login')
    else:
        return redirect('/accounts/profile')
    
def complete_profile(request):
    return render(request,'accounts/complete-register.html')

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