CREATE TABLE clientes (
    id SERIAL PRIMARY KEY,
    cpf VARCHAR(14) UNIQUE NOT NULL,
    nome VARCHAR(100) NOT NULL,
    endereco VARCHAR(200),
    cidade VARCHAR(50),
    uf CHAR(2),
    email VARCHAR(100)
);

CREATE TABLE produtos (
    id SERIAL PRIMARY KEY,
    produto VARCHAR(100) NOT NULL,
    valor DECIMAL(10,2) NOT NULL,
    quantidade INT NOT NULL,
    tipo VARCHAR(50)
);

CREATE TABLE compras (
    id SERIAL PRIMARY KEY,
    id_produto INT REFERENCES produtos(id),
    data DATE NOT NULL,
    id_cliente INT REFERENCES clientes(id),
    quantidade INT NOT NULL,
    valor_total DECIMAL(10,2),
    amigo_indicado VARCHAR(100)
);

CREATE INDEX idx_clientes_cpf ON clientes(cpf);
CREATE INDEX idx_compras_cliente ON compras(id_cliente);
CREATE INDEX idx_compras_data ON compras(data);