import pandas as pd


df = pd.read_csv("statsref.csv")


def jogos_por_equipa():

    r = {}
    r["aa"] = {}
    r["a"] = {}

    for i, line in df.iterrows():
        if line["equipacasa"] not in r[line["funcao"]]:
            r[line["funcao"]][line["equipacasa"]] = 1
        else:
            r[line["funcao"]][line["equipacasa"]] += 1
        if line["equipafora"] not in r[line["funcao"]]:
            r[line["funcao"]][line["equipafora"]] = 1
        else:
            r[line["funcao"]][line["equipafora"]] += 1
    
    sorted_r = {}
    sorted_r["aa"] = {}
    sorted_r["a"] = {}
    sorted_r["aa"] = {team : r["aa"][team] for team in sorted(r["aa"].keys())}
    sorted_r["a"] = {team : r["a"][team] for team in sorted(r["a"].keys())}

    return sorted_r


jogos_por_equipa = jogos_por_equipa()

        
def pontos_conquistados(m):
    r = {}
    for team in jogos_por_equipa[m]:
        r[team] = 0 #team -> pontosconquistados
        
    
    for i, line in df.iterrows():
        if line["funcao"] == m:
            if int(line["goloscasa"]) > int(line["golosfora"]):
                r[line["equipacasa"]] += 3
            elif int(line["goloscasa"]) < int(line["golosfora"]):
                r[line["equipafora"]] += 3
            else:
                r[line["equipacasa"]] += 1
                r[line["equipafora"]] += 1
        
    
    print("\n\n\nEquipa, Pontos Conquistados, Pontos Possíveis, Número de Jogos, Taxa de Aproveitamento")
    for team in r:
        print(f"{team}, {r[team]}, {jogos_por_equipa[m][team]*3}, {jogos_por_equipa[m][team]}, {100*(r[team]/(jogos_por_equipa[m][team]*3))}%.")


def VED(m):

    r = {}
    for team in jogos_por_equipa[m]:
        r[team] = [0,0,0] #team -> (v,e,d)
    
    
    for i, line in df.iterrows():
        if line["funcao"] == m:
            if line["goloscasa"] > line["golosfora"]:
                r[line["equipacasa"]][0] += 1
                r[line["equipafora"]][2] += 1
            elif line["goloscasa"] < line["golosfora"]:
                r[line["equipacasa"]][2] += 1
                r[line["equipafora"]][0] += 1
            else:
                r[line["equipacasa"]][1] += 1
                r[line["equipafora"]][1] += 1


    
    print("\n\n\nEquipa, Jogos, Vitórias, Empates, Derrotas, Taxa de Vitórias, Taxa de Empates, Taxa de Derrotas")
    for team in r:
        print(f"{team}, {jogos_por_equipa[m][team]}, {r[team][0]}, {r[team][1]}, {r[team][2]}, {100*(r[team][0]/jogos_por_equipa[m][team])}%, {100*(r[team][1]/jogos_por_equipa[m][team])}%, {100*(r[team][2]/jogos_por_equipa[m][team])}%.")


def golos(m):

    r = {}
    for team in jogos_por_equipa[m]:
        r[team] = [0,0] #team : (gm,gs)

    for i, line in df.iterrows():
        if line["funcao"] == m:
            r[line["equipacasa"]][0] += int(line["goloscasa"])
            r[line["equipacasa"]][1] += int(line["golosfora"])
            r[line["equipafora"]][0] += int(line["golosfora"])
            r[line["equipafora"]][1] += int(line["goloscasa"])

    print("\n\n\nEquipa, Número de Jogos, Golos Marcados, Golos Sofridos, Diferença de Golos, Média Golos Marcados p/jogo, Média Golos Sofridos p/jogo")
    for team in r:
        print(f"{team}, {jogos_por_equipa[m][team]}, {r[team][0]}, {r[team][1]}, {r[team][0]- r[team][1]}, {r[team][0]/jogos_por_equipa[m][team]}, {r[team][1]/jogos_por_equipa[m][team]}")

 

