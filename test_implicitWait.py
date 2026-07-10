from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True) # Menahan jendela browser tetap terbuka setelah skrip selesai dijalankan

driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(20) # Menunggu hingga 10 detik untuk menemukan elemen sebelum melemparkan NoSuchElementException

driver.get("https://www.riffamedia.com/membuat-aplikasi-desktop-dengan-flask-dan-pyqt") # memanggil halaman google.com
print(datetime.datetime.now().time()) # menampilkan waktu saat ini
element = driver.find_element(By.XPATH, "//*[contains(text(), 'The page you requested could not be found')]") # mencari elemen yang mengandung teks 'Google'
print(datetime.datetime.now().time()) # menampilkan waktu saat ini


driver.close()
