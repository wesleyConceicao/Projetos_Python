################################
##########CALCULO DE DESCONTOS DO INSS E DO IMPOSTO DE RENDA########
##@wesley Conceição
##email:mendesrog282@gmail.com
################################

import sys

class Desconto():
    
    def __init__(self, nome):
        '''Um objeto da classe desconto com o atributo nome'''
        
        self.nome= nome

    def calculo_INSS(self, salario):
        '''Função que calcula o valor de desconto do INSS de acordo com a tabela do inss dado o salario bruto;'''

        self.salario = salario

        if  self.salario <= 1100:
                
            print( "\nOlá Sr.{}, seu desconto do INSS é de R${} reais".format(self.nome, self.salario*0.075))
                
        elif  self.salario >=1101 and self.salario <= 2203:
                
            print( "\nOlá Sr.{}, seu desconto do INSS é de R${} reais".format(self.nome,self.salario*0.09))

        elif self.salario >= 2204 and self.salario <=3305:

            print( "\nOlá Sr.{}, seu desconto do INSS é de R${} reais".format(self.nome,self.salario*0.12))
                
        elif  self.salario  >= 3306 and self.salario <= 6443:
                
            print( "\nOlá Sr.{}, seu desconto do INSS é de R${} reais".format(self.nome,self.salario*0.14))

    def calculo_IR(self, salario):
        
         "funçao que calcula a taxa de desconto de IR de acordo com a tabela do INSS;"

         if self.salario <= 2500:

             print("\nPorém, você é isento de declarar o imposto de renda")

         elif self.salario > 2500 and self.salario <= 3200:

             print("\nSua taxa de desconto de IR, de acordo com a tabela será de: R${} reais\n".format(self.salario*0.075))

         elif self.salario > 3200 and self.salario <= 4250:

            print("\nSua taxa de desconto de IR, de acordo com a tabela será de: R${} reais\n".format(self.salario*0.15))

         elif self.salario > 4250 and self.salario <= 5300:

            print("\nSua taxa de desconto de IR, de acordo com a tabela será de: R${} reais \n".format(self.salario*0.225))

         else:

            if self.salario > 5300:

                print("\nSua taxa de desconto de imposto de acordo com a tabela será de: R${} reais \n".format(self.salario*0.275))

    def  resultado (self, valor):

        "função que retorna o valor do salario liquido com os descontos do IR e INSS;"


        print("\nDado os descontos de INSS e IR, o seu salario liquido é de R${} reais".format((self.salario) - (self.calculo_INSS(self.salario)) + (self.calculo_IR(self.salario))))


def main ():
    print("==================================")

    print('__DESCONTO_DO_IMPOSTO_DE_RENDA __')

    print("==================================")

    nome_cliente=input("\nOlá, Digite seu Nome:")
    
    n= Desconto(nome_cliente)
    
    salario_cliente=int(input('\nDigite aqui o Salario:'))
    
    n.calculo_INSS(salario_cliente)

    n.calculo_IR(salario_cliente)

    print(n.resultado(salario_cliente))


    while True:
        
        print("=============================")

        condição=input('\nDeseja calcular Novamente (y/n)?:')

        print("=============================")


        if condição == 'y':

            nome_cliente=input("\nDigite seu Nome:")
                
            n= Desconto(nome_cliente)
                
            salario_cliente=int(input('\nDigite aqui o Salario:'))
                
            n.calculo_INSS(salario_cliente)

            n.calculo_IR(salario_cliente)

            continue

        else:

            if condição == 'n':

                print("==============================")

                print( '_______FIM__DO___PROGRAMA_____')

                print("==============================")

                break


if __name__ == "__main__":

    sys.exit(main())
    













        
        
