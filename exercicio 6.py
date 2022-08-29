def main():
    nomeArquivo=input("Digite o nome do arquivo: ")
    arquivo=open(nomeArquivo,'r')
    print("                             TABELA:")
    print("Nome:            Salario Por Hora:            Horas Trabalhadas:\n")
    
    for linha in arquivo:
        palavra=""
        for c in linha:
            if(c==' '):
                palavra=palavra+"                        "
               
            
            palavra=palavra+c

        
        
            
        print(palavra)
      
            
            
        
        
     
          
           

    
main()
