from django.forms import ModelForm
from app.models import Empresa, Produto

# Create the form class.
class EmpresaForm(ModelForm):
    class Meta:
        model = Empresa
        fields = ['empresa', 'cnpj', 'email']


class ProdutosForm(ModelForm):
    class Meta:
        model = Produto
        fields = ['produto', 'codigo', 'descricao','marca', 'valor']

