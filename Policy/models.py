from django.db import models
# Create your models here.
from Client.models import Client

class Policy(models.Model):
    policy_id=models.IntegerField(unique=True)
    policy_name=models.CharField(max_length=300,blank=False,null=False)
    description=models.TextField()
    policy_type=models.CharField(max_length=200)
    policy_period=models.DateTimeField()

    def __str__(self):
        return self.policy_name
    class Meta:
        verbose_name_plural = "Policies"

class Applied_Policy(models.Model):
    sum_assured=models.BigIntegerField()
    policy_type=models.ForeignKey(Policy,on_delete=models.CASCADE,default=None,related_name='Policy')
    premium_amount=models.BigIntegerField()
    payment_method_choices = (('monthly', 'MONTHLY'), ('semiannual', 'SEMIANNUAL'),('yearly','YEARLY'))
    payment_method = models.CharField(max_length=20, choices=payment_method_choices, default=None)
    # payment_method = models.CharField(max_length=200, choices=(
    # ('Yearly', 'YEARLY'), ('Monthly', 'MONTHLY'), ('Semiannual', 'SEMIANNUAL')))
    next_payment_date=models.DateTimeField()
    policy_id=models.ForeignKey(Policy,on_delete=models.CASCADE,default=None,related_name='appliedname')
    client_id=models.ForeignKey(Client,on_delete=models.CASCADE,default=None,related_name='Client')

    def __str__(self):
        return self.payment_method

    class Meta:
        verbose_name_plural = "Applied_policies"
