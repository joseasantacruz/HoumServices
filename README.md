# HoumServices
## Development Enviroment for Houm services


This is just a development envrioment for Houm services project. Please follow the install instructions.

## Problem and requirements
```sh
Problema
En Houm tenemos un gran equipo de Houmers que muestran las propiedades y solucionan todos los problemas que podrían ocurrir en ellas. 
Ellos son parte fundamental de nuestra operación y de la experiencia que tienen nuestros clientes. 
Es por esta razón que queremos incorporar ciertas métricas para monitorear cómo operan, mejorar la calidad de servicio y para asegurar la seguridad de nuestros Houmers.

Requisitos
Crear un servicio REST que:
1. Permita que la aplicación móvil mande las coordenadas del Houmer
2. Para un día retorne todas las coordenadas de las propiedades que visitó y cuanto tiempo se quedó en cada una
3. Para un día retorne todos los momentos en que el houmer se trasladó con una velocidad superior a cierto parámetro
```

## Assumptions
1. In the model 'houmer_id' is the identifier of each Houmer and is a numeric field.
2. Each Houmer will call api('/coordinates/houmer_id') every time they arrive and leave a property.
3. A Houmer doesn't visit the same property on the same day.
4. If the Houmer doesn't call api('/coordinates/houmer_id') when exiting the property, it is assumed that it is still in the property.


## API Enpoints
1. Get all coordinates
```sh
URL: http://localhost:8000/coordinates
METHOD: GET
```
2. Set coorditate
```sh
URL: http://localhost:8000/coordinates
METHOD: POST
BODY: {
        "houmer_id": numeric houmer_id, 
        "lat": numeric latitude,
        "lon": numeric longitude
      }
```
3. Get daily summary
```sh
URL: http://localhost:8000/coordinates/houmer_id
METHOD: GET
```
4. Get speed limit
```sh
URL: http://localhost:8000/movements/houmer_id/limit_speed(km/h)
METHOD: GET
```


## Prerequisites
- python
- pip
- virtualenv


## Install

1. Clone this repo:
```sh
git clone git@github.com:joseasantacruz/HoumServices.git
```

2. Activate the virtual environment:
```sh
cd houmservices
virtualenv venv
source venv/bin/activate
```

3. From the new directory run the requirements install:
```sh
pip install -r requirements.txt
```

4. Execute the query to create user and database:
```sh
database.sql
```

5. Create a superuser for the Django Admin:
```sh
cd HoumServices
python manage.py createsuperuser
```


6. Run the server:
```sh
python manage.py runserver
```

7. Run test:
```sh
python manage.py test
```