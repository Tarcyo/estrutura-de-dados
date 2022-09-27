class No(object):
    #contrutor
    def __init__(self,dado,proximo=None):

        self.dado=dado
        self.proximo=proximo

    #Printando;
    def printa(self):
        copia=self

    
        while(copia!=None):
            print(copia.dado)
            copia=copia.proximo
            
    #Pesquisando pelo valor:
    def pesquisaPeloValor(self, valor):
        
        copia=self
        
        while(copia!=None and valor!=copia.dado):
            copia=copia.proximo


        if(copia!=None):
            print("O valor "+str(valor)+" foi encontrado!")
        else:
            print("O valor "+str(valor)+" NÃO foi encontrado!")

        
    #Pesquisando pelo valor:
    def __getitem__(self,index):
        
         if index<0:
             print("a posição "+str(index)+" não exite!")
             return None

             
         copia=self
         i=index
         while i>0:
             copia=copia.proximo
             i=i-1
             if(copia==None):
                 print("a posição "+str(index)+" não exite!")
                 return None
        
         
         

         return copia.dado

    


    #Substituindo pelo valor:
    def substituiPeloValor(self,valorAntigo,valorNovo):
        copia=self
        while copia !=None and copia.dado !=valorAntigo:
            copia=copia.proximo


        if copia !=None:

            copia.dado=valorNovo
            return True
        else:
            return False

    #Substituindo pelo index:
    def __setitem__(self,index,valor):
         if index<0:
             print("a posição "+str(index)+" não exite!")
             return None

             
         copia=self
         i=index
         while i>0:
             copia=copia.proximo
             i=i-1
             if(copia==None):
                 print("a posição "+str(index)+" não exite!")
                 return None
        
         
         

         copia.dado=valor



    #Inserindo no incio:
    def insereNoInicio(self,valor):
        self=No(valor,self)
        return self


    #Inserindo no final:
    def insereNoFinal:
        
        
        
        
        
       
        
        
        
            
   
                
        
        
    
     
    
            
                
            
        
         
         
         
        
            
                
            
            
        


    pass

    
def main():
    
    extrutura=No(0)
    print("Inserindo valores do inicio:")
    for i in range(1,10):
       extrutura=extrutura.insereNoInicio(i)
        
    print("Os valores da extrutura são:")
    extrutura.printa()
    print("Procurando o valor 5 na extrutura: ")
    extrutura.pesquisaPeloValor(5)
    print("Procurando o valor 20 na extrutura: ")
    extrutura.pesquisaPeloValor(20)
    print("Buscando posicão numero 2 da extrutura: ",extrutura[2])
    print("Tentando substituir o valor 2 por 333 o programa retorna:",extrutura.substituiPeloValor(2,333))
    print("Tentando substituir o valor 20 por 3 o programa retorna:",extrutura.substituiPeloValor(20,333))
    print("Substituindo o valor da posicao 0 por 66:")
    extrutura[0]=66
    print("Após as substituições a extrutura fica:")
    extrutura.printa()
    
        
        

    
    
    
main()
