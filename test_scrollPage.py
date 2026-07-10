from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.implicitly_wait(10) # Menunggu hingga 10 detik untuk menemukan elemen
driver.get("https://www.toolsqa.com/")
time.sleep(5) # Menunggu beberapa detik agar halaman termuat sepenuhnya

driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(By.XPATH, "/html/body/footer/div[2]/div[5]/div")) # Menggulir ke bawah halaman
time.sleep(5) # Menunggu beberapa detik agar halaman termuat sepenuhnya

driver.quit()