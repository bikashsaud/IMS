from django.db import models
from UserProfile.models import UserProfile
from Agent.models import Agent

# Create your models here.
class Client(models.Model):
    Form_number = models.IntegerField(unique=True)
    Branch_name = models.CharField(max_length=200, null=True, blank=True)
    client_license_code = models.ForeignKey(Agent, on_delete=models.CASCADE,related_name='Client')
    Name = models.CharField(max_length=200, null=True, blank=True)
    Gender_choices = (('Male', 'MALE'), ('Female', 'FEMALE'))
    gender = models.CharField(max_length=20, choices=Gender_choices, default=None)
    photo = models.ImageField(upload_to='uploads/', blank=True, null=True)
    Temporary_Address = models.CharField(max_length=200)
    Permanent_address = models.CharField(max_length=200)
    Contact_number = models.IntegerField()
    Email = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    Nationality = models.CharField(max_length=200)
    Education_level_choices = (('see', 'SEE'), ('Bachelors', 'BACHELORS'), ('Master', 'MASTER'))
    Education_level = models.CharField(max_length=200, choices=Education_level_choices, default=None)
    Citizenship = models.FileField(upload_to='uploads/',
                                   null=True, default="No file uploaded", blank=True)
    Citizenship_number = models.IntegerField(unique=True)
    Company_name = models.CharField(max_length=200)
    Company_location = models.CharField(max_length=200)
    Income_source = models.BigIntegerField()
    Fathers_name = models.CharField(max_length=200)
    Mothers_name = models.CharField(max_length=200)
    Grandfathers_name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE,
                             related_name="clients")

    def __str__(self):
        return self.Name
