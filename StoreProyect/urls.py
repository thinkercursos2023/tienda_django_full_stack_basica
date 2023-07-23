from django.contrib import admin
from django.urls import path
from StoreApp.views import (vista_productos, vista_clientes, vista_ventas,
                            crear_producto, crear_cliente, crear_venta,
                            editar_producto, eliminar_producto,editar_cliente, eliminar_cliente,editar_venta,eliminar_venta)

urlpatterns = [
    path('', vista_productos),
    path('productos/', vista_productos),
    path('crear_producto/', crear_producto),
    # Ajustamos la ruta para capturar el valor del id_producto en la URL
    path('editar_producto/<int:id_producto>/', editar_producto),
    path('eliminar_producto/<int:id_producto>/', eliminar_producto),
    path('clientes/', vista_clientes),
    path('crear_cliente/', crear_cliente),
    path('editar_cliente/<int:id_cliente>/', editar_cliente),
    path('eliminar_cliente/<int:id_cliente>/', eliminar_cliente),
    path('ventas/', vista_ventas),
    path('crear_venta/', crear_venta),
    path('editar_venta/<int:id_venta>/', editar_venta),
    path('eliminar_venta/<int:id_venta>/', eliminar_venta),
    path('admin/', admin.site.urls),
]
