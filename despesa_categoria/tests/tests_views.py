from django.test import TestCase
from django.urls import reverse

class TestCategoriaDespesas(TestCase):
    def test_categoria_despesas_createGet(self):
        response = self.client.get(reverse("create category despesa"))
        assert response.status_code == 200

    def test_categoria_despesas_createPost(self):
        response = self.client.post(reverse("create category despesa"))
        assert response.status_code == 200
