from django.db.models import fields
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Fieldset, Layout, Submit
from django import forms

from .models import Pedido
from pedido import models


class PedidoCreateForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = [
            "cnpj",
            "status",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.form_action = "."
        self.helper.add_input(
            Submit(
                "submit",
                "Finalizar compra",
                css_class="btn btn-success btn-lg btn-block",
            )
        )
        self.helper.layout = Layout(
            Fieldset(
                "",
                "cnpj",
                "status",
                css_class="border-bottom mb-3",
            )
        )

class FinalizaPedidoForm(forms.ModelForm):
    class Meta:
        model = models.Pedido
        fields = ['status']
        