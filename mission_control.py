NOME_MISSAO = "New Era"
NOME_EQUIPE = "Equipe Alpha"

dados_missao = [
    [22, 95, 91, 98, 93],
    [26, 84, 77, 95, 82],
    [33, 61, 54, 90, 68],
    [37, 44, 31, 85, 48],
    [41, 22, 14, 76, 29],
    [35, 50, 28, 81, 45],
]

areas_monitoradas = [
    "Temperatura interna",
    "Comunicação com a base",
    "Sistema de energia",
    "Suporte de oxigênio",
    "Estabilidade operacional",
]


def analisar_temperatura(valor):
    if valor < 18:
        return "ATENÇÃO", "Temperatura baixa demais", 1
    elif valor <= 30:
        return "NORMAL", "Temperatura estável", 0
    elif valor <= 35:
        return "ATENÇÃO", "Temperatura elevada", 1
    return "CRÍTICO", "Risco de superaquecimento", 2


def analisar_comunicacao(valor):
    if valor < 30:
        return "CRÍTICO", "Comunicação com a base em nível crítico", 2
    elif valor < 60:
        return "ATENÇÃO", "Comunicação instável", 1
    return "NORMAL", "Comunicação estável", 0


def analisar_bateria(valor):
    if valor < 20:
        return "CRÍTICO", "Bateria em nível crítico", 2
    elif valor < 50:
        return "ATENÇÃO", "Bateria abaixo do recomendado", 1
    return "NORMAL", "Energia estável", 0


def analisar_oxigenio(valor):
    if valor < 80:
        return "CRÍTICO", "Oxigênio em nível crítico", 2
    elif valor < 90:
        return "ATENÇÃO", "Oxigênio abaixo do ideal", 1
    return "NORMAL", "Oxigênio adequado", 0


def analisar_estabilidade(valor):
    if valor < 40:
        return "CRÍTICO", "Estabilidade operacional crítica", 2
    elif valor < 70:
        return "ATENÇÃO", "Estabilidade operacional reduzida", 1
    return "NORMAL", "Estabilidade operacional adequada", 0


def classificar_ciclo(pontuacao):
    if pontuacao <= 2:
        return "MISSÃO ESTÁVEL"
    elif pontuacao <= 5:
        return "MISSÃO EM ATENÇÃO"
    return "MISSÃO CRÍTICA"


def gerar_recomendacao(resultados, pontuacao_total):
    status_list = [r[0] for r in resultados]
    criticos = status_list.count("CRÍTICO")

    if criticos >= 3:
        return "Ativar modo de segurança e priorizar suporte à vida, energia e comunicação."

    if status_list[0] == "CRÍTICO":
        return "Verificar controle térmico da missão."
    if status_list[1] == "CRÍTICO":
        return "Tentar restabelecer contato com a base."
    if status_list[2] == "CRÍTICO":
        return "Ativar modo de economia de energia."
    if status_list[3] == "CRÍTICO":
        return "Acionar protocolo de suporte à vida."
    if status_list[4] == "CRÍTICO":
        return "Reduzir operações não essenciais."

    if pontuacao_total >= 3:
        return "Monitorar sistemas em atenção e preparar plano de contingência."

    return "Manter operação normal e continuar monitoramento."


def analisar_tendencia(inicial, final):
    if final > inicial:
        return "A missão apresentou tendência de piora."
    elif final < inicial:
        return "A missão apresentou tendência de melhora."
    return "A missão permaneceu estável em relação ao início."


def identificar_area_mais_afetada(pontuacoes):
    maior = max(pontuacoes)
    return areas_monitoradas[pontuacoes.index(maior)]


