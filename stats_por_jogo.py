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
    r["aa"] = count_aa

    return r


def spj_menu(m):
    print("\n\n\n--------------------------------------------------")
    print("1 - Golos")
    print("2 - Penaltys")
    print("3 - Cartões amarelos")
    print("4 - Cartões vermelhos")
    print("5 - Tempo de compensação")
    print("6 - Sair")
    n = int(input("\nOpção: "))
    if(n == 1):
        golos()
    elif(n == 2):
        penaltys()
    elif(n == 3):
        amarelos()
    elif(n == 4):
        vermelhos()
    elif(n == 5):
        compensacao()        
    else:
        pass



def golos():
    pass

def penaltys():
    pass

def amarelos():
    pass

def vermelhos():
    pass

def compensacao():
    pass