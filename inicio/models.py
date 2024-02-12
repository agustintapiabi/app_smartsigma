from django.db import models


# Crea y Modifica automaticamente Tablas en migrations
class Area(models.Model):
    Name = models.CharField(max_length=200)          
    def __str__(self):    
        return self.Name                             # Se visualiza en el Panel de Administrador

class Proceso(models.Model):
    Name = models.CharField(max_length=200)
    Description = models.TextField()
    Area = models.ForeignKey(Area, on_delete=models.CASCADE)
    def __str__(self):    
        return self.Name + ' - ' + self.Area.Name     
    
class Inventario(models.Model):
    SKU = models.CharField(max_length=200)
    Description = models.TextField()
    Area = models.ForeignKey(Area, on_delete=models.CASCADE)
    def __str__(self):    
        return self.SKU + ' - ' + self.Description + ' - ' + self.Area.Name     

class HistoricoVenta(models.Model):
    SKU = models.CharField(max_length=200)
    Cantidad = models.CharField(max_length=200)
    Precio = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    Fecha = models.DateField(null=True)
    
    class Meta:
        db_table = 'ventas'
    
class InventarioABC(models.Model):
    SKU = models.CharField(max_length=200)
    Familia = models.TextField()
    Cantidad = models.CharField(max_length=200)
    Costo = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    Precio = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    Volumen = models.CharField(max_length=200)
