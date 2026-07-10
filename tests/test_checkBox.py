from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
# chrome_options.add_experimental_option("detach", True) # Menahan jendela browser tetap terbuka setelah skrip selesai dijalankan

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://omayo.blogspot.com/") # memanggil halaman omayo.blogspot.com
driver.maximize_window() # Memaksimalkan jendela browser
driver.implicitly_wait(10)
time.sleep(5) # menunggu selama 5 detik sebelum mengklik checkbox

# Mencari elemen checkbox berdasarkan ID dan mengkliknya
checkbox = driver.find_element(By.ID, "radio1").click() # Mengklik checkbox dengan ID "radio1"
time.sleep(5) # menunggu selama 5 detik sebelum mengklik checkbox

checkbox = driver.find_element(By.ID, "checkbox2").click() # Mengklik checkbox dengan ID "checkbox2"
time.sleep(5) # menunggu selama 5 detik sebelum mengklik checkbox


driver.close()