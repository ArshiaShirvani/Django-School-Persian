from django.urls import path,include
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/',views.login_view,name='login-view'),
    path('profile',views.user_profile,name='profile-view'),
    path('logout',views.logout_view,name='logout_view'),
    path('forget-password',views.forget_password_view,name='forget-password-view'),
    path('signup',views.register_view,name='register-view'),
    path('complete-profile',views.complete_profile,name='register-profile'),
]