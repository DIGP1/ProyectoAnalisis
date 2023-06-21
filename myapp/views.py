from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, JsonResponse
from .models import usuarios, datosEjercicio
from .form import formRegistro
from django.contrib import messages



# Create your views here.

def index(request):
    return render(request, 'pagina.html')

def holaMundo(request):
    return HttpResponse("<h2> Hola Mundo </h2>")

def buscar(request):
    usuario = get_object_or_404(usuarios, id=id)
    return HttpResponse('usuario: %s' % usuario.Nomb)

def registrarUsuario(request):
    if request.method == 'POST':
        insertUsuario = usuarios()
        insertUsuario.Nombre = request.POST['nombreUsuario']
        insertUsuario.correo = request.POST['correoUsuario']
        insertUsuario.usuario = request.POST['userUsuario']
        insertUsuario.contraseña = request.POST['passUsuario']
        insertUsuario.save()
        return redirect('/pagina')
    else:
        return render(request, 'inicioSesion.html',{
            'form': formRegistro()        })

def inicioSesion(request):
   if request.method == 'POST':
        try:
            detalleUsuario = usuarios.objects.get(usuario = request.POST['username'], contraseña=request.POST['password'])
            request.session['usuario'] = detalleUsuario.usuario
            return render(request, 'pagina.html')
        except usuarios.DoesNotExist as e:
            messages.success(request, 'Usuario o contraseña incorrectos!!!')
            return render(request, 'login.html')
   else:
       return render(request, 'login.html')

def cerrarSesion(request):
    try:
        del request.session['usuario']
    except:
        return render(request, 'pagina.html')
    return render(request, 'pagina.html')
