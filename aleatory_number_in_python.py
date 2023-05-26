import random 

def Fazer_numero_aleatorio():
    
    numero_aleatorio = random.randint(1,5)
    return numero_aleatorio

def ler_player():
    p1 = 0
    p2 = 0

    while p1 < 1 or p1 > 5:
        p1 = int(input("p1 - escolha um número entre 1 a 5: "))
        if p1 < 1 or p1 > 5:
            print("Número inválido! Por favor, escolha um número entre 1 e 5.")

    while p2 < 1 or p2 > 5:
        p2 = int(input("p2 - escolha um número entre 1 a 5: "))
        if p2 < 1 or p2 > 5:
            print("Número inválido! Por favor, escolha um número entre 1 e 5.")

    return p1, p2
  
def Quem_ganhou(numero_aleatorio, p1, p2):
    
    print("O número escolhido é:", numero_aleatorio)
    if p1 == p2 == numero_aleatorio:
        print("Os dois escolheram o mesmo número e empataram!")
    elif p1 == p2:
        print("Os dois escolheram o mesmo número, mas não acertaram!")
    else:
        if p1 == numero_aleatorio:
            print("P1 ganhou!")
        elif p2 == numero_aleatorio:
            print("P2 ganhou!")
        else:
            print("Nenhum ganhou")

def main():
   p1, p2 = ler_player()
   numero_aleatorio = Fazer_numero_aleatorio()
   Quem_ganhou(numero_aleatorio, p1, p2)
    
main()
