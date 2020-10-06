from django.test import TestCase


class HomePageTest(TestCase):
    """Тест домашней страницы"""

    def test_used_index_template(self):
        """Используется index шаблон"""
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'main/index.html')

    def test_used_about_template(self):
        """Используется about шаблон"""
        response = self.client.get('/about/')
        self.assertTemplateUsed(response, 'main/about.html')
