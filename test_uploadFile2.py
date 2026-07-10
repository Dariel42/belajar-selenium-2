from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

try:
    driver.get("https://gofile.io/")
    
    # 1. Gunakan WebDriverWait, bukan time.sleep()
    # 2. Cari elemen <input type="file"> menggunakan XPATH
    # presence_of_element_located memungkinkan interaksi meski elemennya di-hidden (invisible)
    file_input = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
    )
    
    print("Elemen input file ditemukan, memulai upload...")
    file_input.send_keys("/Users/mymac/Downloads/Fitted.png")
    
    # Tunggu agar proses upload selesai
    # Idealnya Anda juga menggunakan WebDriverWait di sini untuk mendeteksi pesan sukses dari Gofile
    time.sleep(15) 
    
except Exception as e:
    print(f"Gagal melakukan upload. Error: {e}")

finally:
    # Selalu gunakan driver.quit() di akhir agar tidak meninggalkan proses ChromeDriver yang menggantung di memori
    driver.quit()