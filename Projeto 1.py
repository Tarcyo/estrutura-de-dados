def main():

    lista=[1,2,3,4,5,7,8,9]
 

    alvo=int(input("Digite um valor a ser procurado: "))
   
    numInteracoes=0;
    for i in lista:

        numInteracoes=numInteracoes+1
        if(alvo<i):
            print("O valor não está na lista!\nO numero de interações foi:",numInteracoes)
            return
        elif(alvo==i):
            print("O valor está na lista!\nO numero de interações foi:",numInteracoes)
            return

    print("O valor não está na lista!\nO numero de interações foi:",numInteracoes)

    

#O pior caso será aquele em que o valor a ser procurado será maior que o ultimo elemento da lista, portanto o algoritmo irá passar por todas as posições e terá complexidade O(n).
#O melhor caso será aquele que o valor a ser procurado é menor ou igual ao primeiro elemento da lista, assim a complexidade será O(1).
#O caso médio é aquele em que exite um valor maior que o valor a ser procurado no em algum lugar meio da lista, ou o valor está em algum lugar no meio da lista, portanto a complexidade será de O(n + 1)/2.

    
    

       
        
        


    


    


    
main()
