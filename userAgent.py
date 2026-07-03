from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.3.1 Safari/605.1.15")
# chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get("https://www.whatismybrowser.com/detect/what-is-my-user-agent/")
driver.implicitly_wait(10) # Menunggu hingga 10 detik untuk menemukan elemen


time.sleep(10) # Menunggu beberapa detik agar halaman termuat sepenuhnya
driver.quit()