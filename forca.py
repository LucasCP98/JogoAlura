

def jogar():
    print("Bem-vindo ao jogo da Forca, você tem 6 tentativas.")

    # Mude a palavra aqui
    palavra_secreta = "cachorro"
    tamanho_palavra_secreta = len(palavra_secreta)
    armazena_qtd_letras = []
    for palavra_secreta in range(tamanho_palavra_secreta):
        armazena_qtd_letras.insert(palavra_secreta, "_")
    print("a palavra tem: ", armazena_qtd_letras)

    # Mude a palavra aqui
    palavra_secreta = "cachorro".upper()
    letras_acertadas = armazena_qtd_letras

    enforcou = False
    acertou = False
    tentativas = 0

    # Enquanto enforcou e acertou "NÃO" for verdadeiro, continuará no loop até que seja verdadeiro.
    while not enforcou and not acertou:

        chute = str(input("Para jogarmos, chute uma letra: ")).upper().strip()

        if chute in palavra_secreta:
            for i, palavra in enumerate(palavra_secreta):
                if chute == palavra:
                    letras_acertadas[i] = palavra

        else:
            tentativas += 1

        print(letras_acertadas)
        enforcou = tentativas == 6
        if enforcou and "_" in letras_acertadas:
            print("Infelizmente você perdeu o jogo, tente a sorte na proxima vez")

        elif not enforcou and "_" not in letras_acertadas:
            print("*** AEEEEEEEEEEEEEEEE, Parabéns você ganhou o jogo ***")
            break

        else:
            continue


if __name__ == "__main__":
    jogar()

