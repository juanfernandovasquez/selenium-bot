from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from modules.verificar_anuncios import verificar_anuncios
from time import sleep
from selenium.webdriver.common.by import By
from modules.test import test
from time import sleep
from modules.print_except import imprimit_mensaje


def encotrar_caja_texto_enviar_mensaje(driver, msj):
    
    verificar_anuncios(driver)

    try:
        caja_texto = driver.find_element(By.XPATH,'//div[@class="input-box"]/div[contains(@class,"editor")]')

        try:
            ActionChains(driver).move_to_element(caja_texto).click(caja_texto).perform()
            driver.execute_script("arguments[0].click();", caja_texto)
            sleep(1)

            try:
                driver.execute_script("arguments[0].click();", caja_texto)
                caja_texto.send_keys(msj)
                sleep(1)

                while True:
                    resultado = str(test(driver))
                    if resultado == "None":
                        boton_send = driver.find_element(By.XPATH,'//div[@class="input-feature-box align-center justify-between"]/button[contains(@class,"btn-send")]') 
                        driver.execute_script("arguments[0].click();", boton_send)
                        break
                    sleep(3)           

            except:
                imprimit_mensaje("Error al llenar la caja de comentarios")
                

        except:
            imprimit_mensaje("Error al seleccionar la caja de comentarios")
            

    except:
        imprimit_mensaje("""
        Error al seleccionar el cuadro de texto

        ¿Se han eliminado las notificaciones?
        """)
        