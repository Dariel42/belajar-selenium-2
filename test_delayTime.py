from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
#chrome_options.add_experimental_option("detach", True) # Menahan jendela browser tetap terbuka setelah skrip selesai dijalankan

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.google.com") # memanggil halaman google.com
time.sleep(5) # menunggu selama 5 detik

driver.get("https://www.facebook.com")
time.sleep(5) # menunggu selama 5 detik

driver.get("https://www.instagram.com")
time.sleep(5) # menunggu selama 5 detik

driver.close()
