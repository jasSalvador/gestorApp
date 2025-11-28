from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Integrante, Organizacion, Cuota, Gasto, ItemGasto
from .forms import CuotaForm, GastoForm, ItemGastoForm, IntegranteForm
from django.http import HttpResponseForbidden

#home
def home(request):
    return render(request, 'home.html')

#inicio
@login_required 
def inicio(request):
    integrante = Integrante.objects.get(user=request.user)
    organizacion = integrante.organizacion
    return render(request, 'inicio.html', {"organizacion": organizacion, "integrante": integrante})


#login
def login_view(request):
    if request.method == 'POST': #recibiendo la info del form
        username = request.POST['username'] 
        password = request.POST['password']
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
        #inicio sesion
            login(request, usuario) 
            return redirect('inicio')
        else:
            return render(request, 'login.html', {'error': 'Credenciales inválidas'})
    return render(request, 'login.html')


#logout
def logout_view(request): 
    logout(request)  
    return redirect('login')


#registro de administradores
def registro_admin_view(request):
    if request.method == 'POST':
        #datos del administrador
        username = request.POST['username']
        email = request.POST['email']
        direccion = request.POST['useradress']
        telefono = request.POST['userphone']
        dependiente = request.POST['dependiente']        
        password1 = request.POST['password1']
        password2 = request.POST['password2']        

        #datos de la organizacion
        nombre_org = request.POST['nombre_org']        
        tipo_org = request.POST['tipo_org']        

        #validaciones
        if password1 != password2:
            return render(request, 'registro.html', {'error': 'Las contraseñas no coinciden'})
        
        if User.objects.filter(username=username).exists():
            return render(request, 'registro.html', {'error': 'El nombre de usuario ya existe'})
        
        if User.objects.filter(email=email).exists():
            return render(request, 'registro.html', {'error': 'El correo ya existe'})

        try:
            #crear usuario admin
            user = User.objects.create_user(username=username, email=email, password=password1)
            login(request, user) #para iniciar sesion automaticamente

            #crear organizacion
            organizacion = Organizacion.objects.create(nombre=nombre_org, tipo=tipo_org, admin_local=user)

            #registrar al admin como integrant
            Integrante.objects.create(user=user,organizacion= organizacion,direccion=direccion,telefono=telefono,dependiente=dependiente)

            #mensaje registro exitoso en inicio
            messages.success(request, 'Registro exitoso, ya estás dentro!')
            return redirect('inicio')
        except Exception as e:
            messages.error(request, f'Ah ocurrido un error: {str(e)}')
            return render(request, 'registro.html')
    
    return render(request, 'registro_admin.html')


#registro usuarios
def registro_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        direccion = request.POST['useradress']
        telefono = request.POST['userphone']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        #validaciones
        if password1 != password2:
            return render(request, 'registro.html', {'error': 'Las contraseñas no coinciden'})
        
        if User.objects.filter(username=username).exists():
            return render(request, 'registro.html', {'error': 'El nombre de usuario ya existe'})
        
        if User.objects.filter(email=email).exists():
            return render(request, 'registro.html', {'error': 'El correo ya existe'})

        #crear usuario
        try:
            user = User.objects.create_user(username=username, email=email, password=password1)
            login(request, user) #para iniciar sesion automaticamente

            #crear/registrar integrante
            org_id = request.POST['org_id']
            organizacion = Organizacion.objects.get(id=org_id)

            Integrante.objects.create(user=user, organizacion=organizacion, direccion=direccion, telefono=telefono, dependiente=request.POST.get('dependiente', ''))

            #mensaje registro exitoso en inicio
            messages.success(request, 'Registro exitoso, ya estás dentro!')
            return redirect('inicio')
        except Exception as e:
            messages.error(request, f'Ah ocurrido un error: {str(e)}')
            return render(request, 'registro.html')
    
    organizaciones = Organizacion.objects.all()
    return render(request, 'registro.html', {'organizaciones': organizaciones})


#mostrar cuotas pagadas de cada integrante
@login_required 
def cuotas_view(request):
    integrante = Integrante.objects.get(user=request.user)
    cuotas = integrante.cuotas.all()
    organizacion = integrante.organizacion
    integrante = Integrante.objects.filter(organizacion=organizacion)
    return render(request, "cuotas.html", {"organizacion": organizacion, "integrante": integrante, "cuotas": cuotas})



