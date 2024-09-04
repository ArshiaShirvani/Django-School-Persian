from django.urls import path,include
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login',views.login_view,name='login-view'),
    path('profile',views.user_profile,name='profile-view'),
    # path('login',views.UserRegisterView.as_view(),name='login-view'),
    # path('login',views.UserCompleteRegisterView.as_view(),name='login-view'),
    # path('login',views.UserForgetPasswordView.as_view(),name='login-view'),
]