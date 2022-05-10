import os


def menu():
    while True:
        os.system("cls")
        print("********************************************")
        print("*   Seleccione el modo que desee repasar   *")
        print("********************************************")
        print("*     1. Tabla/s de multiplicar            *")
        print("*     2. Multiplicacion aleatoria          *")
        print("*     3. Evaluacion                        *")
        print("*     4. Resetear puntuacion               *")
        print("*     5. Salir                             *")
        print("********************************************")
        try:
            choice = int(input("Seleccione una opcion "))
            if (not (choice >=1 and choice <=5)):
                print("Introduce un numero valido ")
                input("Pulse una tecla para continuar")
            else:
                return choice
        except:
            return 0


def PlayAgain():
    playAgain = True
    playAgain = input("¿Quieres volver a jugar? y/n  \n")
    if (
        playAgain.upper() == "Y"
        or playAgain.upper() == "YES"
        or playAgain.upper() == "SI"
        or playAgain.upper() == "S"
        or playAgain.upper() == "SÍ"
        or playAgain.upper() == "YE"
    ):
        return playAgain
    else:
        playAgain = False
        return playAgain
