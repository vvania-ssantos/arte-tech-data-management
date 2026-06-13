-- Arquivo de Configuração Inicial e Carga de Dados - Arte-tech
-- Data: 18/05/2026

-- 1. Criação das Tabelas (Se não existirem)
CREATE TABLE IF NOT EXISTS fornecedores (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    tipo_plataforma VARCHAR(50) DEFAULT 'Online'
);

CREATE TABLE IF NOT EXISTS insumos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    caracteristica_cor VARCHAR(50),
    preco_total_pago DECIMAL(10,2) NOT NULL,
    quantidade_comprada DECIMAL(10,2) NOT NULL,
    unidade_medida VARCHAR(20) NOT NULL,
    fornecedor_id INTEGER REFERENCES fornecedores(id),
    data_compra DATE DEFAULT CURRENT_DATE
);

CREATE TABLE IF NOT EXISTS ativos_ferramentas (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    preco_pago DECIMAL(10,2) NOT NULL,
    fornecedor_id INTEGER REFERENCES fornecedores(id),
    data_compra DATE DEFAULT CURRENT_DATE
);

-- 2. Carga de Dados Reais (Notas Fiscais de 18/05/2026)

-- Cadastra o fornecedor principal caso ainda não exista
INSERT INTO fornecedores (id, nome, tipo_plataforma) 
VALUES (1, 'Mercado Livre', 'Online / Full')
ON CONFLICT (id) DO NOTHING;

-- Insere o Kit de Ferramentas Real (Ativo fixo)
INSERT INTO ativos_ferramentas (nome, preco_pago, fornecedor_id, data_compra)
VALUES ('Kit Agulha Crochê Bordado Tesoura Fita - 53 Itens', 37.90, 1, '2026-05-18');

-- Insere a matéria-prima exata das Notas Fiscais
INSERT INTO insumos (nome, caracteristica_cor, preco_total_pago, quantidade_comprada, unity_medida, fornecedor_id, data_compra) VALUES
('Barbante Número 4 Amazonia', 'Branco - 08', 22.95, 1.00, 'unidades', 1, '2026-05-18'),
('Kit 10 Fechos Mosquetão Cadeado', 'Gold', 15.75, 10.00, 'unidades', 1, '2026-05-18'),
('Fio Náutico Rr-04 100m', 'Fio 1', 18.05, 100.00, 'metros', 1, '2026-05-18'),
('Fio Náutico Rr-04 100m', 'Fio 2', 18.05, 100.00, 'metros', 1, '2026-05-18'),
('Fio Náutico Rr-04 100m', 'Fio 3', 18.05, 100.00, 'metros', 1, '2026-05-18'),
('Fio Náutico Rr-04 100m', 'Fio 4', 18.05, 100.00, 'metros', 1, '2026-05-18');