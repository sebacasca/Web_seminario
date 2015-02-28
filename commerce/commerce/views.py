from commerce.models import producto, subcategoria, categoria
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required



from forms import SignUpForm

def lista_producto(request):
	productos = producto.objects.all()
	return render_to_response('lista_producto.html',{'lista':productos}, context_instance=RequestContext(request))
	
def pagina(request):
	return render_to_response('index.html',context_instance=RequestContext(request))

	
def nuevousuario(request):
    if not request.user.is_anonymous():
        return HttpResponseRedirect('/privado')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():  # Validaciones

            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            email = form.cleaned_data["email"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]	
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name
			

            user.save()

            return HttpResponseRedirect('/privado')  # Redirect after POST
			
    else:
        form = SignUpForm()

    data = {
        'form': form,
    }
    return render_to_response('nuevousuario.html', data, context_instance=RequestContext(request))
	
def ingresar(request):
	if not request.user.is_anonymous():
		return HttpResponseRedirect('/privado')
	if request.method == 'POST':
		formulario = AuthenticationForm(request.POST)
		if formulario.is_valid:
			usuario = request.POST['username']
			clave = request.POST['password']
			acceso = authenticate(username=usuario, password=clave)
			if acceso is not None:
				if acceso.is_active:
					login(request,acceso)
					return HttpResponseRedirect('/privado')
				else:
					return render_to_response('noactivo.html', context_instance=RequestContext(request))
			else:
			    return render_to_response('nousuario.html',{'formulario':formulario},context_instance=RequestContext(request))
	else:
	    formulario = AuthenticationForm()
            return render_to_response('ingresar.html', {'formulario':formulario}, context_instance=RequestContext(request))
	
@login_required(login_url='/ingresar')
def privado(request):
	usuario = request.user
	return render_to_response('privado.html',{'usuario':usuario}, context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def cerrar(request):
	logout(request)
	return HttpResponseRedirect('/')
	
def producto_individual(request):
    if request.method == 'POST':
        cod = request.POST["q"]
        productos = producto.objects.get(pk=cod)
        #productos = producto.objects.all()
        return render_to_response('producto_individual.html',{'elemento':productos}, context_instance=RequestContext(request))
		
def mi_carro(request):
	if request.method == 'POST':
		cod = request.POST["q"]
		productos = producto.objects.get(pk=cod)
		#productos = producto.objects.all()
		return render_to_response('mi_carro_compras.html',{'elemento':productos}, context_instance=RequestContext(request))
		
def mi_compra(request):
	return render_to_response('compra_realizada.html', context_instance=RequestContext(request))
		

