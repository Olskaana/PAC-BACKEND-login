from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from .forms import PlanoForm, TopicoForm, AdicionalForm, AcaoForm, BibliotecaForm
from .models import Plano, Topico, Adicional, Acao, Biblioteca
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

def index(request):
    # Carrega a página principal
    return render(request, 'index.html')

def municipio(request, municipio):
    # Busca os planos existentes para o município
    planos = Plano.objects.filter(municipio=municipio)
    context = {'municipio': municipio, 'planos': planos}
    return render(request, 'municipio.html', context)

def plano_detail(request, municipio, id_plano):
    plano = get_object_or_404(Plano, id=id_plano, municipio=municipio)
    context = {
        'plano': plano,
        'municipio': municipio
    }
    return render(request, 'plano_detail.html', context)

def criar_plano(request, municipio):
    TopicoFormSet = modelformset_factory(Topico, form=TopicoForm, extra=1)
    AdicionalFormSet = modelformset_factory(Adicional, form=AdicionalForm, extra=1)
    AcaoFormSet = modelformset_factory(Acao, form=AcaoForm, extra=1)
    BibliotecaFormSet = modelformset_factory(Biblioteca, form=BibliotecaForm, extra=1)

    print("metodo")
    print(request.method)
    if request.method == 'POST':
        form = PlanoForm(request.POST)
        formset_topico = TopicoFormSet(request.POST, request.FILES, queryset=Topico.objects.none(), prefix='topico')
        formset_adicional = AdicionalFormSet(request.POST, request.FILES, queryset=Adicional.objects.none(), prefix='adicional')
        formset_acao = AcaoFormSet(request.POST, request.FILES, queryset=Acao.objects.none(), prefix='acao')
        formset_biblioteca = BibliotecaFormSet(request.POST, request.FILES, queryset=Biblioteca.objects.none(), prefix='biblioteca')

        if form.is_valid() and formset_topico.is_valid() and formset_adicional.is_valid() and formset_acao.is_valid() and formset_biblioteca.is_valid():
            plano = form.save(commit=False)
            plano.municipio = municipio
            plano.save()

            for form in formset_topico:
                if form.is_valid():
                    topico = form.save(commit=False)
                    topico.plano = plano
                    topico.save()

            for form in formset_adicional:
                if form.is_valid():
                    adicional = form.save(commit=False)
                    adicional.plano = plano
                    adicional.save()

            for form in formset_acao:
                if form.is_valid():
                    acao = form.save(commit=False)
                    acao.plano = plano
                    acao.save()
                    print("salvou a acao")

            for form in formset_biblioteca:
                if form.is_valid():
                    biblioteca = form.save(commit=False)
                    biblioteca.plano = plano
                    biblioteca.save()

            return redirect('municipio', municipio=municipio)
    else:
        form = PlanoForm()
        formset_topico = TopicoFormSet(queryset=Topico.objects.none(), prefix='topico')
        formset_adicional = AdicionalFormSet(queryset=Adicional.objects.none(), prefix='adicional')
        formset_acao = AcaoFormSet(queryset=Acao.objects.none(), prefix='acao')
        formset_biblioteca = BibliotecaFormSet(queryset=Biblioteca.objects.none(), prefix='biblioteca')

    return render(request, 'criar_plano.html', {
        'form': form,
        'formset_topico': formset_topico,
        'formset_adicional': formset_adicional,
        'formset_acao': formset_acao,
        'formset_biblioteca': formset_biblioteca,
        'municipio': municipio
    })

def excluir_plano(request, municipio, id_plano):
    plano = get_object_or_404(Plano, id=id_plano, municipio=municipio)

    if request.method == 'POST':
        plano.delete()
        return redirect('municipio', municipio=municipio)

    return render(request, 'excluir_plano.html', {
        'plano': plano,
        'municipio': municipio,
    })


