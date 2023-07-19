import random


class JogoAlura:

    def __init__(self):
        self.listando_palavras_secretas = []
        self.enforcou = False
        self.acertou = False
        self.tentativas = 0

    def jogo_da_forca(self):

        print("Bem-vindo ao jogo da Forca, você tem 12 tentativas.")

        # Abrindo o arquivo que contém a listagem das palavras que serão usadas no jogo.
        arquivos = open("palavras.txt", mode="r", encoding="UTF-8")

        # Passando por cada item dentro do arquivo: "palavras.txt e adiconando dentro de uma lista."
        for arquivo in arquivos:
            self.listando_palavras_secretas.append(arquivo)

        # Gerando uma palavra aleatoria com a biblioteca random, para ser usada no jogo.
        palavra_aleatoria = random.choice(self.listando_palavras_secretas)
        print(palavra_aleatoria)

        # Recebe a palavra e trata ela retirando os espaços e transformando todos em Maiusculas.
        palavra_secreta = str(palavra_aleatoria).upper().strip()

        # List comprehension, para adicionarmos "_" dentro da "palavra_secreta".
        letras_acertadas = ["_" for letra in palavra_secreta]

        return palavra_secreta, letras_acertadas

    def loop_jogo(self):

        # Variaveis retornadas pela função jogo_da_forca()
        palavra_secreta, letras_acertadas = self.jogo_da_forca()

        # Enquanto enforcou e acertou "NÃO" for verdadeiro, continuará no loop até que seja verdadeiro.
        while not self.enforcou and not self.acertou:

            # Chute recebe uma letra, formata a letra e verifica se a letra está dentro da palavra secreta.
            chute = str(input("Para jogarmos, chute uma letra para tentar adivinhar a palavra: ")).upper().strip()
            if chute in palavra_secreta:

                # Passamos por todas as letras e verificamos se a letra é igual a letra.
                for i, letra in enumerate(palavra_secreta):
                    if chute == letra:
                        letras_acertadas[i] = letra

            else:
                # Tentativas caso a letra não esteja na palavra, soma uuma tentativa errada.
                self.tentativas += 1
                print(f"Você errou a {self.tentativas}˚ tentativa.")

            # Str_letras transdorma a list em str para formatação com replace da palavra.
            str_letras = str(letras_acertadas).replace("[", "").replace("]", "").replace("'", "").replace(",", " ")
            print(str_letras)

            # Enforcou verifica se as tentativas são igual a 12 e "_" possui dentro da lista, caso seja finaliza o jogo.
            self.enforcou = self.tentativas == 12
            if self.enforcou and "_" in letras_acertadas:
                print("Infelizmente você perdeu o jogo, tente a sorte na proxima vez.")

            # Verifica se enforcou é false e "_" possui dentro da lista, caso sim o jogador vence.
            elif not self.enforcou and "_" not in letras_acertadas:
                print("*** Parabéns você ganhou o jogo ***")
                break

            # Caso nenhuma das verificações sejam satisfeita, continue o loop.
            else:
                continue


if __name__ == "__main__":
    start = JogoAlura()
    start.loop_jogo()
