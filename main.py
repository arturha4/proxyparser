import sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

if __name__ == '__main__':
    email = "ваш логин"
    password = "ваш пароль"
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)  # This keeps the browser open
    driver = webdriver.Chrome(options=chrome_options)

    driver.get('https://px6.me/user/proxy')
    button = None
    try:
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "i.icon-login"))
        )

    except:
        print('Кнпока логина не найдена')
        sys.exit()
    finally:
        if button:
            button.click()

    email_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "email"))
    )
    email_input.send_keys(email)
    password_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "password"))
    )
    password_input.send_keys(password)
    WebDriverWait(driver, 600).until(
        lambda d: d.current_url == "https://px6.me/user/proxy"
    )
    rows = WebDriverWait(driver, 30).until(
        EC.presence_of_all_elements_located((By.XPATH, "//tr[starts-with(@id, 'el-')]"))
    )
    for row in rows:
        proxy_element = row.find_element(By.XPATH, ".//div[contains(@class, 'clickselect')]/b")
        proxy_value = proxy_element.text
        expiration_date_element = row.find_element(By.XPATH, "//li[@class='mobile-show' and div[contains(text(), 'Дата окончания')]]")
        date_time_div = expiration_date_element.find_element(By.XPATH, ".//div[@class='right']")
        date_time_text = date_time_div.text.strip()
        print(f'{proxy_value} - {date_time_text}')
