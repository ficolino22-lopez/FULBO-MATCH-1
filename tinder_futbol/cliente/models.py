from django.db import models


class Partido(models.Model):
    titulo = models.CharField(max_length=100)           # 1. CharField
    jugadores_faltantes = models.IntegerField(default=1) # 2. IntegerField
    fecha_partido = models.DateTimeField()             # 3. DateTimeField
    es_mixto = models.BooleanField(default=True)         # 4. BooleanField

    def __str__(self):
        return self.titulo