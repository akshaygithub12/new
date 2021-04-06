from django.db import models

# Create your models here.


class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    category=models.CharField(max_length=50,default="")
    category=models.CharField(max_length=50,default="")
    sub_cat=models.CharField(max_length=50,default="")
    desc = models.CharField(max_length=1000)
    pub_date=models.DateField()
    pro_img=models.ImageField(upload_to='shop/images',default="")
    price=models.IntegerField(default=0)

    def __str__(self):
        return self.product_name


class Contact(models.Model):
    
    name=models.CharField(max_length=30,default="")
    email=models.EmailField(max_length=50,default="")
    phone=models.CharField(max_length=40,default="")
    desc=models.CharField(max_length=100,default="")

    def __str__(self):
        return self.name
    



        
