from Array import Array
def main():
    array=Array(10)
    array[1]=11
    array[2]=22
    array[3]=33
    array[4]=44
    array[5]=55

    print("O valor na quarta posição de numero 4 do array é :",array[4])
    print("O tamanho físico do array é: ",len(array))
    print("O tamanho lógico do array é: ",array.size())
    print("O array completo é",array)
    print("Se tentarmos buscar a posição 20 do array ocorrerá um erro: ")
    print(array[20])
    
    
   


main()
