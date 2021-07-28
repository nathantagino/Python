#funções : recebe parametros (valores), realiza um processo e entrega um resultado
#principal obj: não precisar reescrever várias vezes um mesmo processo, quebrar o  código em pequenas partes
#def: define uma função
import math
def somar(x,y):
    return x + y

def subtrair(x,y):
    return x - y

def multiplicar(x,y):
    return x * y

def dividir(x,y):
    return x / y

def elevar(x,y):
    return x**y

def baskara(a,b,c,delta):
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    if not(x1 == x2):
        print(" o valor de x1 corresponde a:", x1)
        print(" o valor de x2 corresponde a: ", x2)
    else:
        print("As raizes são iguais e correspondem a: ",x1)

def continuar_operacao(resposta):
    if  not resposta == "s":
        resposta = "n"
        return resposta
def continuar_programa(repetir):
    if not repetir == "s":
        repetir = "n"
        return repetir
    

    

print("Olá visitante, me chamo Jarvis, serei seu assistente matemático! Antes de começarmos que tal me dizer seu nome?")
nome_usuario=input("Nome ou apelido: ")
print("Bem vindo(a) ",nome_usuario,", agora sim podemos começar! ")
print("Primeiro eu preciso que me informe que tipo de operação faremos hoje, temos as seguintes opções :")
operacoes =['adição','subtração','multiplicação','divisão', 'potenciação' , 'báskara']
print(operacoes)
repetir = "s"
while repetir =="s":
    escolha = input("Digite a operação escolhida ou z para cancelar: ")
    resposta = "s"

    while resposta =="s":
            if escolha == "adição":
                x=float(input("Por favor, digite o valor x: "))
                y=float(input("Por gentileza, agora digite o valor y: "))
                print("O valor corresponde a: ",somar(x,y))
                resposta=input(" deseja continuar somando ? s/n: ")
                

            if escolha == "subtração":
                x=float(input("Por favor digite o valor do primeiro número: "))
                y=float(input("Por favor digite o valor do segundo número: "))
                print("O valor corresponde a: ", subtrair(x,y))
                resposta=input(" deseja continuar subtraindo ? s/n: ")

            if escolha == "multiplicação":
                x=float(input("Por favor digite o valor do primeiro número: "))
                y=float(input("Por favor digite o valor do segundo número: "))
                print("O valor corresponde a: ", multiplicar(x,y))
                resposta=input(" deseja continuar multiplicando ? s/n: ")

            if escolha == "divisão":
                x=float(input("Por favor digite o valor do dividendo : "))
                y=float(input("Por favor digite o valor do divisor : "))
                print("O valor corresponde a: ", dividir(x,y))
                resposta=input(" deseja continuar dividindo ? s/n: ")
                
            if escolha == "potenciação":
                x=float(input("Por favor digite o valor da base da potência: "))
                y=float(input("Por favor digite o valor do expoente: "))
                print("A potência corresponde a :", elevar(x,y))
                resposta=input(" deseja continuar elevando ? s/n: ")

            if escolha == "báskara":
                a = float(input("A: "))
                b = float(input("B: "))
                c = float(input("C: "))
                delta=(b**2)-(4*a*c)
                print("O valor do Delta corresponde a: ", delta)
                if (delta<0):
                    print("Essa equação não possui raizes no conjunto dos números reais.")
                    resposta=input(" deseja realizar outra operação de báskara ? s/n: ")
                else:
                    print("Agora vamos encontrar o valor de x1 e x2!")
                    print(baskara(a,b,c,delta))
                    resposta=input(" deseja realizar outra operação de báskara ? s/n: ")
            if escolha == "z":
                resposta = "n"
                

    repetir=input(("Deseja efetuar outra operação? s/n :"))
print("")
print("Obrigado por utilizar o programa,",nome_usuario,"!!!!")
input()
