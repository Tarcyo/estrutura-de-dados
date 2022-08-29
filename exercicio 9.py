from random import randint
import math
def main():
    
    menorNumero=int(input("Entre com o menor número: "))
    maiorNumero=int(input("Entre com o maior número: "))
    numeros=[]
    
    for i in range(menorNumero,maiorNumero+1):
       numeros.append(i)

    maximoDeSuposicoes=int(math.log2(maiorNumero-menorNumero))+1


    

    for i in range(maximoDeSuposicoes):

        
        numeroAleatorio=randint(numeros[0],numeros[len(numeros)-1]);
        print("Seu número é: ",numeroAleatorio)
        entrada=input("Entre =, < ou >: ")

        
        if(entrada=="<"):
            
            novaLista=[]
            for j in numeros:
                if(j<numeroAleatorio):
                    novaLista.append(j)
            numeros=novaLista
            
        if(entrada==">"):
            
            novaLista=[]
            for j in numeros :
                if(j>numeroAleatorio):
                    novaLista.append(j)
            numeros=novaLista

            
        if(entrada=="="):
            
            print("Uau! Eu acertei em ",i+1," tentativas!")
            return
        




        
    print("Você está trapaceando!")
                          
                           
                           
                           
       
    
   

    
main()
