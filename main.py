from modules.create_instances import create_instances
from modules.utilities import send_drivers_to_link, close_drivers
from modules.temas import seleccionar_tema_comentar
from modules.imprimir_comentarios import encotrar_caja_texto_enviar_mensaje
from modules.identificarse import identificarse_en_trovo
import random
import os
import json

def run():

    while True:
        instances = int(input("Número de bots (entre 1 y 6): ").strip())

        if instances > 6:
            print("Ingresa un número válido")
            continue

        if instances < 1:
            print("Ingresa un número válido")
            continue
        break


    drivers = create_instances(instances)
    link_trovo = "https://trovo.live/"
    send_drivers_to_link(drivers, link_trovo)
    identificarse_en_trovo(drivers)

    while True:
        comando = str(input(""" 


            Ingresa un comando

            "T" para seleccionar el tema a comentar

            "L" para ir al Live

            "C" para cerrar todas las ventanas

        """)).strip().upper()



        if comando=="L":
            ruta_live = os.path.join(os.path.abspath(''),'live.json')
            with open(ruta_live) as contenido:
                link = json.load(contenido)

            link_live = link[0]["link"]
            send_drivers_to_link(drivers, link_live)

                

        elif comando=="T":
            comentarios = seleccionar_tema_comentar()
            comentarios = comentarios[::-1]


            driver_seleccionado = random.choice(drivers)


            for i in range(0,len(comentarios)):
                driver_seleccionado = random.choice(drivers)
                comentario_seleccionado = comentarios.pop()
                encotrar_caja_texto_enviar_mensaje(driver_seleccionado,comentario_seleccionado)    
                

        elif comando=="C":
            close_drivers(drivers)
            break

        else:
            print("Comando incorrecto")



if __name__ == '__main__':
    run()