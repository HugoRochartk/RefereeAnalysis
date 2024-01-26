import pandas as pd


df = pd.read_csv("datasets/statsref2324.csv")


def jogos_por_func():
    r = {}
    count_aa = count_a = 0

    for i,line in df.iterrows():
        if line["funcao"] == "a":
            count_a += 1
        else:
            count_aa += 1

    r["a"] = count_a    
    r["aa"] = count_aa # r = jogos_por_func()

    return r


def spj_menu(m):
    r = jogos_por_func()
    njogos = r[m]
    print("\n\n\n--------------------------------------------------")
    print("1 - Golos")
    print("2 - Penaltys")
    print("3 - Cartões amarelos")
    print("4 - Cartões vermelhos")
    print("5 - Tempo de compensação")
    print("6 - Sair")
    n = int(input("\nOpção: "))
    if(n == 1):
        golos(m, njogos)
    elif(n == 2):
        penaltys(m, njogos)
    elif(n == 3):
        amarelos(m, njogos)
    elif(n == 4):
        vermelhos(m, njogos)
    elif(n == 5):
        compensacao(m, njogos)        
    else:
        pass



def golos(m, njogos):

    c = 0
    f = 0
    
    for i, line in df.iterrows(): 
        if (i != 0 and line['funcao'] == m):
            c += line['goloscasa']
            f += line['golosfora']

    
    print("\n\nMédia de golos (caseiros) por jogo, Média de golos (fora) por jogo, Média de golos total por jogo")
    print(f"{round(c/njogos,2)}, {round(f/njogos,2)}, {round((c+f)/njogos,2)}")
    


def penaltys(m, njogos):
    
    c = 0
    f = 0
    
    for i, line in df.iterrows(): 
        if (i != 0 and line['funcao'] == m):
            c += line['penaltyscasa']
            f += line['penaltysfora']
        

    print("\n\nMédia de penaltys (caseiros) por jogo, Média de penaltys (fora) por jogo, Média de penaltys totais por jogo")
    print(f"{round(c/njogos,2)}, {round(f/njogos,2)}, {round((c+f)/njogos,2)}")


def amarelos(m, njogos):
    
    c = 0
    f = 0
    
    for i, line in df.iterrows(): 
        if (i != 0 and line['funcao'] == m):
            c += line['amareloscasa']
            f += line['amarelosfora']
        

    print("\n\nMédia de amarelos (caseiros) por jogo, Média de amarelos (fora) por jogo, Média de amarelos totais por jogo")
    print(f"{round(c/njogos,2)}, {round(f/njogos,2)}, {round((c+f)/njogos,2)}")


def vermelhos(m, njogos):
    
    c = 0
    f = 0
    
    for i, line in df.iterrows(): 
        if (i != 0 and line['funcao'] == m):
            c += line['vermelhoscasa']
            f += line['vermelhosfora']
        

    print("\n\nMédia de vermelhos (caseiros) por jogo, Média de vermelhos (fora) por jogo, Média de vermelhos totais por jogo")
    print(f"{round(c/njogos,2)}, {round(f/njogos,2)}, {round((c+f)/njogos,2)}")


from math import floor


def converte_min_para_seg(temp):

    min = floor(temp)
    seg = floor((temp - min) * 60)
    
    if seg != 0:
        return f"{min}min{seg}seg"
    else:
        return f"{min}min"



def compensacao(m, njogos):
    
    p1 = 0
    p2 = 0
    
    for i, line in df.iterrows(): 
        if (i != 0 and line['funcao'] == m):
            p1 += line['compensacao1p']
            p2 += line['compensacao2p']
        

    print("\n\nMédia de compensação na 1ª parte por jogo, Média de compensação na 2ª parte por jogo, Média de compensação total por jogo")
    print(f"{converte_min_para_seg(round(p1/njogos,2))}, {converte_min_para_seg(round(p2/njogos,2))}, {converte_min_para_seg(round((p1+p2)/njogos,2))}")