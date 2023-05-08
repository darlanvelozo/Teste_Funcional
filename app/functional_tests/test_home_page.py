import time
from selenium import webdriver
from django.test import LiveServerTestCase

class HomePageTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3) # espera até 3 segundos antes de lançar uma exceção
    def tearDown(self):
        self.browser.quit()
    def test_home_page(self):
    # Abrir a página inicial do aplicativo
        self.browser.get(self.live_server_url)
        # espera por 2 segundos para a página carregar completamente
        time.sleep(5) 
    # Verificar se o título da página contém a mensagem "Welcome to Django"
        self.assertIn('Prof: Rennê Santos', self.browser.title)