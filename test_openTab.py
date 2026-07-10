from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.implicitly_wait(10) # Menunggu hingga 10 detik untuk menemukan elemen
driver.get("https://www.toolsqa.com/")

getText = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div[2]/div[3]").text
print(getText) # Menampilkan teks yang ditemukan di console
time.sleep(5) # Menunggu beberapa detik agar proses selesai

driver.execute_script("window.open('https://www.youtube.com');") # Membuka tab baru dengan URL yang ditentukan
time.sleep(5) # Menunggu beberapa detik agar tab baru termuat sepenuhnya

driver.execute_script("window.open('https://www.google.com');") # Membuka tab baru dengan URL yang ditentukan
time.sleep(5) # Menunggu beberapa detik agar tab baru termuat sepenuhnya

driver.window_handles[0] # Mengambil handle dari tab pertama
driver.switch_to.window(driver.window_handles[0]) # Beralih ke tab pertama
time.sleep(5) # Menunggu beberapa detik agar proses selesai

driver.window_handles[1] # Mengambil handle dari tab kedua
driver.switch_to.window(driver.window_handles[1]) # Beralih ke tab kedua
time.sleep(5) # Menunggu beberapa detik agar proses selesai


driver.quit()