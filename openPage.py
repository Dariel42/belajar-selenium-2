from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True) # Menahan jendela browser tetap terbuka setelah skrip selesai dijalankan

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.google.com") # memanggil halaman google.com
print(driver.title) # menampilkan judul halaman
print(driver.current_url) # menampilkan url halaman
print(driver.page_source) # menampilkan source code halaman

driver.get("https://www.facebook.com")
print(driver.title) # menampilkan judul halaman
print(driver.current_url) # menampilkan url halaman
print(driver.page_source) # menampilkan source code halaman

driver.get("https://www.instagram.com")
print(driver.title) # menampilkan judul halaman
print(driver.current_url) # menampilkan url halaman
print(driver.page_source) # menampilkan source code halaman
