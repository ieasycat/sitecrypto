from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse


class TestUser(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

    def test_login_GET(self):
        url = reverse('users:login')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html')

    def test_login_POST(self):
        url = reverse('users:login')
        response = self.client.post(url, {'username': 'testuser', 'password': 'testpass'})

        self.assertEqual(response.status_code, 302)

    def test_logout(self):
        self.client.logout()

        url = reverse('users:logout')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 302)
