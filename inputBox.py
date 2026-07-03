from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
# chrome_options.add_experimental_option("detach", True) # Menahan jendela browser tetap terbuka setelah skrip selesai dijalankan

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window() # Memaksimalkan jendela browser

driver.get("https://omayo.blogspot.com/") # memanggil halaman 
time.sleep(5) # menunggu selama 5 detik sebelum mengisi input box

driver.find_element(By.XPATH, "//*[@id='BlogSearch1_form']/form/table/tbody/tr/td[1]/input").send_keys("Selenium") # mengisi input box dengan teks
time.sleep(5) # menunggu selama 5 detik sebelum mengisi input box

driver.find_element(By.ID, "ta1").send_keys("Belajar mengisi textarea") # mengisi input box dengan teks
time.sleep(5) # menunggu selama 5 detik

driver.find_element(By.XPATH, "//*[@id='textbox1']").clear()  # Untuk menghapus teks yang ada di input box
time.sleep(5) # menunggu selama 5 detik sebelum mengisi input box

data = "Belajar copywriter teks di input box"
for char in data:
    driver.find_element(By.XPATH, "//*[@id='textbox1']").send_keys(char) # mengisi input box dengan teks satu per satu karakter
    time.sleep(0.2) # menunggu selama 0.2 detik sebelum mengisi input box   


driver.close()  