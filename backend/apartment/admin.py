from django.contrib import admin
from .models import Apartment, Owner, Room, Tenant
# Register your models here.
admin.site.register(Apartment)
admin.site.register(Owner)
admin.site.register(Room)
admin.site.register(Tenant)