import random 

def main():
    # Apresentação do programa
    print("-----------VALORES DA QUINA------------")
    print("==============================\n")

    # Dentro do alcance geral 5 valores aleatórios de 1 a 100
    for j in range(0,5):
        print (random.randint(1,100))

    # Enquanto a condição for verdadeira e o jogador desejar jogar de novo 
    while True:
        print(" ")
        print("==============================")

        # Enquanto a condição de jogo for s ele sempre vai gerar mais 5 novos valores 
        jogada = input("Deseja Jogar de novo?(s/n):")
        print(" ")
        # Se a Jogada for s ele repete a jogada 
        if  jogada == str('s'):
            for i in range(0,5):
                print(random.randint(1,100))
                continue
        #  Caso não deseje jogar de novo ele cancela o jogo 
        if jogada == str('n'):
            print("========FIM DO JOGO=========")
            break
             
if __name__=='__main__':
    main()
        
    

