from django.contrib import admin
from .models import Productos, Clientes,Ventas

# Modelos de productos
@admin.register(Productos)# Se registra el modelo a la vista administrativa
class Productos(admin.ModelAdmin):#el modelo se puede manejar como una clase 
    list_display = ["id_producto", "nombre_producto", "descripcion_producto", "cantidad_disponible"] #Esta opción de list_display nos permite que en la vista administrativa se pueda ver en columnas
    search_fields = ["id_producto","nombre_producto"] #Con esta opción podemos ver desde el panel administrativo un area de busqueda por id y por nombre

# Modelos de clientes
@admin.register(Clientes)
class Clientes(admin.ModelAdmin):
    list_display = ["id_cliente", "nombre_cliente", "correo"] 
    search_fields = ["id_cliente","nombre_cliente"] 

# Modelos de ventas
@admin.register(Ventas)
class Ventas(admin.ModelAdmin):
    list_display = ["id_venta", "id_producto", "cantidad_vendida", "precio_venta", "total_venta", "id_cliente"] 
    search_fields = ["id_venta","id_producto", "id_cliente"] 

