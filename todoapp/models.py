from django.db import models

class usertasks(models.Model):
    
    description=models.CharField(max_length=50)