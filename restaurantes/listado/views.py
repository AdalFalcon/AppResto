import requests
from .models import Restaurant
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from .serializers import RestaurantSerializer
from django.db.models import Q 


# Create your views here.

## Agregar URL de la API DENUE

url = "https://www.inegi.org.mx/app/api/denue/v1/consulta/Buscar/restaurantes/19.432608,-99.133209/1000/727413f4-98da-c80a-7a78-b080cc7d0e4c"

@api_view(['GET'])
def fetch_and_save_restaurants(request):    ###  view to obtain data from DENUE API and save it in DB// Vista para obtener datos de API DENUE y guardarlos en la base de datos
    
    # Make GET solicitude // Hacer solicitud GET    
    response = requests.get(url)   

# if response is succesfull (200 OK), to data process  // si la respuesta es satisfatoria (200 OK) para procesar datos

    if response.status_code == 200:
        data = response.json() # convert data to JSCON format  // Convierte los datos a Formato JSON        
        
        for item in data:
            #  Create new instance from Restaurant with obtanided data // Crear una nueva instancia de restaurante con los datos obtenidos 
            restaurant, created = Restaurant.objects.get_or_create(
                id_restaurant=item.get('Id'),
                defaults={
                    'name': item.get('Nombre'),
                    'Razon_social': item.get('Razon_social'),
                    'class_activity': item.get('Clase_actividad'),
                    'estratum': item.get('Estrato'),
                    'street': item.get('Calle'),
                    'num_exterior': item.get('Num_Exterior'),
                    'num_interior': item.get('Num_Interior'),
                    'colony': item.get('Colonia'),
                    'postal_code': item.get('CP'),
                    'location': f"{item.get('Municipio')}, {item.get('Estado')}",
                    'phone': item.get('Telefono'),
                    'email': item.get('Correo_e'),
                    'website': item.get('Sitio_internet'),
                    'longitude': item.get('Longitud'),
                    'latitude': item.get('Latitud'),
                    'service_type': item.get('Tipo')
                }
            )
            if created:
                print(f"Restaurant {restaurant.name} created successfully!")
        return Response({"status": "Data saved successfully"})
    else:
        return Response ({"error": f"Error en la solicitud: {response.status_code}"})
    
    
@api_view(['GET'])
def search_restaurants(request):
    
    ### Endpoit to find restaurants in DB // Endpoint para buscar restaurantes en la BD
    
    query = request.GET.get('q', '') # obtain parameter 'q' from  URL // Obtener el parametro de busqueda 'q' de la URL
    
    if query:
        # Results filter  // Filtrado de resultados
        restaurants = Restaurant.objects.filter(
            Q(name__icontains=query) |
            Q(class_activity__icontains=query) |
            Q(Razon_social__icontains=query)            
        )
        
        # Serialización de los resultados
        
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data)
    else:
        return Response({"message": "No hay conincidecias. ¿Algún otro antojo?"}, status= 400)