import ast
import json
import os

# Formato JSON

def ResetScore(_score):
    for i in range(1, 11):
        _score[f'Tabla {i}'] = ''

    return _score


def SaveScore(_score):
    with open("socre.json", "w+") as f:
        f.write(json.dumps(_score))


def ReadScore(_score):
    tf = open("Score.txt", "r")
    _score = tf.read()
    ast.literal_eval(_score)
    tf.close()
    return _score


def recordPunctuation(_score:dict , _porc ,tablasMultiplicar):
    for i in tablasMultiplicar:
        _score[f'Tabla {i}']=f'{_porc}%'
    return _score




def eval(_score:dict):
    os.system("cls")
    print("*****************************")
    for clave, valor in _score.items():
        print(f"{clave} : {valor}")
    print("*****************************")
    # return _score