def gerar_relatorio_final(historico, acumulado_areas):
    total = len(historico)
    pontuacoes = [c["pontuacao"] for c in historico]

    media_temp = sum(c["dados"][0] for c in historico) / total
    media_com = sum(c["dados"][1] for c in historico) / total
    media_bat = sum(c["dados"][2] for c in historico) / total
    media_oxi = sum(c["dados"][3] for c in historico) / total
    media_est = sum(c["dados"][4] for c in historico) / total

    ciclo_critico = pontuacoes.index(max(pontuacoes)) + 1
    maior_risco = max(pontuacoes)
    risco_medio = sum(pontuacoes) / total
    qtd_criticos = sum(
        1 for c in historico if c["classificacao"] == "MISSÃO CRÍTICA"
    )

    tendencia = analisar_tendencia(pontuacoes[0], pontuacoes[-1])
    area_afetada = identificar_area_mais_afetada(acumulado_areas)
    classificacao_final = classificar_ciclo(round(risco_medio))

    print("=" * 60)
    print("RELATÓRIO FINAL DA MISSÃO")
    print("=" * 60)
    print(f"Missão: {NOME_MISSAO}")
    print(f"Equipe: {NOME_EQUIPE}")
    print(f"Quantidade de ciclos analisados: {total}\n")
    print(f"Média de temperatura:   {media_temp:.2f} °C")
    print(f"Média de comunicação:   {media_com:.2f}%")
    print(f"Média de bateria:       {media_bat:.2f}%")
    print(f"Média de oxigênio:      {media_oxi:.2f}%")
    print(f"Média de estabilidade:  {media_est:.2f}%\n")
    print(f"Ciclo mais crítico:        Ciclo {ciclo_critico}")
    print(f"Maior pontuação de risco:  {maior_risco}")
    print(f"Risco médio da missão:     {risco_medio:.2f}")
    print(f"Quantidade de ciclos críticos: {qtd_criticos}\n")
    print("Tendência da missão:")
    print(f"  {tendencia}\n")
    print("Pontuação acumulada por área:")
    for i, area in enumerate(areas_monitoradas):
        print(f"  {area}: {acumulado_areas[i]} pontos")
    print(f"\nÁrea mais afetada:\n  {area_afetada}\n")
    print(f"Classificação final da missão:\n  {classificacao_final}\n")
    print("Conclusão:")

    if classificacao_final == "MISSÃO CRÍTICA":
        print(
            "  A missão atingiu nível crítico. Sistemas vitais precisam de intervenção imediata."
        )
    elif classificacao_final == "MISSÃO EM ATENÇÃO":
        print(
            "  A missão apresentou instabilidade relevante. Manter plano de contingência ativo."
        )
    else:
        print(
            "  A missão transcorreu de forma estável. Sistemas dentro dos parâmetros aceitáveis."
        )
    print("=" * 60)


def main():
    print("=" * 60)
    print("MISSION CONTROL AI")
    print("=" * 60)
    print(f"Missão: {NOME_MISSAO}")
    print(f"Equipe: {NOME_EQUIPE}")
    print(f"Quantidade de ciclos analisados: {len(dados_missao)}")
    print("=" * 60)

    historico = []
    acumulado_areas = [0, 0, 0, 0, 0]

    for idx, ciclo in enumerate(dados_missao, start=1):
        temp, com, bat, oxi, est = ciclo

        res_temp = analisar_temperatura(temp)
        res_com = analisar_comunicacao(com)
        res_bat = analisar_bateria(bat)
        res_oxi = analisar_oxigenio(oxi)
        res_est = analisar_estabilidade(est)

        resultados = [res_temp, res_com, res_bat, res_oxi, res_est]
        pontuacao = sum(r[2] for r in resultados)

        for i, res in enumerate(resultados):
            acumulado_areas[i] += res[2]

        classe = classificar_ciclo(pontuacao)
        recomendacao = gerar_recomendacao(resultados, pontuacao)

        print(f"\nCICLO {idx}")
        print("-" * 60)
        print(f"Temperatura:  {temp} °C | {res_temp[0]} | {res_temp[1]}")
        print(f"Comunicação:  {com}% | {res_com[0]} | {res_com[1]}")
        print(f"Bateria:      {bat}% | {res_bat[0]} | {res_bat[1]}")
        print(f"Oxigênio:     {oxi}% | {res_oxi[0]} | {res_oxi[1]}")
        print(f"Estabilidade: {est}% | {res_est[0]} | {res_est[1]}")
        print(f"Pontuação de risco do ciclo: {pontuacao}")
        print(f"Classificação do ciclo: {classe}")
        print(f"Recomendação: {recomendacao}")

        historico.append(
            {
                "ciclo": idx,
                "dados": ciclo,
                "pontuacao": pontuacao,
                "classificacao": classe,
            }
        )

    print()
    gerar_relatorio_final(historico, acumulado_areas)


if __name__ == "__main__":
    main()