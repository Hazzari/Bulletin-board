#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Функциональный тест действий пользователя на сайте."""
import time
import unittest

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

MAX_WAIT = 3


class NewVisitorBboardTest(StaticLiveServerTestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Firefox(executable_path='/Users/aleksan/.local/bin/geckodriver')

    def tearDown(self) -> None:
        self.browser.quit()

    '''
    # Александр открывает браузер и заходим на наш сайт:
    Видит заголовок сайта Главная - Доска объявлений
    # проверяем правильная ли у нас страница:
    # >>> Заголовок и шапка страницы указывают что это список дел
    '''

    def test_get_list_of_ads(self):
        # Александр открывает браузер и заходим на наш сайт:
        self.browser.get(self.live_server_url)
        # проверяем правильная ли у нас страница:
        # >>> Заголовок и шапка страницы указывают что это список дел
        self.assertIn('Главная', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Объявления', header_text)
