from selenium import webdriver
from time import sleep
import pytest
import subprocess
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver

@pytest.fixture
def driver():
    # Iniciar o Streamlit em background
    process = subprocess.Popen(["streamlit", "run", "src/app.py"])
    options = Options()
    options.headless = True  # Executar em modo headless
    driver = webdriver.Chrome(options=options)
    # Iniciar o WebDriver usando GeckoDriver
    driver.set_page_load_timeout(5)
    yield driver

    # Fechar o WebDriver e o Streamlit após o teste
    driver.quit()
    process.kill()

def test_app_opens(driver: WebDriver):
    # Verificar se a página abre
    driver.get("http://localhost:8501")
    sleep(2)