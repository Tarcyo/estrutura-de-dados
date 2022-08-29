
def main():
    
    precoDeCompra=float(input("Digite o preço de compra: "))
    print("O pagamento inicial foi de: ",precoDeCompra*0.1)
    precoDeCompra=precoDeCompra-(precoDeCompra*0.1)
    saldoAtual=precoDeCompra
    print("%50s"%"TABELA:\n")
    print("Mês:    Saldo Atual:    Juros:    Pricipal:    Pagamento:    Saldo Remanecente:    ")

    numeroMes=1
    while(saldoAtual>0):
        juros=saldoAtual*0.01
        pagamentoMensal=precoDeCompra*0.05
        valorPrincipal=pagamentoMensal-juros
        if(saldoAtual>=pagamentoMensal):
           saldoRemanecente=saldoAtual-pagamentoMensal+juros
        else:
            pagamentoMensal=saldoRemanecente
            valorPrincipal=pagamentoMensal-juros
            saldoRemanecente=0
        print(numeroMes,"%12.2f"%saldoAtual,"%13.2f"%juros,"%11.2f"%valorPrincipal,"%11.2f"%pagamentoMensal,"%15.2f"%saldoRemanecente)
        saldoAtual=saldoRemanecente
        numeroMes=numeroMes+1
        
        
        
    
    
        
   
   
    

main()
