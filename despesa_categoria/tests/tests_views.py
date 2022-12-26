from django.test import TestCase
from django.urls import reverse
from despesa_categoria.forms import CategoriaDespesaForm
from despesa_categoria.models import CategoriaDespesa

class TestCategoriaDespesas(TestCase):
    def test_categoria_despesas_createGet(self):
        response = self.client.get(reverse("create category despesa"))
        assert response.status_code == 200

    def test_categoria_despesas_createPost(self):
        name = "teste categoria"
        response = self.client.post(reverse("create category despesa"),{"name":name})
        assert response.status_code == 200

    def test_categoria_despesa_editGet(self):
        name = "teste editado"
        response = self.client.get(reverse("edite categoria despesa"),kwargs={"id":1})
        assert response.status_code == 200



    
