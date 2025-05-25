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
        print("ID:", c[0])
        print("Nome:", c[1])
        print("CPF:", c[2])
        print("Telefone:", c[3])
        print("CEP:", c[4])
        print("----------")

def alterar_cliente():
    listar_clientes()
    id_alterar = input("Digite o ID do cliente que deseja alterar: ")
    nome = input("Novo nome: ")
    cpf = input("Novo CPF: ")
    telefone = input("Novo telefone: ")
    cep = input("Novo CEP: ")
    sql = "UPDATE tbl_clientes SET nome_cliente=%s, cpf_cliente=%s, telefone_cliente=%s, cep_cliente=%s WHERE id_clientes=%s"
    valores = (nome, cpf, telefone, cep, id_alterar)
    cursor.execute(sql, valores)
    conexao.commit()
    print("Cliente alterado com sucesso.")
    print("----------")

def excluir_cliente():
    listar_clientes()
    id_excluir = input("Digite o ID do cliente que deseja excluir: ")
    sql = "DELETE FROM tbl_clientes WHERE id_clientes = %s"
    cursor.execute(sql, (id_excluir,))
    conexao.commit()
    print("Cliente excluído.")
    print("----------")

def inserir_profissional():
    nome = input("Nome do profissional: ")
    especialidade = input("Especialidade: ")
    telefone = input("Telefone: ")
    sql = "INSERT INTO tbl_profissionais (nome_profissional, especialidade_profissional, telefone_profissional) VALUES (%s, %s, %s)"
    cursor.execute(sql, (nome, especialidade, telefone))
    conexao.commit()
    print("Profissional inserido.")
    print("----------")

def listar_profissionais():
    cursor.execute("SELECT * FROM tbl_profissionais")
    for p in cursor.fetchall():
        print("ID:", p[0])
        print("Nome:", p[1])
        print("Especialidade:", p[2])
        print("Telefone:", p[3])
        print("----------")

def alterar_profissional():
    listar_profissionais()
    id_alterar = input("Digite o ID do profissional que deseja alterar: ")
    nome = input("Novo nome: ")
    especialidade = input("Nova especialidade: ")
    telefone = input("Novo telefone: ")
    sql = "UPDATE tbl_profissionais SET nome_profissional=%s, especialidade_profissional=%s, telefone_profissional=%s WHERE id_profissionais=%s"
    cursor.execute(sql, (nome, especialidade, telefone, id_alterar))
    conexao.commit()
    print("Profissional alterado.")
    print("----------")

def excluir_profissional():
    listar_profissionais()
    id_excluir = input("Digite o ID do profissional que deseja excluir: ")
    cursor.execute("DELETE FROM tbl_profissionais WHERE id_profissionais=%s", (id_excluir,))
    conexao.commit()
    print("Profissional excluído.")
    print("----------")

def inserir_agendamento():
    data = input("Data do agendamento (dd/mm/aaaa): ")
    hora = input("Hora do agendamento (HH:MM): ")
    status = input("Status do agendamento: ")
    servico = input("Serviço desejado: ")
    id_cliente = input("ID do cliente: ")
    id_profissional = input("ID do profissional: ")
    data_sql = datetime.strptime(data, "%d/%m/%Y").strftime("%Y-%m-%d")
    hora_sql = hora + ":00"
    sql = "INSERT INTO tbl_agendamentos (data, hora, status, servico_desejado, id_cliente, id_profissional) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(sql, (data_sql, hora_sql, status, servico, id_cliente, id_profissional))
    conexao.commit()
    print("Agendamento registrado.")
    print("----------")

def listar_agendamentos():
    cursor.execute("SELECT * FROM tbl_agendamentos")
    for a in cursor.fetchall():
        print("ID:", a[0])
        print("Data:", a[1])
        print("Hora:", a[2])
        print("Status:", a[3])
        print("Serviço:", a[4])
        print("ID Cliente:", a[5])
        print("ID Profissional:", a[6])
        print("----------")

def excluir_agendamento():
    listar_agendamentos()
    id_excluir = input("Digite o ID do agendamento que deseja excluir: ")
    cursor.execute("DELETE FROM tbl_agendamentos WHERE id_agendamentos=%s", (id_excluir,))
    conexao.commit()
    print("Agendamento excluído.")
    print("----------")

def inserir_pagamento():
    id_agendamento = input("ID do agendamento: ")
    forma = input("Forma de pagamento: ")
    valor = input("Valor do procedimento: ")
    data_pag = input("Data do pagamento (AAAA-MM-DD, ou deixe vazio): ")
    if data_pag.strip() == "":
        data_pag = None
    status = input("Status do pagamento: ")
    sql = "INSERT INTO tbl_pagamentos (id_agendamento, forma_pagamento, valor_procedimento, data_pagamento, status_pagamento) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(sql, (id_agendamento, forma, valor, data_pag, status))
    conexao.commit()
    print("Pagamento inserido.")
    print("----------")

def listar_pagamentos():
    cursor.execute("SELECT * FROM tbl_pagamentos")
    for p in cursor.fetchall():
        print("ID:", p[0])
        print("ID Agendamento:", p[1])
        print("Forma de pagamento:", p[2])
        print("Valor do procedimento:", p[3])
        print("Data do pagamento:", p[4])
        print("Status do pagamento:", p[5])
        print("----------")

def excluir_pagamento():
    listar_pagamentos()
    id_excluir = input("Digite o ID do pagamento que deseja excluir: ")
    cursor.execute("DELETE FROM tbl_pagamentos WHERE id_pagamentos=%s", (id_excluir,))
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
