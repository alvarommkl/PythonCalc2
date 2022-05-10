import os
import random as rd
from Score import recordPunctuation




def ChooseMultTable():
    while True:
        os.system("cls")
        try:

            num = []
            cadena = input("Tablas a practicar ")
            cadena = cadena.strip()
            cadena = cadena.split(" ")

            for i in range(len(cadena)):
                cad_mul = cadena[i]

                num.append(int(cad_mul))


            return num
        except:
            print(f"{cad_mul} No es un numero")
            input("Pulsa una tecla para continuar")








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







def StartTest(option, mulTable1,_score):
    responseUser=0
    correctAnswers = 0
    failedAnswers = 0
    temp = 0
    for mul1 in mulTable1:
        mulTable2 = FillNumber(option)
        for mul2 in mulTable2:
            solution = mul1 * mul2
            try:

                responseUser = int(input(f"{mul1} x {mul2} = "))
            except:
                responseUser=0

            if solution == responseUser:
                print("Muy bien \n")
                correctAnswers += 1
                temp += 1
            else:
                print("Muy mal \n")
                failedAnswers += 1
        porcentage=(temp/10)*100
        _score=recordPunctuation(_score,porcentage,mulTable1)
        temp=0
    return correctAnswers, failedAnswers , _score










# def comp(solution, res, multTable):
#     global hits
#     global fails
#     _porc = 0
#     global total
#     global score
#     global _hits







#     if total % 10 == 0:
#         _porc = (_hits / 10) * 100
#         score[f"Tabla {multTable}"] = f"{_porc}%"
#         print("Resultado guardado con exito")
#         _hits = 0
#         total = 0