def penaltys(m):

    r = {}
    for team in jogos_por_equipa[m]:
        r[team] = 0 #team : penaltys

    for i, line in df.iterrows():
        if line["funcao"] == m:
            r[line["equipacasa"]] += int(line["penaltyscasa"])
            r[line["equipafora"]] += int(line["penaltysfora"])

    print("\n\n\nEquipa, Número de Penalties, Número de jogos, Média de Penalties p/jogo")
    for team in r:
        print(f"{team}, {r[team]}, {jogos_por_equipa[m][team]}, {r[team]/jogos_por_equipa[m][team]}")      



def amarelos(m):
    r = {}

    for team in jogos_por_equipa[m]:
        r[team] = 0 #team : amarelos
    
    for i, line in df.iterrows():
        if line["funcao"] == m:
            r[line["equipacasa"]] += int(line["amareloscasa"])
            r[line["equipafora"]] += int(line["amarelosfora"])
    
    print("\n\n\nEquipa, Número de Cartões Amarelos, Número de jogos, Média de Amarelos p/jogo")
    for team in r:
        print(f"{team}, {r[team]}, {jogos_por_equipa[m][team]}, {r[team]/jogos_por_equipa[m][team]}")      



def vermelhos(m):
    r = {}

    for team in jogos_por_equipa[m]:
        r[team] = 0 #team : vermelhos
    
    for i, line in df.iterrows():
        if line["funcao"] == m:
            r[line["equipacasa"]] += int(line["vermelhoscasa"])
            r[line["equipafora"]] += int(line["vermelhosfora"])
    
    print("\n\n\nEquipa, Número de Cartões Vermelhos, Número de jogos, Média de Vermelhos p/jogo")
    for team in r:
        print(f"{team}, {r[team]}, {jogos_por_equipa[m][team]}, {r[team]/jogos_por_equipa[m][team]}")      



def compensacao(m):

    r = {}
    for team in jogos_por_equipa[m]:
        r[team] = [0,0] #team : total compensacao1p, total compensacao2p
    
    for i, line in df.iterrows():
        if line["funcao"] == m:
            r[line["equipacasa"]][0] += int(line["compensacao1p"])
            r[line["equipafora"]][0] += int(line["compensacao1p"])
            r[line["equipacasa"]][1] += int(line["compensacao2p"])
            r[line["equipafora"]][1] += int(line["compensacao2p"])
    
    print("\n\n\nEquipa, Média de Compensação 1P, Média de Compensação 2P, Total Compensação 1P, Total Compensação 2P, Total Compensação, Número de Jogos, Média de Compensação p/jogo")
    for team in r:
        print(f"{team}, {r[team][0]/jogos_por_equipa[m][team]}, {r[team][1]/jogos_por_equipa[m][team]}, {r[team][0]}, {r[team][1]}, {r[team][0] + r[team][1]}, {jogos_por_equipa[m][team]}, {(r[team][0]+r[team][1])/jogos_por_equipa[m][team]}")
    

def spe_menu(m):
    print("\n\n\n--------------------------------------------------")
    print("1 - Pontos conquistados")
    print("2 - Vitórias/Empates/Derrotas")
    print("3 - Golos")
    print("4 - Penaltys")
    print("5 - Cartões amarelos")
    print("6 - Cartões vermelhos")
    print("7 - Tempo de compensação")
    print("8 - Voltar")
    n = int(input("\nOpção: "))
    if(n == 1):
        pontos_conquistados(m)
    elif(n == 2):
        VED(m)
    elif(n == 3):
        golos(m)
    elif(n == 4):
        penaltys(m)
    elif(n == 5):
        amarelos(m)
    elif(n == 6):
        vermelhos(m)
    elif(n == 7):
        compensacao(m)
    else:
        pass
    
    

    return 0
