from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from modules.print_except import imprimit_mensaje
from time import sleep
from selenium.webdriver.common.by import By


def verificar_anuncios(dvr):

    try:
        anuncio1 = dvr.find_element(By.XPATH,'//section//div[@class="panel-body"]/button[@class="cat-button normal primary"]').is_displayed()

        if anuncio1:
            try:
                boton_reglas = dvr.find_element(By.XPATH,'//section//div[@class="panel-body"]/button[@class="cat-button normal primary"]')
                dvr.execute_script("arguments[0].click();", boton_reglas)
                sleep(1)
            except:
                imprimit_mensaje("No se pudo dar click al rules")
                
    except:
        imprimit_mensaje("Error al buscar el anuncio de reglas")
        

    # anuncio2 = dvr.find_element(By.XPATH,'//section[@class="act-content"]//div[@class="carousel-3d-slider"]/div[@class="carousel-3d-slide current"]/div').is_displayed()
    # print(anuncio2)
    # sleep(2)
    try:
        anuncio_bienvenida = dvr.find_element(By.XPATH,'//section//div[@class="panel-body"]/button[@class="cat-button normal primary"]').is_displayed()
        
        if anuncio_bienvenida:
            try:
                boton_bienvenida = dvr.find_element(By.XPATH,'//div[@class="modal"]//button[@class="skip"]')
                dvr.execute_script("arguments[0].click();", boton_bienvenida)
                sleep(1)

            except:
                imprimit_mensaje("No se pudo dar click al boton de bienvenida")
                
    except:
        imprimit_mensaje("Error en el anuncio de bienvenida")
        
    
    # sleep(2)
    try:
        anuncio_seguir = dvr.find_element(By.XPATH,'//div[contains(@class,"slow-toast")]').is_displayed()
        if anuncio_seguir:
            try:
                boton_seguir = dvr.find_element(By.XPATH,'//div[contains(@class,"slow-toast")]//button')
                dvr.execute_script("arguments[0].click();", boton_seguir)
                sleep(1)
            except:
                imprimit_mensaje("No se pudo dar click al boton seguir")
                
    except:
        imprimit_mensaje("Error en el anuncio de seguir")
        
