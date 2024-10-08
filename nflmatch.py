import random
import time

def jogar():
    jogadas = {
        'Touchdown': 6,
        'Field Goal':3,
        'Falha': 0
    }
    
    jogada = random.choice(list(jogadas.keys()))
    return jogada, jogadas[jogada]
    
    def simular_jogo():
        time1: "Team A"
        time2: "Team B"
        placar1 = 0
        placar2 = 0
        
        print(f"Inicio do jogo: {time1} vs {time2}\n")
        
        for quarto in range(1, 5):
            print(f"Quarto {quarto} começando...\n")
            for i in range(3):
                jogada1, pontos1 - jogar()
                jogada2, pontos2 = jogar()
                
                placar1 += pontos1
                placar2 += pontos2
                
                print(f"{time1} fez uma jogada: {jogada1} e marcou {pontos1} pontos.")
                print(f"{time2} fez uma jogada: {jogada2} e marcou {pontos2} pontos.\n")
                time.sleep(1)
                
        print("Fim de jogoz!\n")
        print(f"Placar Final: {time1} {placar1} x {placar2} {time2")
        
        if placar1 > placar2:
            print(f"{time1} venceu !")
        elif placar2 > placar1:
            print(f"{time2} venceu !")
        else:
            print("Empate")
            
        simular_jogo()
        