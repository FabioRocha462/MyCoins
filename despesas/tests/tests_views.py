from django.test import TestCase
from django.urls import reverse
from despesas.models import Despesas
from despesa_categoria.models import CategoriaDespesa
import datetime
def create():
    despesa = Despesas(
        name = "Teste",
        value = 1200,
        tipoDespesas = '1',
        data = datetime.date.today(),
        categoria = 1
    )
    despesa.save()
class TestViews(TestCase):
    def test_index(self):
        response = self.client.get(reverse("index"))
        assert response.status_code == 200

    def test_DespesaCreateGet(self):
        response = self.client.get(reverse("create"))
        assert response.status_code == 200

    def test_DespesaCreatePost(self):
        response = self.client.post(reverse("create"))
        assert response.status_code == 200

    def test_DespesaAll(self):
        response = self.client.get(reverse("allDespesas"))
        assert response.status_code == 200
    
    def test_DespesaEditGet(self):
        create()
        response = self.client.get(reverse("editDespesa", kwargs={"id":1} ))
        assert response.status_code == 200

    def test_DespesaEditPost(self):
        response = self.client.get(reverse("editDespesa", kwargs={"id":1}))
        assert response.status_code == 404

    def test_DespesaDelete(self):
        response = self.client.get(reverse("despesa delete", kwargs={"id":1}))
        assert response.status_code == 404


    def test_DespesaAnuais(self):
        response = self.client.get(reverse("despesasanuais"))
        assert response.status_code == 200

    def test_ReceitasAnuais(self):
        response = self.client.get(reverse("receitasanuais"))
        assert response.status_code == 200

    def test_ReceitavsDespesa(self):
        response = self.client.get(reverse("receitasvsdespesas"))
        assert response.status_code == 200

    def test_CategoriaDespesa(self):
        response = self.client.get(reverse("categoriadespesa"))
        assert response.status_code == 200

    def test_CategoriaReceita(self):
        response = self.client.get(reverse("categoriareceita"))
        assert response.status_code == 200
    
    def test_lucro(self):
        response = self.client.get(reverse("lucros"))
        assert response.status_code == 200

    