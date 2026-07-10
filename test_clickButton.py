from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
# chrome_options.add_experimental_option("detach", True) # Menahan jendela browser tetap terbuka setelah skrip selesai dijalankan

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.toolsqa.com/") # memanggil halaman
time.sleep(3) # menunggu selama 3 detik sebelum mengeksekusi script

# driver.find_element(By.CSS_SELECTOR, "body > div.landing-page > div.banners > div.container-fluid > div > div.col-12.col-md-6.col-xl-5.order-md-0.new-training.justify-content-sm-center > div.row.align-items-center > div.col.col-sm-6.col-md-7 > a").click() # mencari elemen mengkliknya
# time.sleep(3) # menunggu selama 3 detik sebelum mengeksekusi script

# driver.find_element(By.CLASS_NAME, "new-training__read-more").click() # mencari elemen mengkliknya dari class name
# time.sleep(3) # menunggu selama 3 detik sebelum mengeksekusi script

driver.find_element(By.LINK_TEXT, "Read More").click() # mencari elemen mengkliknya dari link text
time.sleep(3) # menunggu selama 3 detik sebelum mengeksekusi script

driver.close()

