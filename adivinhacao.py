def mensagem_inicial():
    print("\n*********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("*********************************\n")
    print("Neste jogo, o seu objetivo é adivinhar qual o número secreto, \n"
          "no menor número de tentativas possível. "
          "O número está entre 1 e 100 e você começa o jogo com 1000 pontos. \n"
          "A cada chute errado, o valor do seu chute é reduzido de sua pontuação. \n"
          "Você tem 3 níveis de dificuldade: \n"
          "(1) Fácil: 50 chutes \n"
          "(2) Médio: 25 chutes \n"
          "(3) Difícil: 5 chutes \n"
          "Boa sorte!!!\n")
def jogar():
    import random
    mensagem_inicial()
    numero_secreto= random.randrange(1,101)
    rodada= 1
    pontos= 1000

    print("\nEscolha o nível de dificuldade: 1. Fácil; 2. Médio; 3. Difícil.")
    nivel= int(input("Nível selecionado: "))

    if nivel==1:
        total_tentativas= 50
    elif nivel==2:
        total_tentativas= 25
    elif nivel==3:
        total_tentativas= 5

    while (rodada <= total_tentativas):
        print("\nTentativa {} de {}". format(rodada, total_tentativas))
        chute = int(input("\nDigite o seu número: "))
        print("\nVocê digitou ", chute)

        acertou = (numero_secreto == chute)
        errou_menor = (numero_secreto < chute)
        errou_maior = (numero_secreto > chute)

        if (acertou):
            print("Você acertou, parabéns!!")
            break
        else:
            if errou_menor:
                print("Você errou. O número secreto é menor. Tente novamente!")
            elif errou_maior:
                print("Você errou. O número secreto é maior. Tente novamente!")
            pontos_perdidos= abs(numero_secreto - chute)
            pontos= pontos - pontos_perdidos
            print("Sua pontuação está em {}". format(pontos))
        rodada= rodada + 1

    print("\nFim de jogo!")
    print("Sua pontuação foi {}.".format(pontos))
    print("\nO número secreto era {}.". format(numero_secreto))

if(__name__ == "__main__"):
    jogar()