from django.test import TestCase


class SaludoPageTests(TestCase):
    def test_home_displays_greeting(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'hola marbel')