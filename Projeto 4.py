
def expo(numero,expoente):
   print("1")
   if(expoente==0):
       
       return 1
      
  
   if(expoente%2!=0):
       
       return numero*expo(numero,expoente-1)
   
   if(expoente%2==0):
      
       return (expo(numero,expoente/2))**2
       


        
def main():
    numero=int(input("Digite o numero: "))
    expoente=int(input("Digite o expoente: "))
    resultado=expo(numero,expoente)
    print("O resultado é:",resultado)



main()
 
