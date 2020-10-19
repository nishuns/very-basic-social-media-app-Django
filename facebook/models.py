from django.db import models

# Create your models here.

class profiler(models.Model):
    user_id=models.CharField(max_length=64)
    name=models.CharField(max_length=64)
    email=models.CharField(max_length=254)
    bio=models.CharField(max_length=254,blank=True)
    profile_url=models.CharField(max_length=254,blank=True,default="https://miro.medium.com/proxy/1*VcHVCyRSAOF3V6Ldi0iXOQ.jpeg")
    dob=models.CharField(max_length=64)

    def __str__(self):
        return f"{self.user_id}  {self.name}  {self.dob}"
    