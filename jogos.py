import adivinhacao
import forca

def escolha_jogo():
    print("\n************************************")
    print("---Bem vindo. Escolha o seu jogo!---")
    print(  "************************************")

    print("\n (1) Forca; (2) Adivinhação.")

    jogo= int(input("Qual jogo?"))

    if jogo==1:
        print("Jogo da Forca.")
        forca.jogar()

    elif jogo==2:
        print("Jogo da Adivinhação.")
        adivinhacao.jogar()

if(__name__ == "__main__"):
    escolha_jogo()

