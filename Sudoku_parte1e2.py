#PARTE1

#Questão01
def posicao_livre(matriz,linha,coluna):
    '''Função que recebe como entrada o estado da grade e uma posição e retorna True caso a posição esteja vazia e False, caso contrário.
    list(list), int, int --> bool'''
    posicao = matriz[int(linha)- 1][int(coluna) - 1]
    if posicao == 0:
        return True
    else:
        return False   

#Comentário:
#Coloquei o int, pois quando eu tentava realizar o código aparecia um erro de operação entre string e inteiro. Então eu transformei tudo para inteiro.
    
#Testes:   
#posicao_livre([[7,0,0,1,0,0,0,5,2],[9,1,0,5,8,0,0,6,0],[0,0,6,7,3,0,1,0,0],[0,0,0,0,0,0,9,2,5],[0,5,1,0,0,0,6,4,0],[2,4,9,0,0,0,0,0,0],[0,0,5,0,7,3,4,0,0],[0,6,0,0,1,5,0,8,7],[1,9,0,0,0,8,0,0,6]],2,3) --> True
#posicao_livre([[7,0,0,1,0,0,0,5,2],[9,1,0,5,8,0,0,6,0],[0,0,6,7,3,0,1,0,0],[0,0,0,0,0,0,9,2,5],[0,5,1,0,0,0,6,4,0],[2,4,9,0,0,0,0,0,0],[0,0,5,0,7,3,4,0,0],[0,6,0,0,1,5,0,8,7],[1,9,0,0,0,8,0,0,6]],8,4) --> True
#posicao_livre([[7,0,0,1,0,0,0,5,2],[9,1,0,5,8,0,0,6,0],[0,0,6,7,3,0,1,0,0],[0,0,0,0,0,0,9,2,5],[0,5,1,0,0,0,6,4,0],[2,4,9,0,0,0,0,0,0],[0,0,5,0,7,3,4,0,0],[0,6,0,0,1,5,0,8,7],[1,9,0,0,0,8,0,0,6]],6,7) --> True
#posicao_livre([[7,0,0,1,0,0,0,5,2],[9,1,0,5,8,0,0,6,0],[0,0,6,7,3,0,1,0,0],[0,0,0,0,0,0,9,2,5],[0,5,1,0,0,0,6,4,0],[2,4,9,0,0,0,0,0,0],[0,0,5,0,7,3,4,0,0],[0,6,0,0,1,5,0,8,7],[1,9,0,0,0,8,0,0,6]],5,2) --> False




#Questão02  
def linha_disponivel(matriz,linha,coluna,valor):
    '''Função que dado como entrada o estado da grade, a posição e um valor de 1 a 9, retorna e devolve o booleano True se o valor fornecido não aparece naquela mesma linha e False, caso contrário. Considere que, a posição escolhida está livre.
    list(list), int, int, int -> bool'''
    linha_matriz = matriz[int(linha) - 1]
    if valor in linha_matriz:
        return False
    else:
        return True

#Comentário:
#Coloquei o int, pois quando eu tentava realizar o código aparecia um erro de operação entre string e inteiro. Então eu transformei tudo para inteiro.
   
#Testes:
# linha_disponivel([[7,0,0,1,0,0,0,5,2],[9,1,0,5,8,0,0,6,0],[0,0,6,7,3,0,1,0,0],[0,0,0,0,0,0,9,2,5],[0,5,1,0,0,0,6,4,0],[2,4,9,0,0,0,0,0,0],[0,0,5,0,7,3,4,0,0],[0,6,0,0,1,5,0,8,7],[1,9,0,0,0,8,0,0,6]],2,3,7) --> True
# linha_disponivel([[7,0,0,1,0,0,0,5,2],[9,1,0,5,8,0,0,6,0],[0,0,6,7,3,0,1,0,0],[0,0,0,0,0,0,9,2,5],[0,5,1,0,0,0,6,4,0],[2,4,9,0,0,0,0,0,0],[0,0,5,0,7,3,4,0,0],[0,6,0,0,1,5,0,8,7],[1,9,0,0,0,8,0,0,6]],8,4,6) --> False
# linha_disponivel([[7,0,0,1,0,0,0,5,2],[9,1,0,5,8,0,0,6,0],[0,0,6,7,3,0,1,0,0],[0,0,0,0,0,0,9,2,5],[0,5,1,0,0,0,6,4,0],[2,4,9,0,0,0,0,0,0],[0,0,5,0,7,3,4,0,0],[0,6,0,0,1,5,0,8,7],[1,9,0,0,0,8,0,0,6]],5,2,8) --> True




