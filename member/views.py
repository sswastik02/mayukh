from django.shortcuts import render, redirect
from .models import member # need to do this
from .forms import SignupForm
from django.contrib.auth.hashers import make_password #this is used for hashing the password field
# Create your views here.

def memberList(request):
    members = member.objects.all()
    return render(request, 'memberList.html', {"members": members})
    # it will take a request, parse the html file(load) 
    #when you will be reffering to members in the html file
    #the dictionary will take care of it

    #after this create a templates folder for adding html file in the
    #app folder

def signup(request): #to make a form to accept this create forms.py
    if request.method == 'POST':
        form= SignupForm(request.POST)
        if form.is_valid() :
            instance=form.save(commit=False) #not commiting to database but saving
            #before saving instance of the form you can alter the fields but not after
            instance.password=make_password(instance.password)
            instance.first_name=instance.first_name[0].upper() + instance.first_name[1:]
            instance.last_name=instance.last_name[0].upper() + instance.last_name[1:]
            instance.mail=instance.mail.lower()
            instance.save()
            return redirect('list') #sends you to the list url
    else:
        form = SignupForm() #empty form if you havent done anything
        #or just visited
    return render(request,'SignupForm.html',{'form':form}) #now make a template for this
