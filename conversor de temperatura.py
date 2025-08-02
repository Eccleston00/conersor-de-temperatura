#criar a class
from time import sleep
class Conversor:
    def __init__(self,nome,*opcoes):
        self.__nome=nome
        self.__opcoes=opcoes
    #criando interface
    def interface(self):
        print('='*60)
        print(f'{self.__nome}'.center(60))
        print('='*60)
    # exibindo opcoes  enumeradas e formatadas
    def exibindo_opcoes(self):
        print('Suas opcoes:')
        for n,valor in enumerate(self.__opcoes):
            print(f'\n\033[36m{n+1}\033[m- \033[33m{valor}\033[m')
    #validar escolha
    def validar(self):
        
        while True:
            try:
                
                contador=len(self.__opcoes)

                while True:
                
                    opc=int(input('digite a sua opcao:'))
                    if  opc <=0 \
                        or opc >contador:
                        print(f'\033[31m valor invalido por favor digite novamente! \033[m')
                    else:
                        break
                
            except ValueError:
                print('\033[31m por favor digite valores numericos \033[m')
            except:
                print('\033[31m Ocorreu um erro por favor digite novamente \033[m')
            else:
                return opc
    # convertendo
    #celsius
    def fahrenheit_celsius(self,F=0):
        C=round(F-32)*(5/9) #round  aredonda para decimal
        

        print('Convertendo', end='', flush=True)

        for i in range(1, 101):
            if i % 10 == 0:  # imprime um ponto a cada 10%
                print('.', end='', flush=True)
            print(f'\rConvertendo{"."*(i//10)} {i}%', end='', flush=True)
            sleep(0.01)

        print()  # nova linha final


        print(f'Convertendo {F}°F para graus Celsius da: {C}°C ')

    #fahrenheit
    def celsius_fahrenheit(self, C=0):
        F = round(C * 9 / 5 + 32)
        
        #<< round >>  aredonda para decimal

        print('Convertendo', end='', flush=True)

        for i in range(1, 101):
            if i % 10 == 0:  # imprime um ponto a cada 10%
                print('.', end='', flush=True)
            print(f'\rConvertendo{"."*(i//10)} {i}%', end='', flush=True)
            sleep(0.01)

        print()  # nova linha final

        return F
        print(f'Convertendo {C}°C para graus Fahrenheit da: {F}°F ')
        
    
# rodando
graus=Conversor('Conversor de temperatura (Celsius/Fahrenheit) ','Graus Celsius C° para Graus Fahrenheit F°','Graus Fahrenheit F° para Graus Celsius C°')
graus.interface()
graus.exibindo_opcoes()
escolha=graus.validar()
if escolha== 1:
    print('\nQuantos Graus Celsius? ') #resolver todos erros do tipo str ou int
    quantidade=float(input('por favor digite valores numericos:'))    
    graus.celsius_farenheit(quantidade)
else:
    print('Quantos Graus Fahrenheit? ')
    quantidade=float(input('por favor digite valores numericos:'))
    graus.fahrenheit_celsius(quantidade)


#despedida
print('\n=======================volte sempre!=======================')
