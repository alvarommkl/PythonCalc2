from Calc import *
from menu import *
from Score import *





#To do, mirar el tema de las variables de hits fails score... etc





#Declaracion de variables

comprobation = True
playAgain = False
score :dict= {}
correctAnswers = 0
failedAnswers = 0


# Main

#Lee la puntuacion si existe el archivo, si no rellena el diccionario
try:
    score = ReadScore(score)
except:
    score = ResetScore(score)


#Empieza el programa, el comprobation es para que no pongan un numero que no este en el menu.



while comprobation:
    #playAgain es por si quieres volver a jugar o empezar el test de nuevo con distintas tablas.
    if playAgain == False:
        option = menu()


    #Opcion 1 = Multiplicacion en serie, Opcion 2 = Multiplicacion random
    if option=='Multiplicacion Normal' or option == 'Multiplicacion Random':
        multTable = ChooseMultTable()
        correctAnswers , failedAnswers, score = StartTest(option, multTable,score)
        print(f"Has tenido {correctAnswers} aciertos y {failedAnswers} fallos")
        input("\nPulsa intro para continuar ")
        playAgain = PlayAgain()
        
        

    #Opcion 3 = Muestra resultados
    elif option == 'Mostrar Puntuacion':
        eval(score)
        input("\nPulsa una tecla para continuar")


    #Opcion 4 = Resetea resultados
    elif option == 'Resetear Puntuacion':
        score=ResetScore(score)
        input("\nPulsa una tecla para continuar")


    #Opcion 5 = Salir programa
    elif option == 'Salir':
        SaveScore(score)
        comprobation = False

