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
#element = driver.find_element(By.CLASS_NAME, "enroll__why--to").text # mencari elemen yang mengandung teks
element = driver.find_element(By.CSS_SELECTOR, 'body > div.selenium-training-page > div.enroll > div > div:nth-child(2) > div > div.enroll__why--to').text # mencari elemen yang mengandung teks 'Google'
print(element) # menampilkan teks dari elemen yang ditemukan

driver.close()