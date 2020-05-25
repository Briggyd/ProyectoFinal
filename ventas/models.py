from django.db import models

# Create your models here.
class Venta(models.Model):
    nombre = models.CharField(
        max_length=100,
    )
    fechaventa=models.DateField(auto_now=True)
    def __str__(self):
        return '{}'.format(self.nombre)
    
    def save(self):
        self.nombre = self.nombre.upper()
        super(Venta, self).save()
    
    class Meta:
        verbose_name_plural = "Ventas"