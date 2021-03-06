from django import forms
from django.forms.models import inlineformset_factory

from .models import Item, Pedido, Roupa, Status, Suporte


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['pagamento', 'data_entrega']



class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['servico', 'roupa', 'quantidade', 'pedido']


ItemFormset = forms.inlineformset_factory(Pedido, Item, form=ItemForm, extra=1)


class RoupaForm(forms.ModelForm):
    class Meta:
        model = Roupa
        fields = ['nome_peca', 'preco_roupa']


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['comentario', 'pedido', 'situacao_pedido', 'data_comentario']


class SuporteForm(forms.ModelForm):
    class Meta:
        model = Suporte
        fields = ['nome_cliente', 'email', 'cpf', 'mensagem', 'resposta']
