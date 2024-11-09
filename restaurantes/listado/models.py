from django.db import models

# Create your models here.

class Restaurant(models.Model):
         
    id_restaurant = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length= 255)
    Razon_social = models.CharField(max_length=255, null=True, blank=True)
    class_activity = models.CharField(max_length=255) # KIND OF ECONOMIC ACTIVIT / TIPO DE ACTIVIDAD ECONOMICA
    estratum = models.CharField(max_length=50) # Bussiness size / Tamaño del negocio
    street = models.CharField(max_length=255)
    num_exterior = models.CharField(max_length=255, null=True, blank=True)
    num_interior = models.CharField(max_length=255, null=True, blank=True)
    colony = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=10)
    location = models.CharField(max_length=255) # General Location (state, municipe) / Ubicación general (alcaldía, ciudad)
    phone = models.CharField(max_length=20, null=True, blank=True) 
    email = models.EmailField(null=True, blank=True)
    website = models.URLField(null=True, blank=True) 
    longitude = models.FloatField()
    latitude = models.FloatField()
    service_type = models.CharField(max_length=50) # Kind of service (static, ambulant, etc) / Tipo (fijo, ambulante, etc.)
    
    def __str__(self):
        return self.name
   