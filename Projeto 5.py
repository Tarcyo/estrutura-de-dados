def selectionSort(lista,forma):
    if(forma=="c"):
        for i in range(len(lista)):
            
            aux=lista[i]
            
            for j in range(i,len(lista)):
                
                aux2=lista[j]
                
                if(aux>aux2):
                    lista[j]=aux
                    aux=aux2
                    
            lista[i]=aux


        return lista
    
    if(forma=="d"):
        for i in range(len(lista)):
            
            aux=lista[i]
            
            for j in range(i,len(lista)):
                
                aux2=lista[j]
                
                if(aux<aux2):
                    lista[j]=aux
                    aux=aux2
                    
            lista[i]=aux


        return lista
      



def main():

    lista=[9,8,7,6,5,4,3,55,1,2,3,-10,-20,-30,1312,-9999]
    print("A lista é: ",lista)
    forma=input('\nDigite "c" para ordenar em ordem crecente e "d" para ordenar em ordem decrecente: ')
    listaOrdenada=selectionSort(lista,forma)
    print("A lista ordenada é:",listaOrdenada)
    
  
       

         




  
        





  
        
    
   
    
main()
