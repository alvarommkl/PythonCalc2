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
            
            num=[]
            # cont=0
            cadena=input("Tablas a practicar ")
            cadena = cadena.split(" ")

            for i in range(len(cadena)):
                # cont
                cad_mul = cadena[i]
                num.append(int(cad_mul))
                
                # cont=cont + 1
                
            return num
        except:
            print(f"{num} No es un numero")
            input("Pulsa una tecla para continuar")




def menu():

    choice=0
    while choice != 1 and choice != 2:
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
            choice = int(input("Seleccione una opcion "))
            if  choice != 1 and choice != 2 and choice !=3 and choice !=4 and choice != 5:
                print("Introduce un numero valido ")
                input("Pulse una tecla para continuar")
            else:
                return choice
        except:
            return 0


def FillNumber(option):
    mulTable2 = []

    for i in range(1,11):
        if option==1:
            mulTable2.append(i)
        else:
            mulTable2.append(rd.randint(1,10))
            if (i != 1 and mulTable2[i-1]==mulTable2[i-2]  ):
                mulTable2[i-1]=rd.randint(1,10)
    return mulTable2


def ChooseMul(option, mulTable1):
    for mul1 in mulTable1:
        mulTable2 = FillNumber(option)
        for mul2 in mulTable2:
            solution = multiplicar(mul1,mul2)
            try:
                
                comp(solution,int(input(f"{mul1} x {mul2} = ")))
            except:
                comp(solution,0)

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


def comp(solution, res):

    if solution == res:
        print("Muy bien \n")
        global hits 
        hits += 1
    else:
        print("Muy mal \n")
        global fails
        fails += 1




#Main
comprobation=True
playAgain=False
while comprobation:
    if playAgain == False:
        option=menu()
    if option == 1 or option ==2:
        mulTable=ChooseNumber()
        ChooseMul(option,mulTable)
        print(f"Has tenido {hits} aciertos y {fails} fallos")
        playAgain=PlayAgain()
    elif option==3:
        print("Aqui irian los resultados")
        input()
    elif option==4:
        print("Aqui se resetearian las puntuaciones")
        input()
    elif option==5:
        comprobation = False