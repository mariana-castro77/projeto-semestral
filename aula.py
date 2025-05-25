import mysql.connector
from datetime import datetime

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
    database='clinica_estetica'
)
cursor = conexao.cursor()

def inserir_cliente():
    nome = input("Nome: ")
    cpf = input("CPF: ")
    telefone = input("Telefone: ")
    cep = input("CEP: ")
    sql = "INSERT INTO tbl_clientes (nome_cliente, cpf_cliente, telefone_cliente, cep_cliente) VALUES (%s, %s, %s, %s)"
    valores = (nome, cpf, telefone, cep)
    cursor.execute(sql, valores)
    conexao.commit()
    print("Cliente inserido com sucesso.")
    print("----------")

def listar_clientes():
    cursor.execute("SELECT * FROM tbl_clientes")
    for c in cursor.fetchall():
        print(c)
    print("----------")

def alterar_cliente():
    id = input("ID do cliente: ")
    nome = input("Novo nome: ")
    cpf = input("Novo CPF: ")
    telefone = input("Novo telefone: ")
    cep = input("Novo CEP: ")
    sql = "UPDATE tbl_clientes SET nome_cliente=%s, cpf_cliente=%s, telefone_cliente=%s, cep_cliente=%s WHERE id_clientes=%s"
    valores = (nome, cpf, telefone, cep, id)
    cursor.execute(sql, valores)
    conexao.commit()
    print("Cliente alterado com sucesso.")
    print("----------")

def excluir_cliente():
    id = input("ID do cliente: ")
    cursor.execute("DELETE FROM tbl_clientes WHERE id_clientes = %s", (id,))
    conexao.commit()
    print("Cliente excluído.")
    print("----------")

def inserir_profissional():
    nome = input("Nome do profissional: ")
    especialidade = input("Especialidade: ")
    sql = "INSERT INTO tbl_profissionais (nome_profissional, especialidade) VALUES (%s, %s)"
    cursor.execute(sql, (nome, especialidade))
    conexao.commit()
    print("Profissional inserido.")
    print("----------")

def listar_profissionais():
    cursor.execute("SELECT * FROM tbl_profissionais")
    for p in cursor.fetchall():
        print(p)
    print("----------")

def alterar_profissional():
    id = input("ID do profissional: ")
    nome = input("Novo nome: ")
    especialidade = input("Nova especialidade: ")
    sql = "UPDATE tbl_profissionais SET nome_profissional=%s, especialidade=%s WHERE id_profissional=%s"
    cursor.execute(sql, (nome, especialidade, id))
    conexao.commit()
    print("Profissional alterado.")
    print("----------")

def excluir_profissional():
    id = input("ID do profissional: ")
    cursor.execute("DELETE FROM tbl_profissionais WHERE id_profissional=%s", (id,))
    conexao.commit()
    print("Profissional excluído.")
    print("----------")

def inserir_agendamento():
    id_cliente = input("ID do cliente: ")
    id_prof = input("ID do profissional: ")
    data = input("Data do agendamento (dd/mm/aaaa): ")
    valor = input("Valor do serviço: ")
    data_sql = datetime.strptime(data, "%d/%m/%Y").strftime("%Y-%m-%d")
    sql = "INSERT INTO tbl_agendamentos (id_cliente, id_profissional, data_agendamento, valor_servico) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (id_cliente, id_prof, data_sql, valor))
    conexao.commit()
    print("Agendamento registrado.")
    print("----------")

def listar_agendamentos():
    cursor.execute("SELECT * FROM tbl_agendamentos")
    for a in cursor.fetchall():
        print(a)
    print("----------")

def excluir_agendamento():
    id = input("ID do agendamento: ")
    cursor.execute("DELETE FROM tbl_agendamentos WHERE id_agendamento=%s", (id,))
    conexao.commit()
    print("Agendamento excluído.")
    print("----------")

def inserir_pagamento():
    id_agendamento = input("ID do agendamento: ")
    forma = input("Forma de pagamento: ")
    sql = "INSERT INTO tbl_pagamentos (id_agendamento, forma_pagamento) VALUES (%s, %s)"
    cursor.execute(sql, (id_agendamento, forma))
    conexao.commit()
    print("Pagamento inserido.")
    print("----------")

def listar_pagamentos():
    cursor.execute("SELECT * FROM tbl_pagamentos")
    for p in cursor.fetchall():
        print(p[0])
    print("----------")

def excluir_pagamento():
    id = input("ID do pagamento: ")
    cursor.execute("DELETE FROM tbl_pagamentos WHERE id_pagamento=%s", (id,))
    conexao.commit()
    print("Pagamento excluído.")
    print("----------")

def menu():
    while True:
        print("\nMENU PRINCIPAL")
        print("1 - Clientes")
        print("2 - Profissionais")
        print("3 - Agendamentos")
        print("4 - Pagamentos")
        print("0 - Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            submenu("cliente")
        elif escolha == "2":
            submenu("profissional")
        elif escolha == "3":
            submenu("agendamento")
        elif escolha == "4":
            submenu("pagamento")
        elif escolha == "0":
            break
        else:
            print("Opção inválida.")
        print("----------")

def submenu(tipo):
    while True:
        print(f"\nMenu - {tipo.capitalize()}")
        print("1 - Inserir")
        print("2 - Listar")
        print("3 - Alterar")
        print("4 - Excluir")
        print("0 - Voltar")
        opc = input("Escolha uma opção: ")

        if tipo == "cliente":
            if opc == "1": inserir_cliente()
            elif opc == "2": listar_clientes()
            elif opc == "3": alterar_cliente()
            elif opc == "4": excluir_cliente()
            elif opc == "0": break
        elif tipo == "profissional":
            if opc == "1": inserir_profissional()
            elif opc == "2": listar_profissionais()
            elif opc == "3": alterar_profissional()
            elif opc == "4": excluir_profissional()
            elif opc == "0": break
        elif tipo == "agendamento":
            if opc == "1": inserir_agendamento()
            elif opc == "2": listar_agendamentos()
            elif opc == "3": print("Alteração de agendamento não implementada.")
            elif opc == "4": excluir_agendamento()
            elif opc == "0": break
        elif tipo == "pagamento":
            if opc == "1": inserir_pagamento()
            elif opc == "2": listar_pagamentos()
            elif opc == "3": print("Alteração de pagamento não implementada.")
            elif opc == "4": excluir_pagamento()
            elif opc == "0": break
        else:
            print("Opção inválida.")
        print("----------")

menu()