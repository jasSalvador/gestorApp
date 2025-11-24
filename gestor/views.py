from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Integrante, Organizacion


#home
def home(request):
    return render(request, 'home.html')

#inicio
@login_required 
def inicio(request):
    return render(request, 'inicio.html')

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
def registro_org_view(request):
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
    
    return render(request, 'registro.html')


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
    return render(request, 'registro.html', {'organzaciones': organizaciones})



