from django.shortcuts import render
from django.urls import reverse_lazy
from .models import LocalComida, LocalRepuesto, Persona, Barrio
from .forms import PersonaForm, BarrioForm, LocalComidaForm, LocalRepuestoForm
from rest_framework import viewsets
from .serializers import PersonaSerializer, BarrioSerializer, LocalComidaSerializer, LocalRepuestoSerializer
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required


def home(request):
    return render(request, 'home.html')

# BARRIO
def listar_barrios(request):
    barrios = Barrio.objects.all()
    headers = [field.name for field in Barrio._meta.fields]
    return render(request, 'list.html', {'objects_list': barrios, 'object_type': 'barrios', 'headers': headers})


def crear_barrio(request):
    if request.method == "POST":
        form = BarrioForm(request.POST)
        if form.is_valid():
            barrio = form.save()
            return redirect('listar_barrios')
    else:
        form = BarrioForm()
    return render(request, 'form.html', {'form': form})


def editar_barrio(request, id):
    barrio = get_object_or_404(Barrio, id=id)
    if request.method == "POST":
        form = BarrioForm(request.POST, instance=barrio)
        if form.is_valid():
            barrio = form.save()
            return redirect('listar_barrios')
    else:
        form = BarrioForm(instance=barrio)
    return render(request, 'form.html', {'form': form})


def borrar_barrio(request, id):
    barrio = get_object_or_404(Barrio, id=id)
    if request.method == "DELETE":
        barrio.delete()
    return redirect('listar_barrios')

# PERSONA
def listar_personas(request):
    personas = Persona.objects.all()
    headers = [field.name for field in Persona._meta.fields]
    return render(request, 'list.html', {'objects_list': personas, 'object_type': 'personas', 'headers': headers})


def crear_persona(request):
    if request.method == "POST":
        form = PersonaForm(request.POST)
        if form.is_valid():
            persona = form.save()
            return redirect('listar_personas')
    else:
        form = PersonaForm()
    return render(request, 'form.html', {'form': form})


def editar_persona(request, id):
    persona = get_object_or_404(Persona, id=id)
    if request.method == "POST":
        form = PersonaForm(request.POST, instance=persona)
        if form.is_valid():
            persona = form.save()
            return redirect('listar_personas')
    else:
        form = PersonaForm(instance=persona)
    return render(request, 'form.html', {'form': form})


def borrar_persona(request, id):
    persona = get_object_or_404(Persona, id=id)
    if request.method == "DELETE":
        persona.delete()
    return redirect('listar_personas')

# LOCALES REPUESTOS

def listar_locales_repuestos(request):
    locales = LocalRepuesto.objects.all()
    headers = [field.name for field in LocalRepuesto._meta.fields] + \
        ['pago_permiso']

    return render(request, 'list.html', {'objects_list': locales, 'object_type': 'locales repuestos', 'headers': headers})


def crear_local_repuesto(request):
    if request.method == "POST":
        form = LocalRepuestoForm(request.POST)
        if form.is_valid():
            local = form.save()
            return redirect('listar_locales_repuestos')
    else:
        form = LocalRepuestoForm()
    return render(request, 'form.html', {'form': form})


@login_required(login_url=reverse_lazy('login'))
@permission_required('app.change_localrepuesto', login_url=reverse_lazy('login'))
def editar_local_repuesto(request, id):
    local = get_object_or_404(LocalRepuesto, id=id)
    if request.method == "POST":
        form = LocalRepuestoForm(request.POST, instance=local)
        if form.is_valid():
            local = form.save()
            return redirect('listar_locales_repuestos')
    else:
        form = LocalRepuestoForm(instance=local)
    return render(request, 'form.html', {'form': form})


@login_required(login_url=reverse_lazy('login'))
@permission_required('app.delete_localrepuesto', login_url=reverse_lazy('login'))
def borrar_local_repuesto(request, id):
    local = get_object_or_404(LocalRepuesto, id=id)
    if request.method == "DELETE":
        local.delete()
    return redirect('listar_locales_repuestos')

# LOCALES COMIDA
def listar_locales_comida(request):
    locales = LocalComida.objects.all()
    headers = [field.name for field in LocalComida._meta.fields] + \
        ['pago_permiso']
    return render(request, 'list.html', {'objects_list': locales, 'object_type': 'locales comida', 'headers': headers})


def crear_local_comida(request):
    if request.method == "POST":
        # Asumiendo que estás utilizando un ModelForm para LocalComida
        form = LocalComidaForm(request.POST)
        if form.is_valid():
            local = form.save()
            return redirect('listar_locales_comida')
    else:
        form = LocalComidaForm()
    return render(request, 'form.html', {'form': form})

@login_required(login_url=reverse_lazy('login'))
@permission_required('app.change_localcomida', login_url=reverse_lazy('login'))
def editar_local_comida(request, id):
    local = get_object_or_404(LocalComida, id=id)
    if request.method == "POST":
        form = LocalComidaForm(request.POST, instance=local)
        if form.is_valid():
            local = form.save()
            return redirect('listar_locales_comida')
    else:
        form = LocalComidaForm(instance=local)
    return render(request, 'form.html', {'form': form})

@login_required(login_url=reverse_lazy('login'))
@permission_required('app.delete_localcomida', login_url=reverse_lazy('login'))
def borrar_local_comida(request, id):
    local = get_object_or_404(LocalComida, id=id)
    if request.method == "DELETE":
        local.delete()
    return redirect('listar_locales_comida')


# VIEWSETS PARA LA REST API
class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer


class BarrioViewSet(viewsets.ModelViewSet):
    queryset = Barrio.objects.all()
    serializer_class = BarrioSerializer


class LocalComidaViewSet(viewsets.ModelViewSet):
    queryset = LocalComida.objects.all()
    serializer_class = LocalComidaSerializer


class LocalRepuestoViewSet(viewsets.ModelViewSet):
    queryset = LocalRepuesto.objects.all()
    serializer_class = LocalRepuestoSerializer
