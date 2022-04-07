from django.test import TestCase
from api.models import Coordinates
from api.serializers import CoordinatesSerializers
import time


class Coordinates_APIViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        for num in range(10):
            Coordinates.objects.create(houmer_id=1, lat=num+0.2562891, lon=num+0.5820576)
            time.sleep(0.1)
            Coordinates.objects.create(houmer_id=1, lat=num+0.2562891, lon=num+0.5820576)

    def test_view_get_coordinates(self):
        coordinates = Coordinates.objects.all()
        resp = self.client.get('/coordinates')
        serializer = CoordinatesSerializers(coordinates, many=True)
        self.assertEqual(resp.status_code, 200)
        self.assertEquals(coordinates.count(), 20)
        self.assertEquals(serializer.data,resp.data)

    def test_view_get_summary_coordinates(self):
        resp = self.client.get('/coordinates/1')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.json()), 10)

    def test_view_get_speed_limit(self):
        resp = self.client.get('/movements/1/80')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.json()), 9)