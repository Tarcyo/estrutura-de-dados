class Array(object):
     """
     Representa um array
     """
     
     def __init__(self, capacity, fillValue = None):

          # define  tamanho lógico:
         self.logicalSize=0


         
         self.items = list()


         
         
         for count in range(capacity):
             self.items.append(fillValue)




         
     def __len__(self):
         """->A capacidade do array"""
         return len(self.items)





     def __str__(self):
         """ A representação de string do array"""
         return str(self.items)




     def __iter__(self):
         """suporta o percurso com um laço for """
         return iter(self.items)

     def __getitem__(self, index):
         """ Operador de subscrtio para acesso no índice."""
         
         # A pré-condição adicionada faz retonar nulo e printa uma mensagem de erro se a posição não existir:
         if(index>=len(self.items))or(index<0):
              print("ERRO!!!! A Posição "+str(index)+" não existe!!!")
              return None
              
         return self.items[index]





     def __setitem__(self,index,newItem):

        



         
         # A pré-condição adicionada faz retonar nulo e printa uma mensagem de erro se a posição não existir:
         if(index>=len(self.items))or(index<0):
              print("ERRO!!!! A Posição "+str(index)+" não existe!!!")
              return None
         

         #O tamanho lógico só aumenta se a posição estiver vazia naquele momento.
         if(self.items[index]==None):
              self.logicalSize=self.logicalSize+1
        

         self.items[index]=newItem



     def size(self):
        #Retorna o tamanho lógico
        return self.logicalSize
     
     pass


