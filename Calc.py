import ast
from cgitb import reset
import random as rd
import os


hits = 0
fails = 0
total = 0
_hits = 0


def ChooseNumber():
    num = None
    while True:
        os.system("cls")
        try:

            num = []
            # cont=0
            cadena = input("Tablas a practicar ")
            cadena = cadena.strip()
            cadena = cadena.split(" ")

            for i in range(len(cadena)):
                # cont
                cad_mul = cadena[i]

                num.append(int(cad_mul))

                # cont=cont + 1

            return num
        except:
            print(f"{cad_mul} No es un numero")
            input("Pulsa una tecla para continuar")


def menu():

    choice = 0
    while choice != 1 and choice != 2:
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
            if (
                choice != 1
                and choice != 2
                and choice != 3
                and choice != 4
                and choice != 5
            ):
                print("Introduce un numero valido ")
                input("Pulse una tecla para continuar")
            else:
                return choice
        except:
            return 0


def FillNumber(option):
    mulTable2 = []

    for i in range(1, 11):
        if option == 1:
            mulTable2.append(i)
        else:
            mulTable2.append(rd.randint(1, 10))
            if i != 1 and mulTable2[i - 1] == mulTable2[i - 2]:
                mulTable2[i - 1] = rd.randint(1, 10)
    return mulTable2


def ChooseMul(option, mulTable1):
    for mul1 in mulTable1:
        mulTable2 = FillNumber(option)
        for mul2 in mulTable2:
            solution = mul1 * mul2
            try:

                comp(solution, int(input(f"{mul1} x {mul2} = ")), mul1)
            except:
                comp(solution, 0, mul1)

    # except:
    #     res=0


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


def comp(solution, res, multTable):
    global hits
    global fails
    _porc = 0
    global total
    global score
    global _hits

    if solution == res:
        print("Muy bien \n")
        total += 1
        hits += 1
        _hits += 1
    else:
        print("Muy mal \n")
        total += 1
        fails += 1

    if total % 10 == 0:
        _porc = (_hits / total) * 100
        score[f"Tabla {multTable}"] = f"{_porc}%"
        print("Resultado guardado con exito")
        _hits = 0
        total = 0


# hits = 15   total = 20    _total= 2        10-(10/1) = 15-10 = 0


def Eval():
    os.system("cls")
    print("*****************************")
    for clave, valor in score.items():
        if clave == "Tabla 10":
            print(f"*    {clave} : {valor}            *")
        else:
            print(f"*    {clave} : {valor}             *")

    print("*****************************")


# Formato JSON


def ResetScore(_score):
    for i in range(1, 11):
        _score[f"Tabla {i}"] = ""

    return _score


def SaveScore(_score):
    tf = open("Score.JSON", "w")
    tf.write(str(_score))
    tf.close()


def ReadScore(_score):
    tf = open("Score.txt", "r")
    _score = tf.read()
    ast.literal_eval(_score)
    tf.close()
    return _score


# Main

score = {}
try:
    score = ReadScore(score)
except:
    score = ResetScore(score)


comprobation = True
playAgain = False
while comprobation:
    if playAgain == False:
        option = menu()
    if option == 1 or option == 2:
        mulTable = ChooseNumber()
        ChooseMul(option, mulTable)
        print(f"Has tenido {hits} aciertos y {fails} fallos")
        playAgain = PlayAgain()
    elif option == 3:
        Eval()
        input("\nPulsa una tecla para continuar")
    elif option == 4:
        ResetScore()
        input("\nPulsa una tecla para continuar")
    elif option == 5:
        SaveScore(score)
        comprobation = False
        comprobation
