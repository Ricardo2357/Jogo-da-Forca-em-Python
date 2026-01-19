import random
import sys

def terminal_inicial(palavra, tentativas, letras_tentadas):
    verificacao = verificar_acertos(palavra, letras_tentadas)

    print("Bem-vindo ao Jogo da Forca!\n")
    print("\n")
    print(f"Palavra: {verificacao}")
    print("\n")
    print(f"Tentativas restantes: {tentativas}")
    print("Letras tentadas: Nenhuma")
    print("\n")

    return validar_input()

def terminal_acerto(letra, palavra, tentativas, letras_tentadas):
    verificacao = verificar_acertos(palavra, letras_tentadas)

    letras_formatadas = ", ".join(letras_tentadas)

    print(f"Boa! A letra '{letra}' está na palavra.\n")
    print("\n")
    print(f"Palavra: {verificacao}")
    print("\n")
    print(f"Tentativas restantes: {tentativas}")
    print(f"Letras tentadas: {letras_formatadas}")
    print("\n")

    return validar_input()

def terminal_erro(letra, palavra, tentativas, letras_tentadas):
    verificacao = verificar_acertos(palavra, letras_tentadas)

    letras_formatadas = ", ".join(letras_tentadas)

    print(f"A letra '{letra}' não está na palavra.\n")
    print("\n")
    print(f"Palavra: {verificacao}")
    print("\n")
    print(f"Tentativas restantes: {tentativas}")
    print(f"Letras tentadas: {letras_formatadas}")
    print("\n")

    return validar_input()

def validar_input():
    while True:
        letra = input("Digite uma letra: ")
        if len(letra) != 1:
            print("Erro! Não se pode digitar mais de um caractere.")
            print("\n")
        elif not letra.isalpha():
            print("Erro! Apenas é permitido caracteres alfabéticos.")
            print("\n")
        else:
            return letra

def verificar_acertos(palavra, letras_tentadas):
    palavra_secreta = []
    for caractere in palavra:
        if caractere in letras_tentadas:
            palavra_secreta.append(caractere)
        else:
            palavra_secreta.append("_")
    return " ".join(palavra_secreta)

def vitoria(palavra, letras_tentadas):

    verificacao = verificar_acertos(palavra, letras_tentadas)

    if "_" not in verificacao:
        print (f"Parabéns! Você acertou a palavra: {palavra}")
        return True
    return False

def derrota(tentativas, palavra):
    if tentativas == 0:
        print(f"Fim de jogo! A palavra era: {palavra}")
        return True
    return False

try: 
    arquivo = open("words.txt", "r")

    linhas = arquivo.readlines()

    if not linhas:
        print("Erro! O arquivo está vazio.")
        sys.exit()

    palavra = random.choice(linhas).strip()

    tentativas = 6
    letras_tentadas = []

    jogada = terminal_inicial(palavra, tentativas, letras_tentadas)

    while True:
        letras_tentadas.append(jogada)

        if jogada in palavra:
            if vitoria(palavra, letras_tentadas):
                break
            jogada = terminal_acerto(jogada, palavra, tentativas, letras_tentadas)
        else:
            tentativas -= 1
            if derrota(tentativas, palavra):
                    break
            jogada = terminal_erro(jogada, palavra, tentativas, letras_tentadas)

    arquivo.close()
except:
    print("Erro! O arquivo não existe.")