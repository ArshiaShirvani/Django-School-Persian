from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.views import LoginView
from django.views.generic import DetailView
from django.contrib.auth import authenticate,login
from django.urls import reverse_lazy,reverse
from .models import Profile,User

def login_view(request):
    if not request.user.is_authenticated:
          if request.method=='POST':
               username=request.POST['username']
               password=request.POST['password']
               user = authenticate(request,username=username, password=password)
               if user is not None:
                    login(request,user)
                    user_id = user.id
                    # return HttpResponseRedirect(reverse('accounts:profile-view', kwargs={"pk": user.national_code}))
                    return HttpResponseRedirect(reverse('accounts:profile-view'))
                    
          return render(request,'accounts/login.html')
    else:
        return redirect('/')
        
    
def user_profile(request):
    if request.user.is_authenticated:
        user = get_object_or_404(Profile,pk=request.user.id)
        context = {'user':user}
        return render(request,'accounts/profile.html',context)
