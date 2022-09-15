def expo(numero,expoente):
    if(expoente<0):
        print("O expoente deve ser maior que 0")
        return "ERRO!!!"
    total=1;
    for i in range(expoente):
        total=total*numero

    return total
        


        
def main():
    numero=int(input("Digite o numero: "))
    expoente=int(input("Digite o expoente: "))
    resultado=expo(numero,expoente)
    print("O resultado é:",resultado)
    
main()
# A complexidade desse algortmo será O(n), onde n será o valor do expoente.
