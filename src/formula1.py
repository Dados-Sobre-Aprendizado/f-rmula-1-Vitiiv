print("Simulador de Pontuação da Fórmula 1!")

while True:
    print("\nDigite o número de Grandes Prêmios (G) e o número de pilotos (P), separados por espaço:")
    entrada = input("(Ou digite '0 0' para sair) > ").strip()
    G, P = map(int, entrada.split())

    if G == 0 and P == 0:
        print("Encerrando o programa. Até mais!")
        break


    resultados = []
    print(f"\nOk! Vamos registrar os resultados das {G} corridas.")
    for corrida in range(1, G + 1):
        print(f"Digite a ordem de chegada dos {P} pilotos na corrida {corrida} (posições separadas por espaço):")
        chegada = list(map(int, input("> ").split()))
        resultados.append(chegada)

    print("\nAgora, informe a quantidade de sistemas de pontuação que deseja simular:")
    s = int(input(" Quantidade de sistemas > "))


    sistemas = []
    for sistema_num in range(1, s + 1):
        print(f"\nDigite o sistema de pontuação {sistema_num}:")
        dados = list(map(int, input("Comece digitando a quantidade de posições que recebem pontos, seguida dos pontos para cada posição (ex: '3 10 5 1'):").split()))
        sistemas.append(dados)


    print("\nRESULTADOS:")
    for indece, sistema in enumerate(sistemas, start=1):
        K = sistema[0]
        pontuacoes = sistema[1:]
        pontos = [0] * P

        for corrida in resultados:
            for piloto_id in range(P):
                posicao = corrida[piloto_id]
                if posicao <= K:
                    pontos[piloto_id] += pontuacoes[posicao - 1]

        maior_pontuacao = max(pontos)
        campeoes = []
        for i in range(P):
            if pontos[i] == maior_pontuacao:
                campeoes.append(str(i + 1))

        print(f"\nSistema de Pontuação {indece}:")
        print(f"Pontuação final dos pilotos: {pontos}")
        print(f"Campeão(ões): {' '.join(campeoes)}")

print("\nObrigado por usar o simulador!")
