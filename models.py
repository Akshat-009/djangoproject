from django.db import models

# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=20)
    category=models.CharField(max_length=50,default="")
    subcategory=models.CharField(max_length=50,default="")
    dec= models.CharField(max_length=200)
    pub_date=models.DateField()
    price=models.FloatField(default=0)
    image=models.ImageField(upload_to="shop/images",default="")
    def __str__(self):
        return self.product_name
class Contact(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=122)
    email=models.EmailField(max_length=254)
    query=models.CharField(max_length=500)

def __str__(self):
    return self.email

class Order(models.Model):
    id=models.AutoField(primary_key=True)
    itemjson=models.CharField(max_length=500)
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50) 
    address=models.CharField(max_length=500)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    zipcode=models.IntegerField(max_length=12)    

class Track(models.Model):
    id=models.AutoField(primary_key=True)
    update=models.CharField(max_length=100)