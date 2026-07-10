from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--headless") # Menjalankan browser dalam mode headless (tanpa GUI)
# chrome_options.add_argument("--star-t-maximized") # Membuka browser dalam mode layar penuh
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
# driver.fullscreen_window() # Membuka browser dalam mode layar penuh
driver.implicitly_wait(10) # Menunggu hingga 10 detik untuk menemukan elemen
driver.get("https://www.toolsqa.com/")

getText = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div[2]/div[3]").text
print(getText) # Menampilkan teks yang ditemukan di console
time.sleep(5) # Menunggu beberapa detik agar proses selesai


driver.quit()