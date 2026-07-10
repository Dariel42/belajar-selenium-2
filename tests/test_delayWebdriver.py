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
driver.implicitly_wait(10) # Menunggu hingga 10 detik untuk menemukan elemen sebelum melemparkan NoSuchElementException

driver.get("https://omayo.blogspot.com/") # memanggil halaman google.com
print(datetime.datetime.now().time()) # menampilkan waktu saat ini
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "delayedText"))) # Menunggu hingga 10 detik untuk menemukan elemen sebelum melemparkan TimeoutException
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "delayedText"))) # Menunggu hingga 10 detik untuk menemukan elemen sebelum melemparkan TimeoutException

print(datetime.datetime.now().time()) # menampilkan waktu saat ini

driver.close()
