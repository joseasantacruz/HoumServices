from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import JsonResponse
from django.db.models import Count
from .models import Coordinates
from .serializers import CoordinatesSerializers
import datetime
from django.contrib.gis.geos import Point


class Coordinates_APIView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        coordinates = Coordinates.objects.all()
        serializer = CoordinatesSerializers(coordinates, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CoordinatesSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Summary_Coordinates_APIView(APIView):
    # Each Houmer will call api('/coordinates/houmer_id') every time they arrive and leave a property.
    # it is assumed that a Houmer doesn't visit the same property on the same day.
    def get(self, request, pk, format=None, *args, **kwargs):
        today_date = datetime.datetime.now().date()  # + datetime.timedelta(days=-1)
        houmer_id_coordinates = Coordinates.objects.all().filter(houmer_id=pk).filter(created_on__date=today_date)
        coordinates = houmer_id_coordinates.values('lat', 'lon').annotate(count=Count('lat')).values('lat',
                                                                                                     'lon')  # .order_by('created_on')
        for coordinate in coordinates:
            current_coordinates = houmer_id_coordinates.filter(lat=coordinate['lat']).filter(lon=coordinate['lon'])
            max_coordinate = current_coordinates.latest('created_on').created_on
            min_coordinate = current_coordinates.earliest('created_on').created_on
            if max_coordinate == min_coordinate:
                # If the Houmer doesn't call api('/coordinates/houmer_id') when exiting the property, it is assumed that it is still in the property.
                max_coordinate = datetime.datetime.now(datetime.timezone.utc)
            current_duration = (max_coordinate - min_coordinate)
            duration = {"duration": str(current_duration).split('.')[0] + '(HH:MM:SS)'}
            coordinate.update(duration)
        return Response(coordinates)

class Movement_APIView(APIView):
    # Each Houmer will call api('/coordinates/houmer_id') every time they arrive and leave a property.
    # it is assumed that a Houmer doesn't visit the same property on the same day.
    def get(self, request, pk,max_speed, format=None, *args, **kwargs):
        today_date = datetime.datetime.now().date()#+ datetime.timedelta(days=-1)
        coordinates = Coordinates.objects.all().filter(houmer_id=pk).filter(created_on__date = today_date).order_by('created_on')
        last_id=-1
        max_ret=[]
        for coordinate in coordinates:
            if last_id>=0 and coordinate.id !=last_id:
                last_coordinates=coordinates.filter(id=last_id)[0]
                distance=Point(last_coordinates.lat,last_coordinates.lon).distance(Point(coordinate.lat,coordinate.lon))*100
                tiempo=coordinate.created_on-last_coordinates.created_on
                average_speed = distance/(tiempo.total_seconds()/3600)
                if average_speed>max_speed:
                    body={"Origin": str(last_coordinates.lat)+','+str(last_coordinates.lon),"Destination":str(coordinate.lat)+','+str(coordinate.lon),
                          "Distance":str(round(distance, 4))+' km',"Duration":str(tiempo).split('.')[0]+ '(HH:MM:SS)',"Average speed":str(round(average_speed, 2))+' km/h'}
                    max_ret.append(body)
            last_id = coordinates.filter(lat=coordinate.lat).filter(lon=coordinate.lon).latest('created_on').id
        return Response(max_ret)