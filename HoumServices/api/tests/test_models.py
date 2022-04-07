from django.test import TestCase
from api.models import Coordinates


class CoordinatesModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Coordinates.objects.create(houmer_id=1, lat=-25.2562891, lon=-57.5820576)

    def test_houmer_id(self):
        coordinates = Coordinates.objects.get(id=1)
        field_label = coordinates._meta.get_field('houmer_id').verbose_name
        self.assertEquals(field_label, 'houmer id')
        self.assertEquals(coordinates.houmer_id, 1)

    def test_lat(self):
        coordinates = Coordinates.objects.get(id=1)
        field_label = coordinates._meta.get_field('lat').verbose_name
        self.assertEquals(field_label, 'lat')
        self.assertEquals(coordinates.lat, -25.2562891)

    def test_lon(self):
        coordinates = Coordinates.objects.get(id=1)
        field_label = coordinates._meta.get_field('lon').verbose_name
        self.assertEquals(field_label, 'lon')
        self.assertEquals(coordinates.lon, -57.5820576)