#Questão03
def coluna_disponivel(matriz,linha,coluna,valor):
    '''Dado uma matriz como entrada, uma posição(linha e coluna) e um valor (de 1 a 9),
    a função retorna o booleano True se o valor fornecido não aparece no jogo em relação a coluna e caso contrário retorna o Booleano False quando a posição naquela coluna está livre.'''
    '''list(list), int, int, int'''
    linha_matriz= matriz[int(linha)- 1]
    coluna_matriz = []
    for i in range(len(matriz)):
        coluna_matriz = coluna_matriz + [matriz[i][int(coluna)-1]]
    if valor in coluna_matriz:
        return False
    else:
        return True

    
#Comentário:
#Coloquei o int, pois quando eu tentava realizar o código aparecia um erro de operação entre string e inteiro. Então eu transformei tudo para inteiro.
     
#Testes:
#coluna_disponivel([[7,0,0,1,0,0,0,5,2],[9,1,0,5,8,0,0,6,0],[0,0,6,7,3,0,1,0,0],[0,0,0,0,0,0,9,2,5],[0,5,1,0,0,0,6,4,0],[2,4,9,0,0,0,0,0,0],[0,0,5,0,7,3,4,0,0],[0,6,0,0,1,5,0,8,7],[1,9,0,0,0,8,0,0,6]],3,6,9) --> True
#coluna_disponivel([[7,0,0,1,0,0,0,5,2],[9,1,0,5,8,0,0,6,0],[0,0,6,7,3,0,1,0,0],[0,0,0,0,0,0,9,2,5],[0,5,1,0,0,0,6,4,0],[2,4,9,0,0,0,0,0,0],[0,0,5,0,7,3,4,0,0],[0,6,0,0,1,5,0,8,7],[1,9,0,0,0,8,0,0,6]],1,1,7) --> False
#coluna_disponivel([[7,0,0,1,0,0,0,5,2],[9,1,0,5,8,0,0,6,0],[0,0,6,7,3,0,1,0,0],[0,0,0,0,0,0,9,2,5],[0,5,1,0,0,0,6,4,0],[2,4,9,0,0,0,0,0,0],[0,0,5,0,7,3,4,0,0],[0,6,0,0,1,5,0,8,7],[1,9,0,0,0,8,0,0,6]],1,1,8) --> True






#PARTE2

#Questão01
def subgrades(matriz,linha,coluna,valor):
    '''Função que recebe uma grade, as coordenadas da célula dessa grade e um valor de 1 a 9 como entrada e retorna a expressão booleano True se o valor fornecido não aparece na mesma sub-grade e False, caso contrário.
    list(list),int,int,int --> bool'''
    if linha == 1 or linha==2 or linha == 3:
        matriz_nova = [matriz[0],matriz[1],matriz[2]]    
    if linha == 4 or linha==5 or linha == 6:
        matriz_nova = [matriz[3],matriz[4],matriz[5]]
    if linha == 7 or linha==8 or linha == 9:
        matriz_nova = [matriz[6],matriz[7],matriz[8]]
    subgrade = []
    if coluna == 1 or coluna==2 or coluna == 3:
        for i in range(len(matriz)):
            subgrade = subgrade+ [matriz[i][0],matriz[i][1],matriz[i][2]]
    if coluna == 4 or coluna==5 or coluna == 6:
        for i in range(len(matriz)):
            subgrade = subgrade + [matriz[i][3],matriz[i][4],matriz[i][5]]
    if coluna == 7 or coluna==8 or coluna == 9:
        for i in range(len(matriz)):
            subgrade = subgrade + [matriz[i][6],matriz[i][7],matriz[i][8]]
    if valor in subgrade:
        return False
    else:
        return True
    
