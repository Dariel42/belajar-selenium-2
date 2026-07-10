from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
# chrome_options.add_extension("/Users/mymac/Downloads/belajar-selenium-2/proxy.zip")
chrome_options.add_extension("/Users/mymac/Downloads/belajar-selenium-2/extension_1_0_9_0.crx")
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get("https://whatismyipaddress.com/")
driver.implicitly_wait(10) # Menunggu hingga 10 detik untuk menemukan elemen

time.sleep(10) # Menunggu halaman termuat sepenuhnya
driver.quit()