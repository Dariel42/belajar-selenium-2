from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://imgur.com/upload")
driver.maximize_window()
time.sleep(3) # Menunggu halaman termuat sepenuhnya

# Ganti cara klik dengan langsung mengirim file ke elemen <input type="file">
# CSS Selector ini secara spesifik mencari tag input yang digunakan untuk upload file
try:
    file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
    
    # Path harus akurat dan perhatikan huruf besar/kecil (Fitted.png vs fitted.png)
    file_input.send_keys("/Users/mymac/Downloads/Fitted.png") 
    print("File berhasil dikirim ke browser.")
    
except Exception as e:
    print(f"Terjadi kesalahan saat upload: {e}")

time.sleep(5) 
driver.close()