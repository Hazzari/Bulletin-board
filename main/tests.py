from django.test import TestCase


class HomePageTest(TestCase):
    """Тест домашней страницы"""

    def test_used_index_template(self):
        """Используется index шаблон"""
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'main/index.html')
