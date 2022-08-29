def main():
    
    numInt=int(input("Digite o numero de interações: "))

    somatorio=0
    denominador=1
    numerador=1

    for i in range(numInt):
        somatorio=somatorio+(numerador/denominador)
        numerador=numerador*(-1)
        denominador=denominador+2

    pi=somatorio*4
    
    print("O valor resultante de PI é: ",pi)
        
        

    
      


   

    



main()
