import random

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhaç2ão!")
    print("*********************************")
    pontos_restantes=1000
    numero_secreto = random.randrange(1,101)
    total_de_tentativas=0
    print("Niveis de dificuldade")
    print("[1]facil [2]Medio [3]Dificil")
    nivel=int(input("Escolha seu nivel de difilcutade: "))
    if (nivel == 1):
        total_de_tentativas = 7
    elif (nivel == 2):
        total_de_tentativas = 5
    elif (nivel == 3):
        total_de_tentativas = 3
    for rodada in range(1,total_de_tentativas+1):
        print("Tentativas {} de {}".format(rodada,total_de_tentativas))
        chute_str = input("Digite o seu número: ")
        print("Você digitou " , chute_str)
        chute = int(chute_str)
        pontos_restantes =pontos_restantes - chute
        #print(numero_secreto)
        if chute<1 or chute>100:
                print("Voce deve digitar um numero entra 1 e 100 ")
                print("Perdeu uma rodada")
                print(f"Ponto Atuais: {pontos_restantes}!!!")
                continue
        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            pontos_restantes = pontos_restantes + chute
            print("Parabéns! Você acertou!")
            print(f"E terminou com {pontos_restantes}!!! Pontos!!!!")

            break
        else:
            if(maior):
                print("O seu chute foi maior do que o número secreto!")
                print(f"Pontos Atuais {pontos_restantes}!!!!")
            elif(menor):
                print("O seu chute foi menor do que o número secreto!")
                print(f"Pontos Atuais {pontos_restantes}!!!")



    print("Fim do jogo")
    if (__name__ == "__main__"):
        jogar()