#mostrar integrantes
@login_required 
def integrantes_view(request):
    integrante = get_object_or_404(Integrante, user=request.user)
    organizacion = integrante.organizacion
    #vallidacion admin
    if request.user != integrante.organizacion.admin_local:
        return redirect('inicio')

    integrantes = Integrante.objects.filter(organizacion=organizacion)
    return render(request, "integrantes.html", {"organizacion": organizacion, "integrantes": integrantes})



#form pago cuotas
@login_required 
def pago_cuotas_view(request):
    integrante = get_object_or_404(Integrante, user=request.user)
    #validacion admin
    if request.user != integrante.organizacion.admin_local:
        return redirect('inicio')

    if request.method == 'POST':
        form = CuotaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Pago registrado!')
            return redirect('inicio')
    else:
        form = CuotaForm()

    return render(request, 'pago_cuotas.html', {'form': form})



#form gasto
@login_required 
def registro_gasto_view(request):
    integrante = get_object_or_404(Integrante, user=request.user)
    #vallidacion admin
    if request.user != integrante.organizacion.admin_local:
        return redirect('inicio')

    if request.method == 'POST':
        gasto_form = GastoForm(request.POST)
        if gasto_form.is_valid():
            gasto = gasto_form.save()
            messages.success(request, 'Gasto registrado, ahora puedes agregar items al gasto')
            return redirect('registro_item_gasto', gasto_id=gasto.id)
    else:
        gasto_form = GastoForm()
    
    return render(request, 'registro_gasto.html', {'form': gasto_form})



#form item gasto
@login_required 
def registro_item_gasto_view(request, gasto_id):
    integrante = get_object_or_404(Integrante, user=request.user)
    gasto = get_object_or_404(Gasto, id=gasto_id)
    #validacion admin
    if request.user != integrante.organizacion.admin_local:
        return redirect('inicio')

    if request.method == 'POST':
        item_form = ItemGastoForm(request.POST)    
        if item_form.is_valid():
            item = item_form.save(commit=False)
            item.gasto = gasto
            item.save()
            messages.success(request, 'Item agregado!')
            return redirect('registro_item_gasto', gasto_id=gasto.id)
    else:
        item_form = ItemGastoForm()
    
    return render(request, 'registro_item_gasto.html', {'form': item_form, 'gasto': gasto})



#mostrar lista de gastos
@login_required
def lista_gastos_view(request):
    gastos = Gasto.objects.all()
    return render(request, 'lista_gastos.html', {'gastos': gastos})



#detalles de gasto /items
@login_required
def detalle_gasto_view(request, gasto_id):
    gasto = Gasto.objects.get(id=gasto_id)
    items = gasto.items.all()
    return render(request, 'detalle_gasto.html', {'gasto': gasto, 'items': items})



# eliminacion integrante
@login_required
def eliminar_integrante(request, integrante_id):
    integrante = get_object_or_404(Integrante, id=integrante_id)
    user = integrante.user

    # integrante elimina su propia cuenta
    if integrante.user == request.user:
        integrante.delete()
        user.delete()
        return redirect('logout')

    # admin elimina cualquier integrante q pertenezca a la organizacion
    if request.user.is_staff or request.user.is_superuser:
        integrante.delete()
        user.delete()
        return redirect('lista_integrantes')
    
    return HttpResponseForbidden("No tienes permiso para eliminar esta integrante")



#confirmar eliminacion integrante
@login_required
def confirmar_eliminar_integrante_view(request, integrante_id):
    integrante = get_object_or_404(Integrante, id=integrante_id)

    return render(request, 'confirmar_eliminar_integrante.html', {'integrante': integrante})



# editar integrante
def editar_integrante_view(request):
    integrante = get_object_or_404(Integrante, user=request.user)
    if request.method == 'POST':
        form = IntegranteForm(request.POST, instance=integrante)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = IntegranteForm(instance=integrante)
    return render(request, 'editar_integrante.html', {'form': form})



#mostrar todas las cuotas pagadas
@login_required
def lista_cuotas_view(request):
    integrante = Integrante.objects.get(user=request.user)
    if request.user != integrante.organizacion.admin_local:
        return redirect('inicio')
    cuotas = Cuota.objects.filter(integrante__organizacion=integrante.organizacion)
    return render(request, "lista_cuotas.html", {"cuotas": cuotas})





