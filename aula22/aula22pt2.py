vazia = []
idades = [2,4,6,8,10]
notas = [9.0,10.0,8.5,7.8]
cores = ["azul","verde","rose","branco"]
zeradas = [0]*5
strings = [""]*4
print(vazia)
print(idades)
print(notas)
print(cores)
print(zeradas)
print(strings)

idades = [2,4,6,8,10,15,18,25,35,3,11,77,45,48,33]

print("--- Imprimindo com While ---")
i=0
while (i < len (idades)):
    print(idades[i])
    i = i + 1

print("--- Imprimindo com For ---")
i = 0
for i in range(0,len(idades),1):
    print(idades[i])
    
idades = [2,4,6,8,10,15,18,25,35,3,11,77,45,48,33]
print("--- Imprimindo o vetor idades ---")
print(idades)

idades.append(99)
print("\n\n\n--- Imprimindo o vetor idades ---")
print(idades)

nomes = [""]*5
print(nomes)

print("Entre com 5 nomes: ")
for i in range(len(nomes)):
    nomes[i]=input()
print(nomes)

def CalcularMedia (n1,n2):
    media = (n1 + n2)/2
    return round(media,2)

nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))

mediaFinal = CalcularMedia(nota1,nota2)
