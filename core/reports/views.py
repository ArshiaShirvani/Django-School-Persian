from django.shortcuts import render
from django.views.generic import ListView,TemplateView,DetailView
from accounts.models import Profile

"""show main page of admin panel"""
def index_view(request):
    return render (request,'admin-panel/index.html')


"""retrieved data on User profile and show their data"""
class UsersView(TemplateView):
    template_name = 'admin-panel/users.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = Profile.objects.all()
        return context

"""retrieved user data and show on the template"""
class UserDetailView(DetailView):

    model = Profile

    template_name = 'admin-panel/user-detail.html'
    context_object_name = 'user'


