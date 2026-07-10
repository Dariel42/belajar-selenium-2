from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import os

chrome_options = Options()

# 1. Gunakan Absolute Path agar lokasi profil konsisten
# Sesuaikan path ini dengan folder di Mac Anda
profile_path = "/Users/mymac/Documents/SeleniumProfile" 

# 2. Tambahkan awalan -- pada argumen
chrome_options.add_argument(f"--user-data-dir={profile_path}") 

# (Opsional) Tetap buka browser setelah skrip selesai jika terjadi error
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://practicetestautomation.com/practice-test-login/")

# Beri waktu yang cukup panjang HANYA untuk run pertama kali agar Anda bisa login manual
# Setelah run pertama sukses, Anda bisa menghapus time.sleep ini
print("Silakan login manual sekarang. Anda punya waktu 45 detik...")
time.sleep(20) 

driver.quit()