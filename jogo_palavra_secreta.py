# Jogo simples de adivinhação de palavra

palavra_secreta = 'camisa'   # Palavra que o jogador precisa adivinhar
letras_acertadas = ''        # Armazena as letras corretas digitadas
numero_tentativas = 0        # Conta o número total de tentativas

while True:
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1          # Incrementa a cada tentativa, certa ou errada

    # Validação, só aceita uma letra por vez
    if len(letra_digitada) > 1:
        print("Digite apenas uma letra!")
        continue

    # Se a letra estiver na palavra secreta, adiciona a lista de acertos
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    # Monta a palavra com * nas letras que ainda não foram descobertas
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    # Mostra o progresso atual da palavra
    print('Palavra formada:', palavra_formada)

    # Verifica se o jogador acertou a palavra inteira
    if palavra_formada == palavra_secreta:
        print('VOCÊ ACERTOU A PALAVRA SECRETA! PARABÉNS!')
        print(f'A palavra era: {palavra_secreta}')
        print('Número de tentativas:', numero_tentativas)
        break
