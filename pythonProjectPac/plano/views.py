from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from .forms import PlanoForm, TopicoForm
from .models import Plano, Topico

def index(request):
    # Carrega a página principal
    return render(request, 'index.html')

def municipio(request, municipio):
    # Busca os planos existentes para o município
    planos = Plano.objects.filter(municipio=municipio)
    context = {'municipio': municipio, 'planos': planos}
    return render(request, 'municipio.html', context)

def criar_plano(request, municipio):
    TopicoFormSet = modelformset_factory(Topico, form=TopicoForm, extra=1)
    if request.method == 'POST':
        form = PlanoForm(request.POST)
        formset = TopicoFormSet(request.POST, request.FILES, queryset=Topico.objects.none())
        if form.is_valid() and formset.is_valid():
            plano = form.save(commit=False)
            plano.municipio = municipio  # Assume que o modelo Plano tem um campo `municipio`
            plano.save()
            for form in formset:
                topico = form.save(commit=False)
                topico.plano = plano
                topico.save()
            return redirect('listar_planos')  # Certifique-se de que existe uma view 'listar_planos'
    else:
        form = PlanoForm()
        formset = TopicoFormSet(queryset=Topico.objects.none())
    return render(request, 'criar_plano.html', {'form': form, 'formset': formset, 'municipio': municipio})
