from django.db import models

# Create your models here.


class Sales(models.Model):
    product = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    price = models.IntegerField()
    mobilenum = models.CharField(max_length=10, default='')

    def __str__(self) -> str:
        return f"{self.product} owner name:{self.name} and Rs.{self.price}"
    

class Service(models.Model):    
    oname = models.CharField(max_length=50)
    address = models.TextField(max_length=100)
    phnum = models.CharField(max_length=10)
    district = models.CharField(max_length=50)
    pin = models.CharField(max_length=6)
    
    pname = models.CharField(max_length=50)
    mname = models.CharField(max_length=50)
    defect = models.TextField(max_length=500)


   
    