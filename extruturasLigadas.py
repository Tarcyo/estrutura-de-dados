class No(object):


    
    #Contrutor:
    def __init__(self,dado,proximo=None):

        self.dado=dado
        self.proximo=proximo












    #Printando:
    def __str__(self):
        copia=self
        texto="["
    
        while(copia!=None):
            if(copia.proximo==None):

                texto=texto+str(copia.dado)

                
                
            else:
                
                texto=texto+str(copia.dado)+","
                
                
                
            copia=copia.proximo

        texto=texto+"]"   
        return texto




            



    #Pesquisando pelo valor:
    def pesquisaPeloValor(self, valor):
        
        copia=self
        
        while(copia!=None and valor!=copia.dado):
            copia=copia.proximo


        if(copia!=None):
            print("O valor "+str(valor)+" foi encontrado!")
        else:
            print("O valor "+str(valor)+" NÃO foi encontrado!")




        



    #Pesquisando pelo index:
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
        self.proximo=No(self.dado,self.proximo)
        self.dado=valor
        
            




     
        

    #Inserindo no final:
    def insereNoFinal(self,valor):
        no=No(valor)
        if(self is None):
            self=no
            return
        
        copia=self
        while(copia.proximo!=None):
            copia=copia.proximo
        
        copia.proximo=no




    #Inserindo em qualquer posição:
    def insereEmQualquerPosicao(self,valor,index):
         if index<0:
             print("a posição "+str(index)+" não exite!")
             return None

             
         copia=self
         i=index
         while i>1:
             copia=copia.proximo
             i=i-1
             if(copia==None):
                 print("a posição "+str(index)+" não exite!")
                 return None


         copia.proximo=No(valor,copia.proximo)








    #Removendo no inicio:
    def removeNoInicio(self):
        if(self.proximo==None):
            retorno=self.dado
            self.dado=None
            return retorno
        else:
            removido=self.dado
            self.dado=self.proximo.dado
            self.proximo=self.proximo.proximo
            return removido









        
    #Removendo no final:
    def removeNoFinal(self):
        removido=self.dado
        if(self.proximo is None):
            self.dado=None
            
        else:
            copia=self
            while(copia.proximo.proximo!=None):
                copia=copia.proximo
            removido=copia.proximo.dado
            copia.proximo=None
            
        return removido
            






            
        
    #Removendo em qualquer posição:
    def removeEmQualquerPosicao(self,index):
        if index<0:
            print("a posição "+str(index)+" não exite!")
            return None

                 
        copia=self
        i=index
             
        while i>1:
            copia=copia.proximo
            i=i-1
            if(copia==None):
                print("a posição "+str(index)+" não exite!")
                return None

             
        removido = copia.proximo.dado
        copia.proximo=copia.proximo.proximo
        return removido

         
         

        
            
    pass

    
def main():
    extrutura=No(0)
    print("A estrutura inicialmente é: ",extrutura)
    for i in range(1,11):
        extrutura.insereNoInicio(i)

    
    print("Após inserir numeros no inicio a estrutura fica: ",extrutura)
    print("pesquisando o valor 5 ele retona: ")
    extrutura.pesquisaPeloValor(5)
    print("pesquisando o valor 20 ele retona: ")
    extrutura.pesquisaPeloValor(20)
    print("buscando a posicão 4 da extrutura: ",extrutura[4])
    print("buscando a posicão 30 da extrutura(Não existe): ")
    print(extrutura[30])
    extrutura.substituiPeloValor(3,450)
    print("susbstituindo o valor 3 por 450 na extrutura: ",extrutura)
    extrutura[6]=78
    print("susbstituindo a posição 6 por 78: ",extrutura)
    extrutura.insereNoFinal(360)
    print("inserindo o valor 360 no final da extrutura ",extrutura)
    extrutura.removeEmQualquerPosicao(1)
    print("removendo a posição 1 da extrura: ",extrutura)
    extrutura.removeNoInicio()
    extrutura.removeNoFinal()
    print("Após remover os itens do inicio e do final a extrutura fica: ",extrutura)
    
    
    
    
main()
