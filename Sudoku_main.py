from Sudoku_parte1e2 import *

def main():
    grade01 = [[7,0,0,1,0,0,0,5,2],[9,1,0,5,8,0,0,6,0],[0,0,6,7,3,0,1,0,0],[0,0,0,0,0,0,9,2,5],[0,5,1,0,0,0,6,4,0],[2,4,9,0,0,0,0,0,0],[0,0,5,0,7,3,4,0,0],[0,6,0,0,1,5,0,8,7],[1,9,0,0,0,8,0,0,6]]
    grade02 = [[0,0,0,1,0,0,0,5,2],[9,1,0,5,8,0,0,6,0],[0,0,6,7,3,0,1,0,0],[0,0,0,0,0,0,9,2,5],[0,5,1,0,0,0,6,4,0],[2,4,9,0,0,0,0,0,0],[0,0,5,0,7,3,4,0,0],[0,6,0,0,1,5,0,8,7],[1,9,0,0,0,8,0,0,0]]
    grade03 = [[0,0,0,0,0,0,6,0,9],[1,0,0,0,0,4,0,0,0],[0,0,5,3,0,6,8,2,1],[0,0,4,6,7,0,0,5,0],[0,0,7,0,0,0,9,0,0],[0,0,0,5,4,0,0,0,0],[3,7,0,4,0,5,2,0,6],[0,0,0,0,0,0,5,1,0],[0,6,0,0,2,0,0,3,7]]
    grade04 = [[0,0,4,8,6,0,0,3,0],[0,0,1,0,0,0,0,9,0],[8,0,0,0,0,9,0,6,0],[5,0,0,2,0,6,0,0,1],[0,2,7,0,0,1,0,0,0],[0,0,0,0,4,3,0,0,6],[0,5,0,0,0,0,0,0,0],[0,0,9,0,0,0,4,0,0],[0,0,0,4,0,0,0,1,5]]
    grade05 = [[0,0,9,0,0,2,0,0,5],[5,3,8,0,6,4,0,0,9],[1,6,2,0,0,0,0,3,0],[0,0,3,0,2,7,0,0,0],[0,5,4,6,0,0,1,0,0],[0,0,7,0,1,5,3,4,0],[3,0,0,8,0,1,9,0,6],[7,0,0,3,0,0,8,5,0],[0,9,1,0,0,0,4,7,0]]
    print ('\nJogo Sudoku')
    print ('Escolha uma grade')
    print('Opcões de grade:\n1. Grade1\n2. Grade2\n3. Grade3\n4. Grade4\n5. Grade5' )
    escolha = input('Grade escolhida:')
    if '1' in escolha:
        matriz = grade01
    if '2' in escolha:
        matriz = grade02
    if '3' in escolha:
        matriz = grade03
    if '4' in escolha:
        matriz = grade04
    if '5' in escolha:
        matriz = grade05
    print ('A grade escolhida foi:')
    impressao(matriz)
    print ('\nComece a jogar!')
    print ('\nEscolha uma posição e um valor')
    linha = input('Linha:')
    coluna = input('Coluna:')
    valor = input('Valor:')
    while '_' not in matriz:
        if jogada_valida(matriz,linha,coluna,valor) == True:
            matriz[int(linha)-1][int(coluna)-1] = int(valor)
            print ('Sua grade atual é:')
            impressao(matriz)
            print ('\nContinue jogando!')
            print ('Escolha uma posição e um valor')
            linha = input('Linha:')
            coluna = input('Coluna:')
            valor = input('Valor:')
        else:
            print ('\nJogada inválida, tente novamente!')
            print ('Escolha uma posição e um valor')
            linha = input('Linha:')
            coluna = input('Coluna:')
            valor = input('Valor:')
            
if __name__ == '__main__':
    main()

