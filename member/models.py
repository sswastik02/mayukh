from django.db import models
from .validators import phone_number_validator, password_len_validator #make this for custom validations
#make the model first
# Create your models here.

post_choices=(
    ("Teacher","Teacher"),
    ("Student","Student")
)
class  member (models.Model):
    #models.Model is actually used in views.py for objects.all() func
    #as it's not defined here
    first_name=models.CharField(max_length=50, help_text="First Name")
    last_name=models.CharField(max_length=50, help_text="Last Name")
    username=models.CharField(max_length=50,unique=True, help_text="Username")
    password=models.CharField(max_length=100,validators=[password_len_validator], help_text="Password")
    post=models.CharField(max_length=50,choices=post_choices,default='Student',verbose_name='Designation')
    mail=models.EmailField(max_length=100, unique=True, verbose_name="E-Mail")
    phone=models.IntegerField(validators=[phone_number_validator], unique=True, help_text="Phone No. (10 digits)")
    current=models.CharField(max_length=50,default="inactive")
    def __str__(self):
        return(self.username)
#then open admin.py to register the models
#also add it to installed apps in settings
#then create a view in views.py (here we will list all the members)
