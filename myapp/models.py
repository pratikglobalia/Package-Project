from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Package(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    total_activity = models.IntegerField()

    def __str__(self):
        return self.name
    

class PurchasePackage(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

        
class Activity(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)

    def __str__(self):
        return self.name