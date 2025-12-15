INSERT INTO clientes (cpf, nome, endereco, cidade, uf, email) VALUES
('123.456.789-00', 'Mariana da Silva', 'Rua dos Coqueiros 2300', 'Chapecó', 'SC', 'mariana@email.com'),
('987.654.321-00', 'Paulo Pereira', 'Rua Fernando Machado 600', 'Chapecó', 'SC', 'paulo@email.com'),
('456.789.123-00', 'Ana Maria Dias', 'Rua Nereu Ramos 1450', 'São Lourenço do Oeste', 'SC', 'ana@email.com'),
('111.222.333-44', 'Carlos Santos', 'Av. Getúlio Vargas 100', 'Chapecó', 'SC', 'carlos@email.com'),
('555.666.777-88', 'Julia Oliveira', 'Rua das Flores 300', 'Xanxerê', 'SC', 'julia@email.com');

INSERT INTO produtos (produto, valor, quantidade, tipo) VALUES
('Notebook Dell Inspiron', 4500.00, 10, 'Eletrônicos'),
('Smartphone Samsung Galaxy', 3200.00, 15, 'Eletrônicos'),
('Livro: Banco de Dados Avançado', 120.50, 30, 'Livros'),
('Fone de Ouvido Bluetooth', 250.00, 20, 'Acessórios'),
('Camiseta Estampada', 89.90, 50, 'Vestuário'),
('Console PlayStation 5', 4500.00, 5, 'Games'),
('Kit Maquiagem Profissional', 180.00, 25, 'Beleza'),
('Bicicleta Mountain Bike', 1500.00, 8, 'Esportes');

INSERT INTO compras (id_produto, data, id_cliente, quantidade, valor_total, amigo_indicado) VALUES
(1, '2024-12-01', 1, 1, 4500.00, 'Paulo Pereira'),
(3, '2024-11-28', 1, 2, 241.00, 'Ana Maria Dias'),
(2, '2024-11-25', 2, 1, 3200.00, 'Carlos Santos'),
(4, '2024-11-20', 3, 1, 250.00, 'Julia Oliveira'),
(5, '2024-11-15', 1, 3, 269.70, 'Paulo Pereira'),
(6, '2024-11-10', 4, 1, 4500.00, 'Mariana da Silva'),
(7, '2024-11-05', 2, 2, 360.00, 'Ana Maria Dias');