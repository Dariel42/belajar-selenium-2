from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time

chrome_options = Options()
# chrome_options.add_experimental_option("detach", True) # Menahan jendela browser tetap terbuka setelah skrip selesai dijalankan

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://omayo.blogspot.com/") # memanggil halaman omayo.blogspot.com
driver.maximize_window() # Memaksimalkan jendela browser
time.sleep(3) # menunggu selama 3 detik sebelum mengklik checkbox

# Mencari elemen dropdown berdasarkan ID dan memilih opsi berdasarkan nilai
dropdown = Select(driver.find_element(By.ID, "drop1"))
# Memilih opsi berdasarkan nilai
# dropdown.select_by_value("ghi") # Memilih opsi dengan nilai "doc 3"
# dropdown.select_by_index(3) # Memilih opsi dengan indeks 3 (dimulai dari 0)
dropdown.select_by_visible_text("doc 1") # Memilih opsi dengan teks "doc 1"
time.sleep(3) # menunggu selama 3 detik sebelum mengklik checkbox

dropdown_multiselect = Select(driver.find_element(By.ID, "multiselect1"))
dropdown_multiselect.select_by_visible_text("Volvo")
dropdown_multiselect.select_by_visible_text("Audi") # Memilih opsi dengan teks "Volvo" dan "Audi" pada dropdown multiselect
time.sleep(3) # menunggu selama 3 detik sebelum mengklik checkbox

dropdown_multiselect.deselect_by_visible_text("Volvo") # Menghapus pilihan opsi dengan teks "Volvo" pada dropdown multiselect
time.sleep(3) # menunggu selama 3 detik sebelum mengklik checkbox

driver.close()      