def main():
    matriz1 = [[7,0,0,1,0,0,0,5,2],[9,1,0,5,8,0,0,6,0],[0,0,6,7,3,0,1,0,0],[0,0,0,0,0,0,9,2,5],[0,5,1,0,0,0,6,4,0],[2,4,9,0,0,0,0,0,0],[0,0,5,0,7,3,4,0,0],[0,6,0,0,1,5,0,8,7],[1,9,0,0,0,8,0,0,6]]
    matriz2 = [[0,0,0,1,0,0,0,5,2],[9,1,0,5,8,0,0,6,0],[0,0,6,7,3,0,1,0,0],[0,0,0,0,0,0,9,2,5],[0,5,1,0,0,0,6,4,0],[2,4,9,0,0,0,0,0,0],[0,0,5,0,7,3,4,0,0],[0,6,0,0,1,5,0,8,7],[1,9,0,0,0,8,0,0,0]]    
print ('Testes da funcao subgrades, usam matriz1 ou matriz2.')
print ('matriz1:')
print ('matriz1 = [[7,0,0,1,0,0,0,5,2],[9,1,0,5,8,0,0,6,0],[0,0,6,7,3,0,1,0,0],[0,0,0,0,0,0,9,2,5],[0,5,1,0,0,0,6,4,0],[2,4,9,0,0,0,0,0,0],[0,0,5,0,7,3,4,0,0],[0,6,0,0,1,5,0,8,7],[1,9,0,0,0,8,0,0,6]]')
print ('matriz2:')
print ('matriz2 = [[0,0,0,1,0,0,0,5,2],[9,1,0,5,8,0,0,6,0],[0,0,6,7,3,0,1,0,0],[0,0,0,0,0,0,9,2,5],[0,5,1,0,0,0,6,4,0],[2,4,9,0,0,0,0,0,0],[0,0,5,0,7,3,4,0,0],[0,6,0,0,1,5,0,8,7],[1,9,0,0,0,8,0,0,0]]')    

# teste 1
print ('\nTesta se um determinado valor estaria de acordo com as regras do jogo com respeito às sub-grades 3x3.')
teste = subgrades([[7,0,0,1,0,0,0,5,2],[9,1,0,5,8,0,0,6,0],[0,0,6,7,3,0,1,0,0],[0,0,0,0,0,0,9,2,5],[0,5,1,0,0,0,6,4,0],[2,4,9,0,0,0,0,0,0],[0,0,5,0,7,3,4,0,0],[0,6,0,0,1,5,0,8,7],[1,9,0,0,0,8,0,0,6]],4,3,5)
print ('\nmatriz1,4,3,5: esperado = False, obtido = ', teste)

# teste 2
print ('\nTesta se um determinado valor estaria de acordo com as regras do jogo com respeito às sub-grades 3x3.')
teste = subgrades([[0,0,0,1,0,0,0,5,2],[9,1,0,5,8,0,0,6,0],[0,0,6,7,3,0,1,0,0],[0,0,0,0,0,0,9,2,5],[0,5,1,0,0,0,6,4,0],[2,4,9,0,0,0,0,0,0],[0,0,5,0,7,3,4,0,0],[0,6,0,0,1,5,0,8,7],[1,9,0,0,0,8,0,0,0]],8,2,7)
print ('\nmatriz2,8,2,7: esperado = True, obtido = ', teste)

if __name__ == '__main__':
    main()




#Questão02
def jogada_valida(matriz,linha,coluna,valor):
    '''função que recebe uma grade parcialmente preenchida, as coordenadas de uma célula da grade e um valor de 1 a 9 e devolve True se a jogada é válida e False, caso contrário.
    list(list), int, int --> bool'''
    passo1 = posicao_livre(matriz,linha,coluna)
    passo2 = linha_disponivel(matriz,linha,coluna,valor)
    passo3 = coluna_disponivel(matriz,linha,coluna,valor)
    passo4 = subgrades(matriz,linha,coluna,valor)
    if passo1==True and passo2==True and passo3==True and passo4==True:
        return True
    else:
        return False

