from django.db import models

class Sede(models.Model):
    nombre = models.CharField(max_length=100)           # 1. CharField
    cantidad_canchas = models.IntegerField(default=1)    # 2. IntegerField
    fecha_registro = models.DateTimeField(auto_now_add=True) # 3. DateTimeField
    esta_activa = models.BooleanField(default=True)       # 4. BooleanField

    def __str__(self):
        return self.nombre