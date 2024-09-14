from django.urls import path
from . import views

app_name = 'reports'

urlpatterns = [
    path('',views.index_view,name='home-view'),

    #user list
    path('users',views.UsersView.as_view(),name='user-view'),
    path('users/<int:pk>',views.UserDetailView.as_view(),name='user-detail'),
]