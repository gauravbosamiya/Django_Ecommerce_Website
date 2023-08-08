from django.db import models

# Create your models here.
class Category(models.Model):
    category_img = models.ImageField(upload_to='uploads/products/',default="")
    name = models.CharField(max_length=200) 
   
    def __str__(self):
        return self.name
    

class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    name = models.CharField(max_length=200)
    original_price = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=500)
    image = models.ImageField(upload_to='uploads/products/')
    pub_date = models.DateField()
    
    def __str__(self):
        return self.name
    
class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    amount = models.IntegerField(default=0)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Register(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    password = models.CharField(max_length=500)
    con_password = models.CharField(max_length=500)
    
    def __str__(self):
        return self.username
    
    
class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70,default="")
    phone = models.CharField(max_length=10,default="")
    desc = models.CharField(max_length=500,default="")
    
    def __str__(self):
        return self.name
    