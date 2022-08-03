#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
#
#@author: Wesley Conceição da silva, DRE: 118096333,
#@author: Fernanda de Castro Silva Resende Batista, DRE:120059208
#@since 31/05/2021
import random
from enum import Enum

class WordList:
    #
    #    
    #
    #
    
    def __init__ (self, filename='palavras.txt'):
        
        '''constrói uma WordList, a partir de um arquivo de palavras.'''

        self.arquivo = open(filename,'r', encoding='utf-8')

        self.palavras = []

        for linha in self.arquivo:

            linha = linha.split()

            self.palavras.append(linha)


    def check (self, word):
        
        '''Retorna True se a palavra estiver no dicionário, e False caso contrário.
         Todas as palavras no dicionário estão em letras minúsculas.'''

        self.word = word

        if word in str(self.palavras):

            return True
            
        else:
                
            return False 

    def generate (self, size):
        
        '''Retorna a próxima palavra do tamanho especificado, selecionada aleatoriamente pelo objeto WordList.
          Retorna None se o dicionário não contiver palavras do tamanho especificado.'''
        
        for i in range(len(self.palavras)):
            
            if size==4 and len(str(self.palavras[i])) ==4:
                
                indice_palavra = random.randint(0, len(self.palavras))
                
                palavra_sorteada = [indice_palavra]
                
                return palavra_sorteada

            else:

                if size==5 and (len(self.palavras[i]))==5:
                
                    indice_palavra = random.randint(0, len(self.palavras))
                    
                    palavra_sorteada = [indice_palavra]
                    
                    return palavra_sorteada
                
        if size <= 3 or size >= 6:

            print("Valor Incorreto")

    def binarySearch (self , alist, word):
        
        ''' Retorna o índice de uma string "word", na lista de palavras "alist"
           ou -1 se "word" não estiver na lista.
          Deve ser executada uma busca binária, haja vista que "alist" está ordenada.'''

        self.alist = self.palavras

        if word in str(self.palavras):
            
            return self.palavras.index(str(word))
        
        else:
            
            return -1


    
##
# Enumerated type representing possible status after
# guessing a word in the BullsAndCows game .
#
class Status(Enum):
    INVALID_WORD = 1
    LOSE_TURN = 2
    KEEP_TURN = 3
    WIN = 4
    OVER = 5

class BullsAndCowsGame(WordList):
##
# Character to use as a placeholder for the hidden
# characters when displaying the " bulls ".
#
    PLACEHOLDER = '*'
    
    
    def __init__ (self , wlist = {} , arg):
        '''Constrói um novo jogo, usando o objeto WordList fornecido, como um dicionário.'''
        self.wlist = wlist
        
        self.arg = arg
        
        wlist = WordList.__init__(self,filename)

        arg = WordList.generate(self,arg)
        
        if arg == int:
            
            size = arg
            
            WordList.generate(arg)
            
        if arg == str:
            word = arg
            WordList.check(arg)
            while True:
                size = len(arg)
                WordList.generate(arg)

    def startNewRound(self):
        '''Inicia uma nova rodada do jogo, usando a próxima palavra gerada pelo objeto WordList deste jogo.'''
        if self.wlist == True:
            Wordlist.generate(arg)
            return True 
        
    def isOver (self):
        '''Retorna True se a rodada atual terminou (ou seja, não há mais letras ocultas).'''
        palavra_sorteada = self.wlist
        if (''.join(palavra_oculta)) == palavra_sorteada:
            return True

    def getSecretWord (self):
        '''Retorna a palavra secreta para esta rodada.
          A string retornada deve utilizar letras minúsculas.'''
        return self.wlist
    
    def getAllGuessedLetters (self):
        '''Retorna uma string contendo todas as letras de todas as palavras chutadas na rodada atual, sem duplicatas, na ordem em que ocorreram pela primeira vez nas tentativas dos jogadores.
         A string retornada deve estar em letras minúscula.'''
        palavra_sorteada = len(str(self.wlist))
        Letras_Chutadas = ''
        for i in range(len(palavra_sorteada)):
            if palavra[i] not in Letras_Chutadas:
                Letras_Chutadas+= palavra[i]
        return Letras_Chutadas

    def getBulls (self):
        '''Retorna a sequência com os touros revelados em suas posições e outras letras substituídas por PLACEHOLDER. Todas as letras na string retornada são minúsculas.'''
        palavra_sorteada = len(str(self.wlist))
        palavra_oculta = ['*'] * len(str(palavra_sorteada))
        palavra = input(''.join(palavra_oculta)+ '\n')
        if palavra in palavra_oculta:
            for i in range(len(palavra_sorteada)):
                if palavra_sorteada[i] == letra:
                    palavra_oculta[i] = palavra[i]
                return palavra

    def getGeese (self):
        '''Retorna uma string contendo todas as letras utilizadas na rodada atual, e que não ocorrem na palavra secreta.
          Todas as letras na string retornada são minúsculas, sem duplicatas, e a ordem das letras é a mesma que em getAllGuessedLetters().'''
        Letras_Chutadas = list(getAllGuessedLetters())
        Gansos = ''
        for i in range(len(str(palavra_sorteada))):
            if Letras_Chutadas[i] not in palavra_sorteada:
                if Letras_Chutadas[i] not in Gansos:
                    Gansos+= palavra[i]
        return Gansos
    
    def getCows (self):
        '''Retorna uma string contendo todas as letras utilizadas na rodada atual, e que ocorrem na palavra secreta.
         Todas as letras na string retornada são minúsculas, sem duplicatas, e a ordem das letras é a mesma que em getAllGuessedLetters().'''
        Letras_Chutadas = list(getAllGuessedLetters())
        Vacas = ''
        for i in range(len(palavra_sorteada)):
            if Letras_Chutadas[i] not in palavra_sorteada:
                if Letras_Chutadas[i] not in Vacas:
                    Vacas+= palavra[i]
        return Vacas
    
    def guess (self , word):
        '''Processa a tentativa de um jogador e retorna o estado apropriado. Este método não é sensível a letras maiúsculas e minúsculas.'''
        if WordList.check() is False or WordList.generate() is None:
            return Status.INVALID_WORD
        if getBulls() is False:
            return Status.LOSE_TURN
        if getBulls() is True:
            return Status.KEEP_TURN
        if isOver is True:
            return Status.WIN
        if Status.WIN is True:
            return Status.OVER
      
        
