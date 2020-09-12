from django.db import models

class Login_credentials(models.Model):
    username = models.CharField(max_length=100,null=True,blank=True)
    password = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return  self.username

