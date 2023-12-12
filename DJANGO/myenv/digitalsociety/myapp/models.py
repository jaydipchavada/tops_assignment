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

    def __str__(self):
        return self.email

class chairman(models.Model):
    user_id = models.ForeignKey(user,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    contect_no = models.CharField(max_length=30)
    pic = models.FileField(upload_to="media/images",default="media/JAYDIP.jpg ")

    def __str__(self) -> str:
        return self.first_name

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
    pic = models.FileField(upload_to="media/images",default="media/JAYDIP.jpg ")

    def __str__(self) -> str:
        return self.first_name

class Notice (models.Model):
    notice_title = models.CharField(max_length=50)
    notice_description = models.TextField()
    pic = models.FileField(upload_to="media/images",null=True,blank=True)
    video = models.FileField(upload_to="media/video",null=True,blank=True)

class events (models.Model):
    event_title = models.CharField(max_length=50)
    event_description = models.TextField()
    pic = models.FileField(upload_to="media/images",null=True,blank=True)
    video = models.FileField(upload_to="media/video",null=True,blank=True)