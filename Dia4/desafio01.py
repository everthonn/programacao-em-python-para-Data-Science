import statistics
from funcoes_desafio01 import *



inicio = 1
while inicio == 1:
    print('''
consultor de empresas
digite a empresa que deseja visualizar as imformações
0- fechar
1- empresa 1
2- empresa 2 
3- empresa 3 
4- empresa 4
5- empresa 5 
6- ver todas
7- ranking das empresas
''')
    escolha =  input("digite a empresa escolhida")
    match escolha:
        case '1':
            empresa1()
            voltar = input("digite algo para voltar")
        case '2':
            empresa2()
            voltar = input("digite algo para voltar")
        case'3':
            empresa3()
            voltar = input("digite algo para voltar")
        case '4':
            empresa4()
            voltar = input("digite algo para voltar")
        case'5':
            empresa5()
            voltar = input("digite algo para voltar")
        case'6':
            empresa1()
            empresa2()
            empresa3()
            empresa4()
            empresa5()
            voltar = input("digite algo para voltar")
        case'7':
            rankear_empresas(empresas)
            voltar = input("digite algo para voltar")
        case'0':
            break
        case _:
            print("escolha invalida")
            voltar = input("digite algo para voltar")
