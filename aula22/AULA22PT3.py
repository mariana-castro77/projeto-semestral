def CalcularMedia (n1,n2):
    media = (n1 + n2)/2
    return round(media,2)

nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))

mediaFinal = CalcularMedia(nota1,nota2)