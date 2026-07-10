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
# driver.implicitly_wait(10) # Menunggu hingga 10 detik untuk menemukan elemen sebelum melemparkan NoSuchElementException

driver.get("https://www.toolsqa.com/selenium-training?q=headers") # memanggil halaman google.com
element = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div[1]/div[1]/img").get_attribute("src") # mendapatkan link dari elemen yang ditemukan
print(element) # menampilkan link dari elemen yang ditemukan

driver.close()