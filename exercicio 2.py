def main():
    salarioPorHora=float(input("Digite o salario por hora: "))
    horasRegulares=float(input("Digite as horas regulares: "))
    horasExtras=float(input("Digite a quantidade de horas extras: "))
    pagamento=(salarioPorHora*horasRegulares)+(salarioPorHora*(horasExtras*1.5))
    print("O pagameto semanal total é: ",pagamento)
    

    return


main()
