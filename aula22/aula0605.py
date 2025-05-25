def incluir(novo):
    nomes.append(novo)
    print("Nome incluido com sucesso!")
    listar()

def listar():
    print("---------------")
    print("Relação de Nomes cadastrados")
    for i in range(len(nomes )):
        print(nomes[i])
    print("---------------")

nomes = []
while True:
    opcao = input("Escolha a opção:\n(I)ncluir\n(L)istar\n(E)xcluir\n(S)air\nOpção desejada:").upper()
    if (opcao == "I"):
        novo = input("Qual o nome a ser incluido? ")
        incluir(novo)
    elif (opcao == "L"):
        listar()
    elif (opcao == "E"):
        valor = input("Qual o nome a ser excluido?")
        excluir(valor) 
    elif (opcao == "S"):
        break                              
    else:
        print("Opção inválida!")