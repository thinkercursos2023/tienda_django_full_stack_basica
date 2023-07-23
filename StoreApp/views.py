from django.shortcuts import render, get_object_or_404, redirect
from .models import Productos, Clientes,Ventas #importamos el modelo Productos
from .forms import ProductoForm, ClientesForm, VentasForm # Importa el formulario para crear un producto, cliente

#Aquí definimos la función de vista llamada vista_productos
def vista_productos(request):
    productos_get_list = Productos.objects.all() #Creamos una instancia de ese modelo productos y lo convertimos en un objete, con todos los datos que tiene dentro
    return render(request, 'pagina_productos.html',{'productos':productos_get_list})

 #Retornamos de manera renderizada la página productos, cabe recalcar que Django sabe la ubicación de estos archivos que estén en la carpeta templates

# Vista para crear un nuevo producto
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/productos/')  # Redirige a la vista de productos después de guardar el nuevo producto
    else:
        form = ProductoForm()
    return render(request, 'crear_producto.html', {'form': form})

# Vista para editar un producto
def editar_producto(request, id_producto):
    producto = get_object_or_404(Productos, id_producto=id_producto)

    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('/productos/')
    else:
        form = ProductoForm(instance=producto)

    return render(request, 'editar_producto.html', {'form': form})

# Vista para eliminar un producto
def eliminar_producto(request, id_producto):
    producto = get_object_or_404(Productos, id_producto=id_producto)

    if request.method == 'POST':
        producto.delete()
        return redirect('/productos/')

    return render(request, 'eliminar_producto.html', {'producto': producto})


#Vista clientes
def vista_clientes(request):
    clientes_get_list = Clientes.objects.all()
    return render(request, 'pagina_clientes.html', {'clientes':clientes_get_list})

# Vista para crear un nuevo cliente
def crear_cliente(request):
    if request.method == 'POST':
        form = ClientesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/clientes/')  # Redirige a la vista de clientes después de guardar el nuevo cliente
    else:
        form = ClientesForm()
    return render(request, 'crear_cliente.html', {'form': form})

# Vista para editar un cliente
def editar_cliente(request, id_cliente):
    cliente = get_object_or_404(Clientes, id_cliente=id_cliente)

    if request.method == 'POST':
        form = ClientesForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('/clientes/')
    else:
        form = ClientesForm(instance=cliente)

    return render(request, 'editar_cliente.html', {'form': form})

# Vista para eliminar un cliente
def eliminar_cliente(request, id_cliente):
    cliente = get_object_or_404(Clientes, id_cliente=id_cliente)

    if request.method == 'POST':
        cliente.delete()
        return redirect('/clientes/')

    return render(request, 'eliminar_cliente.html', {'cliente': cliente})

#Vista Ventas
def vista_ventas(request):
    ventas_get_list = Ventas.objects.all()
    return render(request, 'pagina_ventas.html', {'ventas':ventas_get_list})


# Vista para crear una nueva venta
def crear_venta(request):
    if request.method == 'POST':
        form = VentasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/ventas/')  # Redirige a la vista de clientes después de guardar el nuevo cliente
    else:
        form = VentasForm()
    return render(request, 'crear_venta.html', {'form': form})
    
# Vista para editar una venta
def editar_venta(request, id_venta):
    venta = get_object_or_404(Ventas, id_venta=id_venta)

    if request.method == 'POST':
        form = VentasForm(request.POST, instance=venta)
        if form.is_valid():
            form.save()
            return redirect('/ventas/')
    else:
        form = VentasForm(instance=venta)

    return render(request, 'editar_venta.html', {'form': form})

# Vista para eliminar una venta
def eliminar_venta(request, id_venta):
    venta = get_object_or_404(Ventas, id_venta=id_venta)

    if request.method == 'POST':
        venta.delete()
        return redirect('/ventas/')

    return render(request, 'eliminar_venta.html', {'venta': venta})

