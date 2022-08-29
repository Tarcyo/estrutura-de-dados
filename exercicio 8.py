def main():

    nomeArquivo=input("Digite o nome do arquivo: ")
    arquivo=open(nomeArquivo)
    lista=[]

    for linha in arquivo:
        lista.append(linha)

    arquivo.close()
    while(True):
        numeroDaLinha=int(input("Digite o numero da linha: "))
        if(numeroDaLinha==0):
            print("Fim do programa.")
            return

        else:
            print(lista[numeroDaLinha-1])
    
        
        
    
    


    
main()
