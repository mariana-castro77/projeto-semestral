cont=0
while True:
    nome = str(input("entre com seu nome :"))
    peso = float(input("entre com seu peso :"))
    altura = float(input("entre com a sua altura:"))
    imc = peso/altura**2
    if (imc<18.5):
        print("abaixo do peso.")
    elif(imc<25):
        print("peso ideal.")
    elif(imc<30):
        print("sobrepeso")
    elif(imc<35):
        print("obesidade grau 1.")
    elif(imc<40):
        print("obesidade grau 2.")
    else:
        print("obesidade grave")
    cont = cont + 1
    opcao = str(input("deseja fazer novo calculo. S - Sim ou N - Não"))
    if(opcao == "N"):
            break 
print("total de calculos realizados :", cont)