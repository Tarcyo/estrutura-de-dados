import math

def main():
    raio=float(input("Digite o raio da esfera: "))
    diametro=raio*2
    circunferencia=diametro*math.pi
    areaDaSuperficie=4*math.pi*(raio**2)
    volume=(4*math.pi*(raio**3))/3
    print("\n\nO valor do diametro é:",diametro,"\nO valor da circunferencia é: ",circunferencia,"\nO valor da area da superfie é:",areaDaSuperficie,"\nO valor do volume da esfera é:",volume)
    return







main()
    
