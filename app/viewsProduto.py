from django.shortcuts import render, redirect
from app.forms import ProdutosForm
from app.models import Produto, Empresa
import json

# Create your views here.


def home(request):
    data = {}
    data['db'] = Produto.objects.all()
    return render(request, 'indexProducts.html', data)

def form(request):
    data = {}
    data['form'] = ProdutosForm()
    return render(request, 'productsForm.html', data)

def create(request,pk):
    empresa = Empresa.objects.get(pk=pk)
    produto = Produto(empresa=empresa, produto=request.POST.get("produto"))
    produto.save()
    return redirect('homeproduto')

def view(request, pk):
    data = {}
    data['db'] = Produto.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Produto.objects.get(pk=pk)
    data['form'] = ProdutosForm(instance=data['db'])
    return render(request, 'productsForm.html', data)

def update(request, pk):
    data = {}
    data['db'] = Produto.objects.get(pk=pk)
    form = ProdutosForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

def delete(request, pk):
    db = Produto.objects.get(pk=pk)
    db.delete()
    return redirect('home')

