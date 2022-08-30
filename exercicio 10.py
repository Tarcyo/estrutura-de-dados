class Student:
    
    
    nome=""
    pontos=[]

    def __repr__(self):
        a="Nome: "+self.nome
        for i in range(len(self.pontos)):
            a=a+"\nPonto: "+(str(i+1))+" : "+str(self.pontos[i])
        return a
    
    def __init__(self,nome,quantPontuacoes):
        self.nome=nome
        for i in range(quantPontuacoes):
            self.pontos.append(0)

            
    def acessaPontuacao(self,indice):
        return self.pontos[(indice-1)]
    

    def substituiPontuacao(self,indice,novaPontuacao):
        self.pontos[indice]=novaPontuacao
        

    def obtemNumeroPontuacoes(self):
        return len(self.pontos)
    
    
    def obtemPontuacaoMaisAlta(self):
        pontosOrdenados=[]
        for i in self.pontos:
            pontosOrdenados.append(i)

        pontosOrdenados.sort()
        return pontosOrdenados[len(pontosOrdenados)-1]

    def obtemMedia(self):
        somatorio=0
        for i in self.pontos:
            somatorio=somatorio+int(i)


        return somatorio/len(self.pontos)

    def obtemNomeDoAluno(self):
        return self.nome

    
    
    
      
        

 
    pass





def teste():
    
  nomeDoAluno=input("Digite o nome do aluno: ")
  quantPontuacoes=int(input("Digite a quantdade de pontuações: "))
  
    
  aluno=Student(nomeDoAluno,quantPontuacoes)
  
  for i in range(quantPontuacoes):
      ponto=float(input("Digite o ponto "+str(i+1)+": "))
      aluno.substituiPontuacao(i,ponto)

  a=int(input("Digite um numero de pontuacao para ser acessada: "))
  print("O valor dessa pontuacao é:",aluno.acessaPontuacao(a))

  print("\n\nO nome do aluno é: ",aluno.obtemNomeDoAluno())
  print("A quantidade de pontuacões é de: ",aluno.obtemNumeroPontuacoes())
  print("A pontuacao mais alta é de: ",aluno.obtemPontuacaoMaisAlta())
  print("A media é de: ",aluno.obtemMedia())
  print("\n\nO objeto completo é: \n",aluno)
 
  return




teste()








    

    

