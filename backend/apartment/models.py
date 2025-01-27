from django.db import models

# Create your models here.
class Apartment(models.Model):
    address = models.CharField(max_length = 255)
    rent = models.DecimalField(max_digits=10, decimal_places=2)
    available_from = models.DateField()
    owner = models.ForeignKey('Owner', related_name='apartments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Apartment at {self.address}"
    
    
    
    
class Owner(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
