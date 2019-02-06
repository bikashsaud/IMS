from django.db import models
from UserProfile.models import UserProfile
# Create your models here.

class Agent(models.Model):
        License_code = models.IntegerField(unique=True)
        Name = models.CharField(max_length=200, null=True, blank=True)
        Gender_choices = (('Male', 'MALE'), ('Female', 'FEMALE'))  # value ma agadi ko jancha paxi ko dispaly ma janxa
        gender = models.CharField(max_length=20, choices=Gender_choices, default=None)
        photo = models.ImageField(upload_to='uploads/', blank=True, null=True)
        Temporary_Address = models.CharField(max_length=200)
        Permanent_address = models.CharField(max_length=200)
        # Birth_place=models.CharField(max_length=200)
        Contact_number = models.IntegerField()
        Email = models.EmailField(max_length=200, unique=True)
        password = models.CharField(max_length=200)
        Nationality = models.CharField(max_length=200)
        Education_level_choices = (('see', 'SEE'), ('Bachelors', 'BACHELORS'), ('Master', 'MASTER'))
        Education_level = models.CharField(max_length=200, choices=Education_level_choices, default=None)
        Citizenship = models.FileField(upload_to='uploads/',
                                       null=True, default="No file uploaded", blank=True)
        Citizenship_number = models.IntegerField(unique=True)
        Fathers_name = models.CharField(max_length=200)
        Mothers_name = models.CharField(max_length=200)
        Grandfathers_name = models.CharField(max_length=200)
        Name_of_institution = models.CharField(max_length=200, blank=True)
        Date_of_training = models.DateTimeField()
        location = models.CharField(blank=True, max_length=200)
        Bank_ac_no = models.IntegerField(max_length=None)
        Bank_branch_name = models.CharField(max_length=200)
        is_active = models.BooleanField(default=True)

        user = models.ForeignKey(UserProfile, on_delete=models.CASCADE,
                                 related_name="agents")

        def __str__(self):
            return self.Name
