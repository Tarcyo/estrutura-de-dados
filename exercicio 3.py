def main():
    altura=float(input("Digite a altura: "))
    quantVezes=int(input("Digite a quantidade de vezes que a bola pode continuar quicando: "))
    distancia=0.0;

    for i in range(quantVezes):
        distancia=distancia+(altura+(altura*0.6))
        altura=altura*0.6


    print("A distancia percorrida pela bola foi de: ",distancia)
    
    return



main()
