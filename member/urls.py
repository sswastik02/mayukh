from django.urls import path #add this to use path
from . import views

urlpatterns = [
    path('list', views.memberList, name="list"),
    path('signup', views.signup, name='signup'),
    # name is the alias of the url defined through path
]

#you have to include the path of this file in main urls.py