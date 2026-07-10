from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import random

chrome_options = Options()
driver = webdriver.Chrome(options=chrome_options)

driver.maximize_window()
driver.implicitly_wait(10) # Menunggu hingga 10 detik untuk menemukan elemen
driver.get("https://www.toolsqa.com/")

# delay = random.uniform(5, 15) # Menghasilkan angka acak antara 5 hingga 15 detik
delay = random.randrange(3, 10) # Menghasilkan angka acak antara 5 hingga 15 detik
print(delay) # Menampilkan angka acak di console
time.sleep(delay) # Menunggu beberapa detik agar halaman termuat sepenuhnya

driver.quit()
