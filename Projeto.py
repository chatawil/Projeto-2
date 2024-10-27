def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []
    if orientacao == "vertical":
        for i in range(tamanho):
            posicoes.append([linha + i, coluna])
    elif orientacao == "horizontal":
        for i in range(tamanho):
            posicoes.append([linha, coluna + i])
    return posicoes

def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    posicoes_navio = define_posicoes(linha, coluna, orientacao, tamanho)
    if nome_navio in frota:
        frota[nome_navio].append(posicoes_navio)
    else:
        frota[nome_navio] = [posicoes_navio]
    return frota

def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = "X"  
    else:
        tabuleiro[linha][coluna] = "-"  
    return tabuleiro
def posiciona_frota(frota):
    tabuleiro = [[0 for _ in range(10)] for _ in range(10)]
    
    for navio, lista_de_posicoes in frota.items():
        for posicoes in lista_de_posicoes:
            for linha, coluna in posicoes:
                tabuleiro[linha][coluna] = 1
    return tabuleiro