#sem uso
def editar_plano(request, municipio, id_plano):
    plano = get_object_or_404(Plano, id=id_plano, municipio=municipio)

    # Formulário principal para o Plano
    form = PlanoForm(request.POST or None, instance=plano)

    # Formsets para os detalhes relacionados ao Plano
    TopicoFormSet = modelformset_factory(Topico, form=TopicoForm, extra=1)
    AdicionalFormSet = modelformset_factory(Adicional, form=AdicionalForm, extra=1)
    AcaoFormSet = modelformset_factory(Acao, form=AcaoForm, extra=1)
    BibliotecaFormSet = modelformset_factory(Biblioteca, form=BibliotecaForm, extra=1)

    formset_topico = TopicoFormSet(request.POST or None, request.FILES or None, queryset=Topico.objects.filter(plano=plano), prefix='topico')
    formset_adicional = AdicionalFormSet(request.POST or None, request.FILES or None, queryset=Adicional.objects.filter(plano=plano), prefix='adicional')
    formset_acao = AcaoFormSet(request.POST or None, request.FILES or None, queryset=Acao.objects.filter(plano=plano), prefix='acao')
    formset_biblioteca = BibliotecaFormSet(request.POST or None, request.FILES or None, queryset=Biblioteca.objects.filter(plano=plano), prefix='biblioteca')

    if request.method == 'POST':
        if form.is_valid() and formset_topico.is_valid() and formset_adicional.is_valid() and formset_acao.is_valid() and formset_biblioteca.is_valid():
            plano = form.save(commit=False)
            plano.save()

            # Salvando formsets
            for form in formset_topico:
                if form.is_valid():
                    topico = form.save(commit=False)
                    topico.plano = plano
                    topico.save()

            for form in formset_adicional:
                if form.is_valid():
                    adicional = form.save(commit=False)
                    adicional.plano = plano
                    adicional.save()

            for form in formset_acao:
                if form.is_valid():
                    acao = form.save(commit=False)
                    acao.plano = plano
                    acao.save()

            for form in formset_biblioteca:
                if form.is_valid():
                    biblioteca = form.save(commit=False)
                    biblioteca.plano = plano
                    biblioteca.save()

            return redirect('plano_detail', municipio=municipio, id_plano=id_plano)

    context = {
        'form': form,
        'formset_topico': formset_topico,
        'formset_adicional': formset_adicional,
        'formset_acao': formset_acao,
        'formset_biblioteca': formset_biblioteca,
        'municipio': municipio,
        'plano': plano,
    }

    return render(request, 'editar_plano.html', context)

def criar_plano_api(request, municipio):
    if request.method == 'POST':
        # Lógica para criar um plano
        TopicoFormSet = modelformset_factory(Topico, form=TopicoForm, extra=1)
        AdicionalFormSet = modelformset_factory(Adicional, form=AdicionalForm, extra=1)
        AcaoFormSet = modelformset_factory(Acao, form=AcaoForm, extra=1)
        BibliotecaFormSet = modelformset_factory(Biblioteca, form=BibliotecaForm, extra=1)

        form = PlanoForm(request.POST)
        formset_topico = TopicoFormSet(request.POST, request.FILES, queryset=Topico.objects.none(), prefix='topico')
        formset_adicional = AdicionalFormSet(request.POST, request.FILES, queryset=Adicional.objects.none(), prefix='adicional')
        formset_acao = AcaoFormSet(request.POST, request.FILES, queryset=Acao.objects.none(), prefix='acao')
        formset_biblioteca = BibliotecaFormSet(request.POST, request.FILES, queryset=Biblioteca.objects.none(), prefix='biblioteca')

        if form.is_valid() and formset_topico.is_valid() and formset_adicional.is_valid() and formset_acao.is_valid() and formset_biblioteca.is_valid():
            plano = form.save(commit=False)
            plano.municipio = municipio
            plano.save()

            for form in formset_topico:
                if form.is_valid():
                    topico = form.save(commit=False)
                    topico.plano = plano
                    topico.save()

            for form in formset_adicional:
                if form.is_valid():
                    adicional = form.save(commit=False)
                    adicional.plano = plano
                    adicional.save()

            for form in formset_acao:
                if form.is_valid():
                    acao = form.save(commit=False)
                    acao.plano = plano
                    acao.save()

            for form in formset_biblioteca:
                if form.is_valid():
                    biblioteca = form.save(commit=False)
                    biblioteca.plano = plano
                    biblioteca.save()

            return JsonResponse({'message': 'Plano criado com sucesso!'})

        else:
            return JsonResponse({'error': 'Erro ao processar formulários'}, status=400)

    else:
        return JsonResponse({'error': 'Método não permitido'}, status=405)