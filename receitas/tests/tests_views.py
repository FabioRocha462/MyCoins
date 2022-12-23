from django.test import TestCase
from django.urls import reverse

class TesteViews(TestCase):
    def test_receitasAll(self):
        response = self.client.get(reverse("receita all"))
        assert response.status_code == 200

    def test_receitaCreateGet(self):
        response = self.client.get(reverse("receita create"))
        assert response.status_code == 200

    def test_receitaCreatePost(self):
        response = self.client.post(reverse("receita create"))
        assert response.status_code == 200

    def test_receitaEditGet(self):
        response = self.client.get(reverse("edit Receitas", kwargs={"id":1}))
        assert response.status_code == 404

    def test_receitaDelete(self):
        response = self.client.get(reverse("receita delete", kwargs={"id":1}))
        assert response.status_code == 404
        