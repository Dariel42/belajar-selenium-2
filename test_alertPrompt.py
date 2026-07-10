from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.implicitly_wait(10) # Menunggu hingga 10 detik untuk menemukan elemen
driver.get("https://omayo.blogspot.com/")
time.sleep(3) # Menunggu halaman termuat sepenuhnya

driver.find_element(By.ID, "alert1").click()
time.sleep(2) # Menunggu alert muncul
driver.switch_to.alert.accept() # Klik OK pada alert
time.sleep(2) # Menunggu beberapa detik agar proses selesai

driver.find_element(By.XPATH, "//*[@id='prompt']").click()
time.sleep(2) # Menunggu prompt muncul
driver.switch_to.alert.send_keys("Ini adalah input dari prompt") # Mengirim teks ke prompt
time.sleep(2) # Menunggu beberapa detik agar proses selesai
driver.switch_to.alert.accept() # Klik OK pada prompt
time.sleep(2) # Menunggu beberapa detik agar proses selesai


driver.find_element(By.ID, "confirm").click()
time.sleep(2) # Menunggu prompt muncul
driver.switch_to.alert.accept() # Klik OK pada prompt
time.sleep(2) # Menunggu beberapa detik agar proses selesai

driver.quit()