from stats_por_jogo import spj_menu
from stats_por_equipa import spe_menu


def menu():
    

    print("\n\n\n*************** HUGO ROCHA REF STATS 23/24***************")


    while(True):
        print("\n\n\n--------------------------------------------------")
        print("1 - Árbitro")
        print("2 - Assistente")
        print("3 - Sair")
        m = int(input("\nOpção: "))
        if(m != 1 and m != 2):
            break
        elif m == 1:
            m = "a"
        else:
            m = "aa"
        print("\n\n\n--------------------------------------------------\n1 - Estatísticas do árbitro por jogo")
        print("2 - Estatísticas por equipa")
        print("3 - Sair")
        n = int(input("\nOpção: "))
        if(n == 1):
            spj_menu(m)
        elif(n == 2):
            spe_menu(m)
        else:
            break



def main():
    menu()
    return 0


main()