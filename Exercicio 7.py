def mediana(lista):
    lista.sort()
    posicaoDoMeio=int(len(lista)/2)
    return lista[posicaoDoMeio]
    
def modo(lista):
    quantMaisAparece=0
    indice=0
    numeroMaisAparece=lista[0]
    for num in lista:
        if(quantMaisAparece<lista.count(num)):
           numeroMaisAparece=lista[indice]
           quantMaisAparece=lista.count(num)
    
        indice=indice+1

    return numeroMaisAparece
           
def  mean(lista):
     somatorio=0
     for num in lista:
         somatorio=somatorio+num
     return float(somatorio/len(lista))
     
    
def main():
    lista=[21,22,23,24,25,26,27,28,25,26,26]
    print("A media é: ",mean(lista))
    print("A mediana é: ",mediana(lista))
    print("O modo é: ",modo(lista))
    
   
  
        
    



    
main()
