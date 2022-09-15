def reverse(lista):
    listaInvertida=[]

    for i in range(len(lista)):
        listaInvertida.append(lista.pop(len(lista)-1))

   

    return listaInvertida


def main():
    
    lista=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    print("A lista é: ",lista)
    listaInvertida=reverse(lista)
    print("A lista invertida é: ",listaInvertida)
    
    
main()

#A complexidade desse algortmo sempre será O(n) pois sempre precisará percorrer todos os elementos da lista para inverte-la. 



    
    

