CREATE DATABASE clinica_estetica;
USE clinica_estetica;

CREATE TABLE tbl_profissionais (
  id_profissionais INT PRIMARY KEY AUTO_INCREMENT,
  nome_profissional VARCHAR(100) NOT NULL,
  especialidade_profissional VARCHAR(100),
  telefone_profissional VARCHAR(15)
);

CREATE TABLE tbl_agendamentos (
  id_agendamentos INT PRIMARY KEY AUTO_INCREMENT,
  data DATE NOT NULL,
  hora TIME NOT NULL,
  status VARCHAR(20) DEFAULT 'Pendente',
  servico_desejado VARCHAR(100),
  id_cliente INT,
  id_profissional INT,
  FOREIGN KEY (id_profissional) REFERENCES tbl_profissionais(id_profissionais)
    ON DELETE SET NULL ON UPDATE CASCADE
);

CREATE TABLE tbl_pagamentos (
  id_pagamentos INT PRIMARY KEY AUTO_INCREMENT,
  id_agendamento INT,
  forma_pagamento VARCHAR(50), 
  valor_procedimento DECIMAL(10,2),
  data_pagamento DATE,
  status_pagamento VARCHAR(20) DEFAULT 'Pendente',
  FOREIGN KEY (id_agendamento) REFERENCES tbl_agendamentos(id_agendamentos)
    ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE tbl_clientes (
  id_clientes INT PRIMARY KEY AUTO_INCREMENT,
  nome_cliente VARCHAR(100) NOT NULL,
  cpf_cliente VARCHAR(14) UNIQUE NOT NULL,
  telefone_cliente VARCHAR(15),
  cep_cliente VARCHAR(9),
  fk_profissionais_clientes INT,
  fk_agendamentos_clientes INT,
  fk_pagamentos_clientes INT,
  FOREIGN KEY (fk_profissionais_clientes) REFERENCES tbl_profissionais(id_profissionais),
  FOREIGN KEY (fk_agendamentos_clientes) REFERENCES tbl_agendamentos(id_agendamentos),
  FOREIGN KEY (fk_pagamentos_clientes) REFERENCES tbl_pagamentos(id_pagamentos)
);

INSERT INTO tbl_clientes (nome_cliente, cpf_cliente, telefone_cliente, cep_cliente)
VALUES 
('Isadora Lafayette', '12345678901', '11991234567', '04567000'),
('Theo Montenegro', '98765432100', '11999887766', '01311000'),
('Aurélia D’Castro', '32178965409', '11997654321', '04012001'),
('Vicente Balthazar', '74185296355', '11998889900', '05089040'),
('Catarina Valmont', '15975348622', '11993334444', '06030450'),
('Enrico Saint-Clair', '25836914777', '11994561234', '03047010'),
('Helena Fontenelle', '36925814711', '11993456789', '08210300'),
('Gael Moreau', '45612378933', '11995550123', '04304020'),
('Manuela D’Angelis', '65478912344', '11992345678', '01156000'),
('Davi Laurent', '78945612388', '11997881234', '02650000');

INSERT INTO tbl_profissionais (nome_profissional, especialidade_profissional, telefone_profissional)
VALUES
('Valentina Monteiro', 'Rinomodelação Estética', '11999887766'),
('Aurora D’Ávila', 'Harmonização Facial', '11997654321'),
('Théo Lacerda', 'Preenchimento Labial', '11995432178'),
('Isis Belmont', 'Bichectomia', '11991234000'),
('Enzo Castelan', 'Lipo de Papada', '11996789543'),
('Selena Marquez', 'Peeling de Fenol', '11997881234'),
('Gael Fontenelle', 'Bioestimulador de Colágeno', '11998889900'),
('Allegra Vasconcellos', 'Rinoplastia Não Cirúrgica', '11992345678'),
('Luna Caravaggio', 'Skinbooster Avançado', '11993456789'),
('Rafael D’Alencar', 'Toxina Botulínica Facial', '11994567890');

INSERT INTO tbl_agendamentos (data, hora, status, servico_desejado)
VALUES
('2025-04-10', '14:00:00', 'Concluído', 'Rinomodelação Estética'),
('2025-04-12', '10:30:00', 'Confirmado', 'Preenchimento Labial'),
('2025-04-15', '16:00:00', 'Pendente', 'Harmonização Facial'),
('2025-04-18', '11:00:00', 'Cancelado', 'Lipo de Papada'),
('2025-04-20', '15:00:00', 'Confirmado', 'Peeling de Fenol'),
('2025-04-22', '13:00:00', 'Pendente', 'Toxina Botulínica Facial'),
('2025-04-25', '09:00:00', 'Confirmado', 'Skinbooster Avançado'),
('2025-04-28', '17:30:00', 'Pendente', 'Bioestimulador de Colágeno'),
('2025-04-30', '12:30:00', 'Pendente', 'Bichectomia'),
('2025-05-02', '10:00:00', 'Confirmado', 'Rinoplastia Não Cirúrgica');

INSERT INTO tbl_pagamentos (forma_pagamento, valor_procedimento, data_pagamento, status_pagamento)
VALUES
('Pix', 1200.00, '2025-04-10', 'Pago'),
('Cartão de Crédito', 950.00, '2025-04-12', 'Pago'),
('Dinheiro', 2300.00, NULL, 'Pendente'),
('Pix', 1800.00, NULL, 'Cancelado'),
('Cartão de Débito', 2100.00, '2025-04-20', 'Pago'),
('Pix', 1750.00, NULL, 'Pendente'),
('Cartão de Crédito', 1990.00, '2025-04-25', 'Pago'),
('Pix', 1600.00, NULL, 'Pendente'),
('Dinheiro', 2200.00, '2025-04-30', 'Pago'),
('Cartão de Crédito', 2500.00, NULL, 'Confirmando');

UPDATE tbl_clientes
SET fk_profissionais_clientes = 1,
    fk_agendamentos_clientes = 1,
    fk_pagamentos_clientes = 1
WHERE id_clientes = 1;

UPDATE tbl_clientes
SET fk_profissionais_clientes = 3,
    fk_agendamentos_clientes = 2,
    fk_pagamentos_clientes = 2
WHERE id_clientes = 2;

UPDATE tbl_clientes
SET fk_profissionais_clientes = 2,
    fk_agendamentos_clientes = 3,
    fk_pagamentos_clientes = 3
WHERE id_clientes = 3;

UPDATE tbl_clientes
SET fk_profissionais_clientes = 5,
    fk_agendamentos_clientes = 4,
    fk_pagamentos_clientes = 4
WHERE id_clientes = 4;

UPDATE tbl_clientes
SET fk_profissionais_clientes = 6,
    fk_agendamentos_clientes = 5,
    fk_pagamentos_clientes = 5
WHERE id_clientes = 5;

UPDATE tbl_clientes
SET fk_profissionais_clientes = 10,
    fk_agendamentos_clientes = 6,
    fk_pagamentos_clientes = 6
WHERE id_clientes = 6;

UPDATE tbl_clientes
SET fk_profissionais_clientes = 9,
    fk_agendamentos_clientes = 7,
    fk_pagamentos_clientes = 7
WHERE id_clientes = 7;

UPDATE tbl_clientes
SET fk_profissionais_clientes = 7,
    fk_agendamentos_clientes = 8,
    fk_pagamentos_clientes = 8
WHERE id_clientes = 8;

UPDATE tbl_clientes
SET fk_profissionais_clientes = 4,
    fk_agendamentos_clientes = 9,
    fk_pagamentos_clientes = 9
WHERE id_clientes = 9;

UPDATE tbl_clientes
SET fk_profissionais_clientes = 8,
    fk_agendamentos_clientes = 10,
    fk_pagamentos_clientes = 10
WHERE id_clientes = 10;

SELECT 
    tbl_clientes.nome_cliente,
    tbl_profissionais.nome_profissional,
    tbl_agendamentos.id_agendamentos,
    tbl_pagamentos.id_pagamentos
FROM tbl_clientes
INNER JOIN tbl_profissionais 
    ON tbl_clientes.fk_profissionais_clientes = tbl_profissionais.id_profissionais
INNER JOIN tbl_agendamentos 
    ON tbl_clientes.fk_agendamentos_clientes = tbl_agendamentos.id_agendamentos
INNER JOIN tbl_pagamentos 
    ON tbl_clientes.fk_pagamentos_clientes = tbl_pagamentos.id_pagamentos;
    USE clinica_estetica;
    SELECT 
    c.nome_cliente, 
    p.nome_profissional, 
    a.data, 
    a.hora, 
    a.status AS status_agendamento, 
    a.servico_desejado, 
    pag.forma_pagamento, 
    pag.valor_procedimento, 
    pag.data_pagamento, 
    pag.status_pagamento
FROM tbl_clientes c
INNER JOIN tbl_profissionais p ON c.fk_profissionais_clientes = p.id_profissionais
INNER JOIN tbl_agendamentos a ON c.fk_agendamentos_clientes = a.id_agendamentos
INNER JOIN tbl_pagamentos pag ON c.fk_pagamentos_clientes = pag.id_pagamentos;



