from django.urls import path, include #add this to use path
from django.contrib.auth.views import LoginView #using the default django view to login a user
from django.views.generic.base import TemplateView 
from . import views                             #couldn't find one for signup otherwise i wouldn't have created a view

urlpatterns = [
    path('list', views.memberList, name="list"),
    path('signup', views.signup, name='signup'),
    # name is the alias of the url defined through path
    path('accounts/',include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'), #trailing comma is important as 
    #                                                                       adding a url at any postion would be the same
    #                                                                       end or middle

]
#you have to include the path of this file in main urls.py
