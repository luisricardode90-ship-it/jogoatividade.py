import random
pontos=0
soma=0
nome=input("digite o seu nome de usuario:")
sala=input("digite o código da sala{ou crie uma nova sala,Ex;sala54}")
print("""Escolha o nível de dificuldade:"
[1] fácil{1,10 }
[2] médio{1,20}
[3] difícil{1,30}""")

jogar="sim"
while jogar=="sim":
    opcao = int(input("digite o número da opçaõ desejada:"))
    
    limite= 30
    if opcao== 1:
        limite=10
    elif opcao== 2:
        limite=20
    elif opcao == 3:
        limite=30
    numero_sorteado=random.randint(1,limite)
    tentativa=3
    while tentativa>0:
        numero = int(input("Digite seu palpite: "))

        if numero == numero_sorteado:
            print("Você acertou! Parabens!")
        acertou = "Sim"
        pontos+=1
        tentativa =0
        
        
        if tentativa==0:
             print("Você errou! Fim de jogo.")

        if numero<numero_sorteado:
            print("digite um número maior:")
        else:
            print(" digite um número menor:")
        if tentativa > 0:
            print(f"tentativa restante")
            tentativa-=1
            pontos+=pontos
            soma+=pontos
            print(f"Total de pontos:{pontos}")
    
        menu=0
        while menu!=4:
            menu= input("""Escolha uma opcao desejada
            [1] continua jogando
            [2]tente novamente
            [3]salva
            [4]parar
            [5]outras opcões{pontuação,áudio,dificuldade}""")
            if menu == "2":
                tentativa = 3
                break

            if menu == "3":
                print("salvamento concluído!")

            if menu == "4":
                jogar = "não"
                break

            elif menu == "5":
                sub = input("""Outras opções:
            [1] pontuação
            [2] áudio
            [3] dificuldade
            Digite o número da opção: """)
            sub=""
            if sub == "1":
             print(f"Sua pontuação nesta rodada: {pontos} ponto(s).")
            print(f"Soma acumulada de pontos: {soma}")

            if sub == "2":
                print("Opção de áudio ainda não implementada.")

            elif sub == "3":
                print("Para trocar a dificuldade, reinicie o jogo escolhendo outro nível.")

