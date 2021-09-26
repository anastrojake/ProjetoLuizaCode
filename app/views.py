from django.shortcuts import render, redirect, HttpResponse
from app.forms import EmpresaForm
from app.models import Empresa, Produto
from django.core import serializers
from django.core.paginator import Paginator


def home(request):
    data = {}
    all = Empresa.objects.all()
    paginator = Paginator(all, 10)
    pages = request.GET.get('page')
    data['db'] = paginator.get_page(pages)
    return render(request, 'index.html', data)


def form(request):
    data = {}
    data['form'] = EmpresaForm()
    return render(request, 'form.html', data)


def create(request):
    form = EmpresaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('home')


def view(request, pk):
    data = {}
    data['db'] = Empresa.objects.get(pk=pk)
    return render(request, 'view.html', data)


def edit(request, pk):
    data = {}
    data['db'] = Empresa.objects.get(pk=pk)
    data['form'] = EmpresaForm(instance=data['db'])
    return render(request, 'form.html', data)


def update(request, pk):
    data = {}
    data['db'] = Empresa.objects.get(pk=pk)
    form = EmpresaForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')


def delete(request, pk):
    db = Empresa.objects.get(pk=pk)
    db.delete()
    return redirect('home')


def produtos(request, pk):
    data = {}
    data['db'] = Produto.objects.filter(empresa_id=pk)
    data["empresa_id"] = pk
    # data = {}
    # produtos = list(Produto.objects.filter(empresa_id=pk).all())
    # produtos_json = serializers.serialize('json', produtos)
    # data['db'] = produtos_json
    print(data)
    return render(request, "indexProducts.html", data)

