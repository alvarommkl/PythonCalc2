import random as rd
import os



hits=0
fails=0

def multiplicar(num1, num2):
    
    return num1*num2

def ChooseNumber():
    num=None
    while True:
        os.system('cls')
        try:
            num = input("Tabla a practicar ")
            return int(num)

        except:
            print(f"{num} no es un numero ")
            input("Pulse una tecla para continuar ")




def menu():

    ch=0
    while ch != 1 and ch != 2:
        os.system('cls')
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
            ch = int(input("Seleccione una opcion "))
            if  ch != 1 and ch != 2 and ch !=3 and ch !=4 and ch != 5:
                print("Introduce un numero valido ")
                input("Pulse una tecla para continuar")
            else:
                return ch
        except:
            return 0



def ChooseMul(op, num1):
    num2 = []

    for i in range(1,11):
        if op==1:
            num2.append(i)
        else:
            num2.append(rd.randint(0,10))
    
    for i in num2:
        sol = multiplicar(num1,i)
        try:
            
            comp(sol,int(input(f"{num1} x {i} = ")))
        except:
            comp(sol,0)

    # except:
    #     res=0


def PlayAgain():
    playAgain = True
    playAgain=input("¿Quieres volver a jugar? y/n  \n")
    if playAgain.upper()=='Y' or playAgain.upper() == 'YES' or playAgain.upper() == 'SI' or playAgain.upper()=='S' or playAgain.upper()=='SÍ' or playAgain.upper() == 'YE':
        return playAgain
    else:
        playAgain = False
        return playAgain


def comp(sol, res):

    if sol == res:
        print("Muy bien \n")
        global hits 
        hits += 1
    else:
        print("Muy mal \n")
        global fails
        fails += 1
