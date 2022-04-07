from django.db import models

class Coordinates(models.Model):
    #  'houmer_id' is the identifier of each Houmer and is a numeric field.
    houmer_id = models.IntegerField(blank=False, null=False)
    lat = models.FloatField(blank=False, null=False)
    lon = models.FloatField(blank=False, null=False)
    created_on = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Creado el')
    last_updated_on = models.DateTimeField(auto_now=True,
                                           verbose_name='Actualizado el')