def main():
    matriz1 = [[7,0,0,1,0,0,0,5,2],[9,1,0,5,8,0,0,6,0],[0,0,6,7,3,0,1,0,0],[0,0,0,0,0,0,9,2,5],[0,5,1,0,0,0,6,4,0],[2,4,9,0,0,0,0,0,0],[0,0,5,0,7,3,4,0,0],[0,6,0,0,1,5,0,8,7],[1,9,0,0,0,8,0,0,6]]
    matriz2 = [[0,0,0,1,0,0,0,5,2],[9,1,0,5,8,0,0,6,0],[0,0,6,7,3,0,1,0,0],[0,0,0,0,0,0,9,2,5],[0,5,1,0,0,0,6,4,0],[2,4,9,0,0,0,0,0,0],[0,0,5,0,7,3,4,0,0],[0,6,0,0,1,5,0,8,7],[1,9,0,0,0,8,0,0,0]]    
print ('Testes da funcao jogada_valida, usam matriz1 ou matriz2.')
print ('matriz1:')
print ('matriz1 = [[7,0,0,1,0,0,0,5,2],[9,1,0,5,8,0,0,6,0],[0,0,6,7,3,0,1,0,0],[0,0,0,0,0,0,9,2,5],[0,5,1,0,0,0,6,4,0],[2,4,9,0,0,0,0,0,0],[0,0,5,0,7,3,4,0,0],[0,6,0,0,1,5,0,8,7],[1,9,0,0,0,8,0,0,6]]')
print ('matriz2:')
print ('matriz2 = [[0,0,0,1,0,0,0,5,2],[9,1,0,5,8,0,0,6,0],[0,0,6,7,3,0,1,0,0],[0,0,0,0,0,0,9,2,5],[0,5,1,0,0,0,6,4,0],[2,4,9,0,0,0,0,0,0],[0,0,5,0,7,3,4,0,0],[0,6,0,0,1,5,0,8,7],[1,9,0,0,0,8,0,0,0]]')    

# teste 1
print ('Testa se um determinada jogada é válida de acordo com as regras do jogo.')
teste = jogada_valida([[7,0,0,1,0,0,0,5,2],[9,1,0,5,8,0,0,6,0],[0,0,6,7,3,0,1,0,0],[0,0,0,0,0,0,9,2,5],[0,5,1,0,0,0,6,4,0],[2,4,9,0,0,0,0,0,0],[0,0,5,0,7,3,4,0,0],[0,6,0,0,1,5,0,8,7],[1,9,0,0,0,8,0,0,6]],4,5,6)
print ('matriz1,4,5,6: esperado = True, obtido = ', teste)

# teste 2
print ('Testa se uma determinada jogada é válida de acordo com as regras do jogo.')
teste = jogada_valida([[0,0,0,1,0,0,0,5,2],[9,1,0,5,8,0,0,6,0],[0,0,6,7,3,0,1,0,0],[0,0,0,0,0,0,9,2,5],[0,5,1,0,0,0,6,4,0],[2,4,9,0,0,0,0,0,0],[0,0,5,0,7,3,4,0,0],[0,6,0,0,1,5,0,8,7],[1,9,0,0,0,8,0,0,0]],8,2,7)
print ('matriz2,8,2,7: esperado = False, obtido = ', teste)
if __name__ == '__main__':
    main()




#Questão03
def impressao(matriz):
    '''Função que mostra o estado atual da grade para o jogador em formato quadrado, usando um sublinhado '_' para mostrar as posições vazias.
    list(list) --> none'''
    linha1 = matriz[0]
    linha2 = matriz[1]
    linha3 = matriz[2]
    linha4 = matriz[3]
    linha5 = matriz[4]
    linha6 = matriz[5]
    linha7 = matriz[6]
    linha8 = matriz[7]
    linha9 = matriz[8]
    grade1 = []
    grade2 = []
    grade3 = []
    grade4 = []
    grade5 = []
    grade6 = []
    grade7 = []
    grade8 = []
    grade9 = []
    for i in range(len(linha1)):
        if 0 == linha1[i]:
            list.append(grade1,'_')
        else:
            list.append(grade1,linha1[i])
            
    for i in range(len(linha2)):
        if 0 == linha2[i]:
            list.append(grade2,'_')
        else:
            list.append(grade2,linha2[i])
            
    for i in range(len(linha3)):
        if 0 == linha3[i]:
            list.append(grade3,'_')
        else:
            list.append(grade3,linha3[i])
            
    for i in range(len(linha4)):
        if 0 == linha4[i]:
            list.append(grade4,'_')
        else:
            list.append(grade4,linha4[i])

    for i in range(len(linha5)):
        if 0 == linha5[i]:
            list.append(grade5,'_')
        else:
            list.append(grade5,linha5[i])

    for i in range(len(linha6)):
        if 0 == linha6[i]:
            list.append(grade6,'_')
        else:
            list.append(grade6,linha6[i])

    for i in range(len(linha7)):
        if 0 == linha7[i]:
            list.append(grade7,'_')
        else:
            list.append(grade7,linha7[i])

    for i in range(len(linha8)):
        if 0 == linha8[i]:
            list.append(grade8,'_')
        else:
            list.append(grade8,linha8[i])

    for i in range(len(linha1)):
        if 0 == linha9[i]:
            list.append(grade9,'_')
        else:
            list.append(grade9,linha9[i])
    print([grade1,grade2,grade3])
    print([grade4,grade5,grade6])
    print([grade7,grade8,grade9])

