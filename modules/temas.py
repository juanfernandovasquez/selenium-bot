import json
import os

def seleccionar_tema_comentar():

    root = os.path.abspath('')
    ruta = os.path.join(root, 'temas.json')

    temas = []
    with open(ruta) as contenido:
        temas = json.load(contenido)

    temas_disponibles= []
    for tema in temas:
        temas_disponibles.append(tema["titulo"])


        
    print("Las temáticas disponibles son las siguientes:")
    print(" ")
    print(" ")

    i = 0
    # tematicas = {}
    for _ in temas_disponibles:
        print( f'{i}.- {_}')
        i=i+1 

    print(" ")
    print(" ")
    


    while True:

        tema_idx = int(input("""
        
        Elige una tema (numero de índice):
        
        """))
        
        if tema_idx < 0:
            print("Ingresa un número correcto")

        elif tema_idx >= i:
            print("Ingresa un número correcto")

        break

    comentarios = temas[tema_idx]["comentarios"]
    
    return comentarios