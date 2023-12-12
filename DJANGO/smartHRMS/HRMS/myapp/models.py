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
        HR                  Emplopyess
"""

class user(models.Model):
    email = models.EmailField(unique=True,max_length=30)
    password = models.CharField(max_length=30)
    role = models.CharField(max_length=30)

    def __str__(self):
        return self.email

class HR(models.Model):
    user_id = models.ForeignKey(user,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    contect_no = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.first_name

class Emplopyess (models.Model):
    user_id = models.ForeignKey(user,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    contect_no = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    email = models.EmailField(max_length=30)
    birth_date = models.CharField(max_length=30)
    special_intereste = models.CharField(max_length=30)
    Education = models.CharField(max_length=30)
    
    
