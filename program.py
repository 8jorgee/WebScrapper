from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time
import re

# Configurar el driver de Selenium (asegúrate de tener ChromeDriver instalado)
service = Service("chromedriver.exe")  # Reemplaza con la ruta a tu ChromeDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Para ejecutar en segundo plano

driver = webdriver.Chrome(service=service, options=options)

# URL de ejemplo (esto podría ser Twitter, pero requiere autenticación)
url = "https://news.ycombinator.com/"  # Hacker News como ejemplo

driver.get(url)
time.sleep(3)  # Esperar a que la página cargue

# Obtener contenido de la página
soup = BeautifulSoup(driver.page_source, "html.parser")
driver.quit()

# Extraer datos de la página
articles = []
for item in soup.find_all("a", class_="storylink"):
    title = item.text
    link = item['href']
    articles.append((title, link))

# Mostrar los datos extraídos
print("Artículos extraídos:")
for title, link in articles:
    print(f"- {title}: {link}")

# Simulación de ataque de phishing con datos obtenidos
def simulate_phishing_attack(articles):
    fake_links = {}
    for title, link in articles:
        fake_url = re.sub(r"https?://", "https://fake-", link)  # Crear una URL engañosa
        fake_links[title] = fake_url
    return fake_links

# Crear una lista de sitios falsificados basados en los datos extraídos
phishing_sites = simulate_phishing_attack(articles)

print("\nEjemplo de sitios falsificados para phishing:")
for title, fake_link in phishing_sites.items():
    print(f"- {title}: {fake_link}")
