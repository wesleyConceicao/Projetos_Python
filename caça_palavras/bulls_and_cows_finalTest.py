#!/usr/bin/env python
#coding: UTF-8
#

import random

def play():
    "Funcao que verifica se a letra informada esta contida na palavra"
   
    # Importa o arquivo frase.txt
    arquivo = open('palavras.txt','r',encoding='utf-8')

    palavras = []

    tentativas= 0

    let=[]

        
    #abre um aquivo frase.txt e lê o que esta dentro do arquivo
    #Feito isso, é criado a variavel que em que vai estar o arquivo txt
        
        
    #A palavra sorteada vai estar dentro do alcance e isso dentro do indice_palavra
    #já a palavra sorteada é referenete ao indice de palavras em aleatorio que vão ser sorteadas 
    #palavra_oculta esconde a palavra sorteada isso com os asteriscos

    for linha in arquivo:

        linha = linha.strip()

        palavras.append(linha)

    arquivo.close()
    
    palavra_sorteada = random.choice(palavras)# ou um randrange

    palavra = palavra_sorteada
    
    oculta_palavra = ['*']*len(palavra_sorteada)
    
    
    print("_______BULLS AND COWS TEST_________\n")

    print (oculta_palavra,'\n')

    print(palavra_sorteada,'\n')


    
    while True :

        
        letra = input('Informe uma letra:')
        
        print(" ")
        #
        # Enquanto a for verdadeiro a condição ele entra com o teclado para o jogador inserir a palavra 
        #
        #
        #
        if letra in palavra_sorteada:

            
            for i in range(len(palavra_sorteada)):
                
                if palavra_sorteada[i] == letra:

                    palavra = palavra[:i] + letra + palavra[i+1:]

                elif palavra_sorteada[i] in let:

                    palavra= palavra[:i] + palavra_sorteada[i] + palavra[i+1:]
                    
                else:

                    palavra = palavra[:i] + '*' + palavra[i+1:]

            let.append(letra)
                 
        else:
            # caso voce erre uma das letras inseridas ele gera mais uma tentativa
            
            if letra not in palavra:

                tentativas+=1

                print(tentativas)
            
                print ('Não é essa letra certa\n')

            elif tentativas == 8:
                #caso o numero de tentativas sejam iguais a 8 o jogo acaba
                #e acaso não tenha acertado, voce perde o jogo
                
                print("Você tentou", tentativas, "vezes\n")

                print ('______VOCE PERDEU_____\n')

                break

        if palavra == palavra_sorteada:
            # se a condição for verdadeira e a palavra for igual a palavra sorteada, voce vence o jogo
            
            print ('____VOCE VENCEU____\n')

            break

        print(palavra)

    print('A palavra certa é {}'.format(palavra_sorteada),'\n')

    print("==========FIM DE JOGO===========")

    print("=====DESEJA JOGAR DE NOVO??=====")
    
    
#
# 
#
#
#
if "__main__"==__name__:
    play()
