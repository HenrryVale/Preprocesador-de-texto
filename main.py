


def validar_solo_letras(cadena):
    letras_permitidas = "áéíóúÁÉÍÓÚñÑabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ \n"
    resultado = ''.join(c for c in cadena if c in letras_permitidas)
    return resultado

def validar_txt(file):
    with open(file, 'r', encoding="UTF-8") as file:
        #Poner a minusculas
        contenido = file.read().lower()
        #valida solo letras
        nuevo_contenido = validar_solo_letras(contenido)
        #Tokenizar 
        nuevo_contenido_tokenizado = nuevo_contenido.split()
        return nuevo_contenido_tokenizado #print(nuevo_contenido_tokenizado)

texto_a_procesar = validar_txt('raw-text.txt')
stop_words = validar_txt('stop-words.txt')
#Filtar stop-words
resultado = [token for token in texto_a_procesar if token not in stop_words]

#Crear archivo processed-text.txt
with open('processed-text.txt', 'w', encoding='utf-8') as file:
        file.write(str(resultado))