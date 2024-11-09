from rest_framework import serializers
from .models import Restaurant

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = [
            'id_restaurant', 'name', 'Razon_social', 'class_activity', 'estratum', 'street',
            'num_exterior', 'num_interior', 'colony', 'postal_code', 'location', 'phone', 
            'email', 'website', 'longitude', 'latitude ', 'service_type'
        ]