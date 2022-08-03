import random


def constroiMatriz():
    "construção da matriz do jogo da memória"
    # Matriz dos valores dos jogo da memoria 4x4
    matriz = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    valores = [1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8]
    
    for numero in valores: # Estabelecendo os valores das coordenadas da matriz de forma aleatória usando o random.sample, para os numeros dentro dos valores.
        coordenadaX = random.sample([0,1,2,3],1)[0]
        coordenadaY = random.sample([0,1,2,3],1)[0]
        while matriz[coordenadaX][coordenadaY] != 0: # enquanto as coordenadas da matriz forem diferentes de zero, a posição e as coordenadas  vão corresponder um valor aleatório dentro da matriz 
            posicao = random.sample([0,1,2,3],2)
            coordenadaX = random.sample([0,1,2,3],1)[0]
            coordenadaY = random.sample([0,1,2,3],1)[0]
        matriz[coordenadaX][coordenadaY] = numero
    
    return matriz #retorno da função dado os valores das coordenadas dentro da matriz, retornando a matriz 

def matrizOcultada():
    '''função para ocultar a matriz'''
    matrizOculta = [["*","*","*","*"],["*","*","*","*"],["*","*","*","*"],["*","*","*","*"]] #Variavel para ocultar a matriz com as string's
    return matrizOculta 


def imprimir_Matriz(matriz):
   # os valores da matriz convertidos em string 
    print(str(matriz[0][0]) + " " +  str(matriz[0][1]) + " " + str(matriz[0][2]) + " " + str(matriz[0][3]))
    print(str(matriz[1][0]) + " " +  str(matriz[1][1]) + " " + str(matriz[1][2]) + " " + str(matriz[1][3]))
    print(str(matriz[2][0]) + " " +  str(matriz[2][1]) + " " + str(matriz[2][2]) + " " + str(matriz[2][3]))
    print(str(matriz[3][0]) + " " +  str(matriz[3][1]) + " " + str(matriz[3][2]) + " " + str(matriz[3][3]))


def primeiraJogada():
    "primeira jogada"
    primeiraPosicao = input("Faça a primeira Jogada [x,y]: ") # entrada do teclado para a posição dado as coordenadas X,Y
    primeiraJogada = [int(primeiraPosicao[0]), int(primeiraPosicao[2])]
    return primeiraJogada #retornando a primeira jogada dado as coordenadas 


def segundaJogada():
    segundaPosicao = input("Faça a segunda Jogada [x,y]: ") #entrada do teclado para a posição dado as coordenadas X,Y
    segundaJogada = [int(segundaPosicao[0]), int(segundaPosicao[2])]
    return segundaJogada #retornando a primeira jogada dado as coordenadas 


def executaJogada(matrizMemoria, matriz_Oculta, jogada): #função para executar as jogadas
    matriz_Oculta[jogada[0]][jogada[1]] = matrizMemoria[jogada[0]][jogada[1]] #chama as funções matriz_oculta e a imprimir_matriz 
    imprimir_Matriz(matriz_Oculta)


def validaAcerto(matrizMemoria, matrizOcultada, jogada1, jogada2): # valida o acerto da função 
    if (matrizMemoria[jogada1[0]][jogada1[1]] != matrizMemoria[jogada2[0]][jogada2[1]]): #se a jogada for errada ele volta a esconder o valor pra refazer a jogada 
        matrizOcultada[jogada1[0]][jogada1[1]] = "*"
        matrizOcultada[jogada2[0]][jogada2[1]] = "*"
        print("Ixi ein .. Voce errou, Tente de Novo.") #se a jogada for errada a função printa que ele errou a jogada
    else: # caso contrario será inidcado um acerto 
        print("Parabens! Voce acertou.")


def concluido(matriz): # forma a matriz dentro do jogo com os asteriscos 
    for l in range(4):
        for c in range(4):
            if (matriz[l][c] == "*"):
                return False
    return True


def validaPosicao(jogada, matrizOculta): #valida a jogada dentro da função matrizoculta
    if jogada[0] not in [0,1,2,3]: # se a jogada na posição 0 for fora desses valores dentro da matriz a jogada será invalida 
        print("Posicao Invalida.")
        return False
    elif jogada[1] not in [0,1,2,3]: # se a jogada na posição 0 for fora desses valores dentro da matriz a jogada será invalida 
        print("Posicao Invalida.")
        return False
    elif matrizOculta[jogada[0]][jogada[1]] != "*": # caso a posição esteja dentro da matriz e ja tenha sido escolhida, ele retorna que a posição já foi escolhida 
        print("Posicao ja escolhida.")
        return False
    return True


def main():
    # unificando as funções para ser chamada 
    matrizMemoria = constroiMatriz() 
    matriz_Oculta = matrizOcultada()
    numeroJogadas = 1

    while concluido(matriz_Oculta) == False: 
        imprimir_Matriz(matriz_Oculta)
        jogada1 = primeiraJogada()
        while validaPosicao(jogada1,matriz_Oculta) == False:
            jogada1 = primeiraJogada()
        executaJogada(matrizMemoria, matriz_Oculta, jogada1)
        jogada2 = segundaJogada()
        while validaPosicao(jogada2, matriz_Oculta) == False: 
            jogada2 = segundaJogada()
        executaJogada(matrizMemoria, matriz_Oculta, jogada2)
        validaAcerto(matrizMemoria, matriz_Oculta, jogada1, jogada2)
        numeroJogadas += 1 # contador para repetir as jogadas entrando no looping 

    print("Parabens!! Voce conseguiu descobir todas as casas em " + str(numeroJogadas) + " jogadas!")

if __name__ == "__main__":
    main()
