from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.core import mail


class SignupTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_signup_page_loads(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')

    def test_signup_successful(self):
        response = self.client.post(reverse('signup'), {
            'name': 'testuser',
            'mail': 'testuser@example.com',
            'password': 'testpassword',
            'password2': 'testpassword'
        })
        self.assertRedirects(response, reverse('main-page'))
        user = User.objects.get(username='testuser')
        self.assertFalse(user.is_active)
        self.assertEqual(len(mail.outbox), 1)
        self.assertIn('admin@example.com', mail.outbox[0].to)

    def test_signup_username_already_taken(self):
        User.objects.create_user('testuser', 'testuser@example.com', 'testpassword')
        response = self.client.post(reverse('signup'), {
            'name': 'testuser',
            'mail': 'testuser2@example.com',
            'password': 'testpassword',
            'password2': 'testpassword'
        })
        self.assertRedirects(response, reverse('main-page'))
        self.assertIn('This username is already taken', response.cookies.output(header='', sep=';'))

    def test_signup_passwords_do_not_match(self):
        response = self.client.post(reverse('signup'), {
            'name': 'testuser',
            'mail': 'testuser@example.com',
            'password': 'testpassword',
            'password2': 'testpassword2'
        })
        self.assertRedirects(response, reverse('main-page'))
        self.assertIn('Passwords do not match', response.cookies.output(header='', sep=';'))


class LoginTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('testuser', 'testuser@example.com', 'testpassword')
    
    def test_login_page_loads(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_login_successful(self):
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertRedirects(response, reverse('main-page'))
        self.assertEqual(str(response.wsgi_request.user), 'testuser')

    def test_login_invalid_credentials(self):
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'wrongpassword'
        })
        self.assertRedirects(response, reverse('login'))
        self.assertIn('Invalid username or password', response.cookies.output(header='', sep=';'))


class MainPageTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('testuser', 'testuser@example.com', 'testpassword')

    def test_main_page_loads(self):
        response = self.client.get(reverse('main-page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main_page.html')
        self.assertIn(self.user, response.context['users'])


