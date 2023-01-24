from selenium.webdriver.common.by import By

def modo_lento(driver):
    modo_lento = driver.find_element(By.XPATH,'//div[@class="slow-mode-tip-container"]/div/span/b').is_displayed()
    print(modo_lento)
    return modo_lento