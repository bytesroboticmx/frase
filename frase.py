#Programa que imprime una frase, letra por letra utilizando la funcion time.sleep
#Autor: Aldo Gonzalez Vazquez
#Licencia: MIT
import time

def imprimeLento(frase):
    for letter in frase:
        print(letter, end='', flush=True)
        time.sleep(0.09)
    print()

def main():
    #word = input("Escribe una frase: ")
    frase = "Nunca desistas, cuando vayan mal las cosas, como a veces suelen ir. Cuando ofrezca tu camino, solo cuesta que subir. Cuando haya poco haber, pero mucho que pagar. Aunque cueste sonreir, aun teniendo que llorar. Cuando ya el dolor te agobie, ya plateadas ya sombrias, descansar acaso debes pero nunca desistir."
    imprimeLento(frase)

if __name__ == '__main__':
    main()
