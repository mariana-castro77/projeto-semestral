import mysql.connector
from datetime import datetime

conexao = mysql.connector.connect(host='localhost', user='root', password='senhateste', database='bd')
cursor = conexao.cursor()

def inserir():
    nome = input("Digite o nome: ")
    nascto = input("Digite a data de nascimento dd/mm/aaaa: ")
    data = datetime.strptime(nascto, "%d/%m/%Y")
    data_BD = data.strftime("%Y-%m-%d")
    sql = "INSERT INTO Usuarios (name, nascto) VALUES (%s,%s)"
    valores = (nome,data_BD)
    cursor.execute(sql, valores)   
    conexao.commit()
    print(cursor.rowcount, "registro inserido.")

def excluir():
    cod = int(input("Digite o código do usuário a ser excluído: "))
    sql = "DELETE FROM Usuarios WHERE CodUsuario = %s"
    valores = (cod,)
    cursor.execute(sql,valores)
    conexao.commit()
    print(cursor.rowcount, "registro(s) excluído(s).")

def alterar():
    nome = input("Digite o nome: ")
    cod = int(input("Digite o código do usuário a ser alterado: "))
    sql = "UPDATE Usuarios SET name = %s WHERE CodUsuario = %s"
    valores = (nome, cod)
    cursor.execute(sql,valores)
    conexao.commit()
    
def listar():
    cursor.execute("SELECT * FROM Usuarios")
    resultado = cursor.fetchall()
    for linha in resultado:
        cod = linha[0]
        nome = linha[1]
        nascto = linha[2].strftime('%d/%m/%Y') if isinstance(linha[2], datetime) else linha[2]
        print(f"CodUsuario: {cod}\nNome: {nome}\nData de Nascimento: {nascto}\n-------------------------\n")

while True:
    opcao = input("O que deseja fazer? (I)ncluir, (A)lterar, (L)istar, (E)xcluir? ou (S)air | ").upper()
    if (opcao == "S"):
        break
    elif (opcao == "I"):
        inserir()
    elif (opcao == "L"):
        listar()
    elif (opcao == "E"):
        excluir()
    elif (opcao == "A"):
        alterar()
    else:
        print("Opção inválida!")