def main():
    matriz1 = [[7,0,0,1,0,0,0,5,2],[9,1,0,5,8,0,0,6,0],[0,0,6,7,3,0,1,0,0],[0,0,0,0,0,0,9,2,5],[0,5,1,0,0,0,6,4,0],[2,4,9,0,0,0,0,0,0],[0,0,5,0,7,3,4,0,0],[0,6,0,0,1,5,0,8,7],[1,9,0,0,0,8,0,0,6]]
    matriz2 = [[0,0,0,1,0,0,0,5,2],[9,1,0,5,8,0,0,6,0],[0,0,6,7,3,0,1,0,0],[0,0,0,0,0,0,9,2,5],[0,5,1,0,0,0,6,4,0],[2,4,9,0,0,0,0,0,0],[0,0,5,0,7,3,4,0,0],[0,6,0,0,1,5,0,8,7],[1,9,0,0,0,8,0,0,0]]    
print ('Testes da função impressão, usam matriz1 ou matriz2.')
print ('matriz1:')
print ('matriz1 = [[7,0,0,1,0,0,0,5,2],[9,1,0,5,8,0,0,6,0],[0,0,6,7,3,0,1,0,0],[0,0,0,0,0,0,9,2,5],[0,5,1,0,0,0,6,4,0],[2,4,9,0,0,0,0,0,0],[0,0,5,0,7,3,4,0,0],[0,6,0,0,1,5,0,8,7],[1,9,0,0,0,8,0,0,6]]')
print ('matriz2:')
print ('matriz2 = [[0,0,0,1,0,0,0,5,2],[9,1,0,5,8,0,0,6,0],[0,0,6,7,3,0,1,0,0],[0,0,0,0,0,0,9,2,5],[0,5,1,0,0,0,6,4,0],[2,4,9,0,0,0,0,0,0],[0,0,5,0,7,3,4,0,0],[0,6,0,0,1,5,0,8,7],[1,9,0,0,0,8,0,0,0]]')    

# teste 1
print ('Testa a impressão de uma determinada matriz.')
teste = impressao([[7,0,0,1,0,0,0,5,2],[9,1,0,5,8,0,0,6,0],[0,0,6,7,3,0,1,0,0],[0,0,0,0,0,0,9,2,5],[0,5,1,0,0,0,6,4,0],[2,4,9,0,0,0,0,0,0],[0,0,5,0,7,3,4,0,0],[0,6,0,0,1,5,0,8,7],[1,9,0,0,0,8,0,0,6]])
print ('matriz1: esperado = none, obtido = ', teste)

# teste 2
print ('Testa a impressão de uma determinada matriz.')
teste = impressao([[0,0,0,1,0,0,0,5,2],[9,1,0,5,8,0,0,6,0],[0,0,6,7,3,0,1,0,0],[0,0,0,0,0,0,9,2,5],[0,5,1,0,0,0,6,4,0],[2,4,9,0,0,0,0,0,0],[0,0,5,0,7,3,4,0,0],[0,6,0,0,1,5,0,8,7],[1,9,0,0,0,8,0,0,0]])
print ('matriz2: esperado = none, obtido = ', teste)


