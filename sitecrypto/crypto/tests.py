from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from crypto.models import Crypto, Network


class TestCrypto(TestCase):

    def setUp(self):
        self.client = Client()
        self.network = Network.objects.create(title='erc-20', full_name='Ethereum')
        self.crypto = Crypto.objects.create(title='Usdt', full_name='Tether')
        self.crypto.networks.add(self.network)
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

    def test_get_index(self):
        url = reverse('home')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'crypto/index.html')

    def test_get_network(self):
        url = reverse('network', args=['erc-20'])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'crypto/index.html')

    def test_get_network_with_wrong_slug(self):
        url = reverse('network', args=['test'])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 404)

    def test_get_post(self):
        url = reverse('post', args=['tether'])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'crypto/post.html')

    def test_get_post_with_error_slug(self):
        url = reverse('post', args=['test'])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 404)

    def test_add_new_post(self):
        url = reverse('add_page')
        response = self.client.post(url, {
            'title': 'eth',
            'full_name': 'Ethereum',
            'content': 'Test content',
            'is_published': True,
            'networks': self.network.id
        })

        new_crypto = Crypto.objects.get(pk=2)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Crypto.objects.count(), 2)
        self.assertEqual(new_crypto.title, 'eth')
        self.assertEqual(new_crypto.full_name, 'Ethereum')

    def test_add_new_post_no_login(self):
        self.client.logout()

        url = reverse('add_page')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 302)

    def test_add_new_post_no_data(self):
        url = reverse('add_page')
        response = self.client.post(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Crypto.objects.count(), 1)
        self.assertTemplateUsed(response, 'crypto/addpage.html')

    def test_update_post(self):
        url = reverse('edit_page', args=['tether'])
        response = self.client.post(url, {
            'title': 'usdt',
            'full_name': 'tether',
            'content': 'Test content',
            'is_published': True,
            'networks': self.network.id
        })

        crypto = Crypto.objects.all().first()

        self.assertEqual(response.status_code, 302)
        self.assertEqual(crypto.content, 'Test content')

    def test_update_post_no_login(self):
        self.client.logout()

        url = reverse('edit_page', args=['tether'])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 302)

    def test_update_post_no_datat(self):
        url = reverse('edit_page', args=['tether'])
        response = self.client.post(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'crypto/editpage.html')

    def test_delete_post(self):
        url = reverse('delete_page', args=['tether'])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Crypto.objects.count(), 0)

    def test_delete_post_no_login(self):
        self.client.logout()

        url = reverse('delete_page', args=['tether'])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 302)

    def test_delete_post_with_wrong_slug(self):
        url = reverse('delete_page', args=['test'])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(Crypto.objects.count(), 1)

    def test_get_about(self):
        url = reverse('about')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'crypto/about.html')

    def test_get_contact(self):
        url = reverse('contact')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'crypto/contact.html')

    def get_search_post(self):
        url = reverse('search_post', args=['usdt'])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def get_search_post_no_data(self):
        url = reverse('search_post')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 404)
