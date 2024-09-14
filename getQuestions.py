from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://stage4-pb.github.io/#")

for i in range(0, 5344):
    correct_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Correct']"))
    )
    correct_button.click()
    
    rendered_html_after_click = driver.page_source

    soup = BeautifulSoup(rendered_html_after_click, 'html.parser')
    h1_tag = soup.find('h1')

    print(f"Iteration {i+1}:")
    print(f"Question is: {h1_tag.text}")
    with open("questions2.txt", "a") as f:
        f.write(h1_tag.text + "\n")

driver.quit()
