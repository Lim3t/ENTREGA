
from django.shortcuts import render,redirect
from .models import Cliente
from .form import ClienteForm

# Create your views here.
def index(request):
    return render(request,'core/index.html')

def test(request):

    Clientes = Cliente.objects.all()

    datos = { 
        'Clientes': Clientes
        }
    return render(request,'core/test.html',datos)


def form_cliente(request):
    data = { 
        'form': ClienteForm()
    }

    if request.method=='POST':
        formulario = ClienteForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            data['mensaje']='guardado con EXITO'
        

    return render(request,'core/form_cliente.html',data)

def form_mod_cliente(request,id):
    cliente= Cliente.objects.get(nombre=id)
    data={
        'form':ClienteForm(instance=cliente)
    }
    if request.method =='POST':
        formulario=ClienteForm(data=request.POST,instance=cliente)
    
        if formulario.is_valid:
            formulario.save()
            data['mensaje'] ="modificados correctamente"
    return render(request,'core/form_cliente.html',data)


def Form_del_cliente(request,id):
    cliente = Cliente.objects.get(nombre=id)
    cliente.delete()
    return redirect(to="test")

