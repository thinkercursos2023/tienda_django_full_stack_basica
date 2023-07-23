from django.db import models
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
#Modelo de la tabla productos 
class Productos(models.Model):
    id_producto = models.BigIntegerField(primary_key=True) #Este será la llave primaria
    nombre_producto = models.CharField(max_length=50) # Se le incluyó un máximo de letras, para que no ingresen nombres muy largos
    descripcion_producto = models.TextField()
    cantidad_disponible = models.IntegerField()

    # Devuelve el nombre del producto cuando se imprime el objeto
    def __str__(self):
        return self.nombre_producto 

#Modelo de la tabla clientes 
class Clientes(models.Model):
    id_cliente = models.BigIntegerField(primary_key=True)
    nombre_cliente = models.CharField(max_length=50) 
    correo = models.CharField(max_length=50) 

    # Devuelve el nombre del cliente cuando se imprime el objeto
    def __str__(self):
        return self.nombre_cliente

class Ventas(models.Model):
    id_venta = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    cantidad_vendida = models.IntegerField()
    precio_venta = models.IntegerField()
    total_venta = models.IntegerField(editable=False)
    id_cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)

    def clean(self):
        # Validar que la cantidad vendida no sea mayor que el stock disponible
        if self.cantidad_vendida > self.id_producto.cantidad_disponible:
            raise ValidationError("La cantidad vendida no puede ser mayor al disponible.")
        # Calcular el total_venta antes de guardar
        self.total_venta = self.cantidad_vendida * self.precio_venta

    def save(self, *args, **kwargs):
        # Sobrescribir el método save para realizar el cálculo antes de guardar
        self.clean()
        super().save(*args, **kwargs)

# Método para actualizar la cantidad_disponible después de guardar una venta
@receiver(post_save, sender=Ventas)
def actualizar_cantidad_disponible(sender, instance, **kwargs):
    # Restar la cantidad_vendida al stock disponible del producto
    instance.id_producto.cantidad_disponible -= instance.cantidad_vendida
    instance.id_producto.save()