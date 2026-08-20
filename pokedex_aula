import random

#Declarando variáveis para gerar um número aleatório
numero_secreto = random.randint(1,100)
tentativas = 0 
acertou = False 

#Laço de repetição com condição boleana 

while not acertou:
    palpite = int(input("Digite um número entre 1 e 100:"))
    tentativas  += 1

    if palpite < numero_secreto:
        print("Muito abaixo")
    elif palpite > numero_secreto:
        print("Muito acima")
    else:
        print (f'Parabéns! Acertou em {tentativas} tentativas.')
        acertou = True
