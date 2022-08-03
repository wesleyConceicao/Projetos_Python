#!/usr/bin/env python
# coding: UTF-8
#
import random

def main():
    "Funcao que verifica se a letra informada esta contida na palavra"
    tentativas=0
    l=[]
   
    # Importa o arquivo frase.txt
    with open('frase.txt','r') as f:
        
        #abre um aquivo frase.txt e lê o que esta dentro do arquivo
        #Feito isso, é criado a variavel que em que vai estar o arquivo txt
        
        palavras=f.readlines()
        
    #A palavra sorteada vai estar dentro do alcance e isso dentro do indice_palavra
    #já a palavra sorteada é referenete ao indice de palavras em aleatorio que vão ser sorteadas 
    #palavra_oculta esconde a palavra sorteada isso com os asteriscos 
    #
    
    indice_palavra = random.randint(0, len(palavras)-1)
    palavra_sorteada = palavras[indice_palavra].replace('\n','')
    palavra_oculta = ['*'] * len(palavra_sorteada)
    palavra=palavra_sorteada
    
    print("_______BULLS AND COWS TEST_________\n")

    print (palavra_oculta,'\n')
    
    while True:
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
                    #caso a letra certa esteja dentro da palavra sorteada 
                    palavra = palavra[:i] + letra + palavra[i+1:]                    
                elif palavra_sorteada[i] in l:
                    palavra = palavra[:i] + palavra_sorteada[i] + palavra[i+1:]
                else:
                    palavra = palavra[:i] + '*' + palavra[i+1:]
            l.append(letra)
            print(palavra)
            
        else:
            # caso voce erre uma das letras inseridas ele gera mais uma tentativa 
            tentativas+=1
            print ('Não é a letra certa\n')
            print(palavra)
                
            if tentativas == 8 :
                #caso o numero de tentativas sejam iguais a 8 o jogo acaba
                ##
                #e acaso não tenha acertado, voce perde o jogo 
                print("Você tentou", tentativas, "vezes\n")
                print("A palavra certa é",palavra_sorteada,'\n') 
                print ('______VOCE PERDEU_____\n')
                break
            
        if palavra == palavra_sorteada:
            # se a condição for verdadeira e a palavra for igual a palavra sorteada, voce vence o jogo 
            print ('____VOCE VENCEU____\n')
            print("A palavra certa é", palavra_sorteada,'\n')
            break
# Acrescentar a ideia dos acentos e etc 
# 
#
#
#
if "__main__"==__name__:
    main()
