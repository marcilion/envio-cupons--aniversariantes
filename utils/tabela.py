def montar_linha(valores: list[str], eh_cabecalho: bool = False, largura_coluna: int = 20):
    if len(valores) == 0:
        return ""
    
    linha = ""
    largura_borda = -1
    for valor in valores:
        valor_coluna = f"| {valor}"

        if len(valor_coluna) < largura_coluna:
            diferenca = largura_coluna - len(valor_coluna)
            valor_coluna += " " * diferenca
        elif len(valor_coluna) > largura_coluna:
            valor_coluna = valor_coluna[largura_coluna]

        largura_borda += len(valor_coluna)
        linha += valor_coluna

    linha += "|"
    if eh_cabecalho == False:
        return linha

    borda_cima = " " + ("_" * largura_borda)
    borda_baixo = " " + ("¨" * largura_borda)

    linha = f"{borda_cima}\n{linha}\n{borda_baixo}"
    return linha
            

print(montar_linha(["coluna 1", "coluna 2", "coluna 3"], eh_cabecalho=True))