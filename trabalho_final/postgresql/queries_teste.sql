-- ============================================
-- QUERIES PARA TESTE E DEMONSTRAÇÃO
-- ============================================

-- 1. Total de clientes
SELECT COUNT(*) as total_clientes FROM Clientes;

-- 2. Clientes e suas compras
SELECT 
    c.nome as cliente,
    COUNT(co.id) as total_compras,
    SUM(co.valor_total) as valor_total_gasto
FROM Clientes c
LEFT JOIN Compras co ON c.id = co.id_cliente
GROUP BY c.id, c.nome
ORDER BY valor_total_gasto DESC;

-- 3. Produtos mais vendidos
SELECT 
    p.produto,
    p.tipo,
    SUM(co.quantidade) as quantidade_vendida,
    SUM(co.valor_total) as valor_total_vendas
FROM Produtos p
JOIN Compras co ON p.id = co.id_produto
GROUP BY p.id, p.produto, p.tipo
ORDER BY quantidade_vendida DESC;

-- 4. Amigos mais indicados
SELECT 
    amigo_indicado,
    COUNT(*) as vezes_indicado,
    SUM(valor_total) as valor_total_indicacoes
FROM Compras 
WHERE amigo_indicado IS NOT NULL
GROUP BY amigo_indicado
ORDER BY vezes_indicado DESC;

-- 5. Últimas compras com detalhes
SELECT 
    c.nome as cliente,
    p.produto,
    co.data,
    co.quantidade,
    co.valor_total,
    co.amigo_indicado
FROM Compras co
JOIN Clientes c ON co.id_cliente = c.id
JOIN Produtos p ON co.id_produto = p.id
ORDER BY co.data DESC
LIMIT 10;