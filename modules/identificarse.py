import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
from time import sleep
import os
from modules.print_except import imprimit_mensaje

def identificarse_en_trovo(drivers):

    print(""" 
 
    Después de cerrar las notificaciones, pulsar enter

    """)


    try:
        input()
    except Exception as e:
        imprimit_mensaje(e)


    ruta = os.path.join(os.path.abspath(''),'cuentas.json')
    cuentas = []

    with open(ruta) as contenido:
        cuentas = json.load(contenido)

    i = 0
    for dr in drivers:

        ###Corregir que funcione en cualquier idioma ctmr
        cuenta = cuentas[i]
        try:
            boton_iniciar_sesion= dr.find_element(By.XPATH,'//div[@class="login-btn-wrap"]/button[contains(@class,"cat-button")]')
            dr.execute_script("arguments[0].click();", boton_iniciar_sesion)
        except:
            imprimit_mensaje("error al hacer click en el boton de iniciar sesion")
  
        try:
            input_correo = WebDriverWait(dr, 10).until(EC.presence_of_element_located((By.XPATH,'//input[@maxlength="50"]')))
        
            sleep(1 + random.randint(0,2))
            input_contraseña = dr.find_element(By.XPATH,'//input[@type="password"]')
            input_correo.send_keys(cuenta["correo"])
            input_contraseña.send_keys(cuenta["password"])
            sleep(1 + random.randint(0,2))
        except:
            imprimit_mensaje("error al ingresar el correo y contraseña")
        #ingresando

        try:
            boton_ingresar_cuenta = dr.find_element(By.XPATH,'//button[@class="button-sign-up primary-btn"]')
            dr.execute_script("arguments[0].click();", boton_ingresar_cuenta)
            i=i+1
        except:
            imprimit_mensaje("Error al hacer click en el boton ingresar")
