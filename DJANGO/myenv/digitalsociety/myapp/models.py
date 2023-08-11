from django.db import models

# Create your models here.
"""
                    user
                     |
                    email
                    password
                    role
                     |
            ----------------------
            |                    |
        chairman                socity member
"""

class user(models.Model):
    email = models.EmailField(unique=True,max_length=30)
    password = models.CharField(max_length=30)
    role = models.CharField(max_length=30)

class chairman(models.Model):
    user_id = models.ForeignKey(user,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    contect_no = models.CharField(max_length=30)

class socity_member(models.Model):
    user_id = models.ForeignKey(user,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    contect_no = models.CharField(max_length=30)
    no_of_familymember = models.CharField(max_length=30)
    house_no = models.CharField(max_length=30)
    vehical_detalis = models.CharField(max_length=30)
    no_of_vehical = models.CharField(max_length=30)
    occupation = models.CharField(max_length=30)
    job_address = models.CharField(max_length=100,blank=True,null=True)