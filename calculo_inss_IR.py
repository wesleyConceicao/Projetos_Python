def main():
    '''Executavel que calcula os descontos do INSS e realiza os calculos da taxa de desconto
      Do imposto de renda, dado o valor do salario bruto do individuo'''
    
    # Inicio do programa
    print(" ------ BEM VINDO AO PROGRAMA DE CALCULO DO DESCONTO DO INSS ------\n")

    print("=============================================================\n")

    # Entrada do teclado pra inserir o valor do salario 
    v1 = int(input("Digite aqui o Valor Bruto do seu salario:"))
    
    print('\n')

    print("_______Resultado do Calculo______\n")
    
    # Condições para o calculo de descontos do INSS
    
    if v1 <=2000: # Desconto dado caso o salario seja menor ou igual a 2.000 reais 
        print(str.format("Será descontado do seu salario bruto {} reais", v1*0.06,"\n"))
        
    elif v1 <= 3000:  # Caso o salario seja menor ou igual a 3.000 reais 
        print("Será descontado do seu salario bruto:", v1*0.08,"\n")
        
    elif v1 > 3000:  # Caso o salario seja maior que 3.000 reais 
        print ("Será descontado do seu salario bruto:", v1*0.1,"\n")
    
    condição=input("\nDeseja calcular se desconto no Imposto de Renda. (s/n) ?: ")

    if  condição == str('s'):
        v2=int(input("\nDigite aqui o valor bruto do seu salario:"))
        print(" ")
        if v2 <=2500:
            print("Sua taxa de desconto de imposto de acordo com a tabela será de:", v2*0.11,"\n")
        elif v2<=5000:
            print("Sua taxa de desconto de imposto de acordo com a tabela será de:", v2*0.15,"\n")
        elif v2 >5000:
            print("Sua taxa de desconto de imposto de acordo com a tabela será de:", v2*0.22,"\n")
        print("----------------------F I M --- D O----P R O G R A M A ---------------------\n")
    else:
        print("----------------------F I M --- D O----P R O G R A M A ----------------------\n")
        

if __name__== "__main__":
    main()
