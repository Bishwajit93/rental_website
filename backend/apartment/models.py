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


class Room(models.Model):
    apartment = models.ForeignKey(Apartment, related_name='rooms', on_delete=models.CASCADE)
    room_number = models.CharField(max_length=10)
    capacity = models.IntegerField(choices=[(1, '1 person'), (2, '2 persons'), (3, '3 persons')])
    rent = models.DecimalField(max_digits=10, decimal_places=2)
    tenant = models.ForeignKey('Tenant', null=True, blank=True, on_delete=models.SET_NULL, related_name='rooms')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Room {self.room_number} in {self.apartment.address}"




class Tenant(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    room = models.ForeignKey(Room, related_name='tenants', on_delete=models.SET_NULL, null=True)
    rental_start_date = models.DateField()  # Date the rental agreement started
    room_rent = models.DecimalField(max_digits=10, decimal_places=2)  # Rent for the room the tenant is renting
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
