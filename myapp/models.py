
from email.policy import default
# from nis import match
from django.db import models



class Information(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    phonenum = models.CharField(max_length=70, default="")
    # aadharno = models.CharField(max_length=70, default="")
    # gender = models.CharField(max_length=70, default="")
    # fathername = models.CharField(max_length=500, default="")
    match = models.BooleanField(default=False)
    


    def __str__(self):
        return self.name