from email.policy import default
from django.db import models

# Create your models here.



class UserRole(models.Model):
    role = models.CharField(max_length=20)

    class Meta:
        db_table = 'role'

    def __str__(self) -> str:
        return self.role

class Profile(models.Model):
    UserRole = models.ForeignKey(UserRole, on_delete=models.CASCADE)
    profileimage = models.FileField(upload_to='profile_images/', default='default.png')
    email = models.EmailField(unique=True, default="")
    password = models.CharField(max_length=10, default="")
    fullname = models.CharField(max_length=30, default="")
    contact_info = models.CharField(max_length=10, blank=True)
    location = models.CharField(max_length=100, blank=True)
    

    class Meta:
        db_table = 'profile'


    def __str__(self) -> str:
        return self.email





class Product(models.Model):
    Profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=50, default="")
    product_price = models.IntegerField(default=0)
    description = models.TextField(max_length=1000, blank=True)
    product_image = models.FileField(upload_to="product_images/", default="default.png")


    def __str__(self) -> str:
        return self.product_name


