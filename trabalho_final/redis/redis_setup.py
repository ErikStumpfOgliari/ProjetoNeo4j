import redis
import json
from datetime import datetime

print("=" * 70)
print("SISTEMA DE RECOMENDAÇÃO - UNOCHAPECÓ")
print("Banco de Dados II - Trabalho Final")
print("=" * 70)

# 1. Testar conexão com Redis
try:
    r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
    if r.ping():
        print("✅ Redis conectado na porta 6379")
    else:
        print("❌ Redis não respondeu")
        exit()
except Exception as e:
    print(f"❌ Erro ao conectar no Redis: {e}")
    exit()

# 2. Limpar dados antigos
r.flushdb()
print("✅ Dados anteriores removidos")

print("\n" + "=" * 70)
print("CRIANDO DADOS DAS 4 BASES DE DADOS")
print("=" * 70)

# ============================================
# FUNÇÃO COMPATÍVEL PARA HSET (versão antiga Redis)
# ============================================
def hset_seguro(chave, dados):
    """HSET compatível com versões antigas do Redis"""
    for campo, valor in dados.items():
        r.hset(chave, campo, valor)

# ============================================
# BASE 1: POSTGRESQL (RELACIONAL)
# ============================================
print("\n📊 BASE 1: POSTGRESQL (Relacional)")

# Clientes
clientes = [
    {"id": "1", "nome": "Mariana da Silva", "cpf": "123.456.789-00", 
     "cidade": "Chapecó", "uf": "SC", "email": "mariana@email.com"},
    {"id": "2", "nome": "Paulo Pereira", "cpf": "987.654.321-00", 
     "cidade": "Chapecó", "uf": "SC", "email": "paulo@email.com"},
    {"id": "3", "nome": "Ana Maria Dias", "cpf": "456.789.123-00", 
     "cidade": "São Lourenço do Oeste", "uf": "SC", "email": "ana@email.com"},
    {"id": "4", "nome": "Carlos Santos", "cpf": "111.222.333-44", 
     "cidade": "Chapecó", "uf": "SC", "email": "carlos@email.com"},
    {"id": "5", "nome": "Julia Oliveira", "cpf": "555.666.777-88", 
     "cidade": "Xanxerê", "uf": "SC", "email": "julia@email.com"}
]

for cliente in clientes:
    chave = f"postgresql:cliente:{cliente['id']}"
    dados_completos = {
        **cliente,
        "base": "postgresql",
        "tipo": "relacional",
        "data_criacao": datetime.now().isoformat()
    }
    hset_seguro(chave, dados_completos)

print(f"✅ {len(clientes)} clientes criados")

# Produtos
produtos = [
    {"id": "1", "produto": "Notebook Dell Inspiron", "valor": "4500.00", 
     "quantidade": "10", "tipo": "Eletrônicos"},
    {"id": "2", "produto": "Smartphone Samsung Galaxy", "valor": "3200.00", 
     "quantidade": "15", "tipo": "Eletrônicos"},
    {"id": "3", "produto": "Livro: Banco de Dados Avançado", "valor": "120.50", 
     "quantidade": "30", "tipo": "Livros"},
    {"id": "4", "produto": "Fone de Ouvido Bluetooth", "valor": "250.00", 
     "quantidade": "20", "tipo": "Acessórios"},
    {"id": "5", "produto": "Camiseta Estampada", "valor": "89.90", 
     "quantidade": "50", "tipo": "Vestuário"}
]

for produto in produtos:
    chave = f"postgresql:produto:{produto['id']}"
    dados_completos = {
        **produto,
        "base": "postgresql",
        "disponivel": "sim"
    }
    hset_seguro(chave, dados_completos)

print(f"✅ {len(produtos)} produtos criados")

# Compras
compras = [
    {"id": "1", "id_cliente": "1", "id_produto": "1", "data": "2024-12-01", 
     "valor_total": "4500.00", "amigo_indicado": "Paulo Pereira"},
    {"id": "2", "id_cliente": "1", "id_produto": "3", "data": "2024-11-28", 
     "valor_total": "241.00", "amigo_indicado": "Ana Maria Dias"},
    {"id": "3", "id_cliente": "2", "id_produto": "2", "data": "2024-11-25", 
     "valor_total": "3200.00", "amigo_indicado": "Carlos Santos"},
    {"id": "4", "id_cliente": "3", "id_produto": "4", "data": "2024-11-20", 
     "valor_total": "250.00", "amigo_indicado": "Julia Oliveira"}
]

for compra in compras:
    chave = f"postgresql:compra:{compra['id']}"
    dados_completos = {
        **compra,
        "base": "postgresql",
        "status": "concluida"
    }
    hset_seguro(chave, dados_completos)

print(f"✅ {len(compras)} compras criadas")

# ============================================
# BASE 2: MONGODB (DOCUMENTOS)
# ============================================
print("\n📄 BASE 2: MONGODB (Documentos)")

interesses = [
    {
        "cliente_id": "1",
        "nome": "Mariana da Silva",
        "interesses": {
            "esportes": ["ciclismo", "yoga", "caminhada"],
            "filmes": ["romance", "comédia", "drama"],
            "musica": ["pop", "mpb", "sertanejo"],
            "hobbies": ["leitura", "culinária", "viagens"]
        },
        "data_cadastro": datetime.now().isoformat()
    },
    {
        "cliente_id": "2",
        "nome": "Paulo Pereira",
        "interesses": {
            "esportes": ["futebol", "basquete", "corrida"],
            "filmes": ["ação", "aventura", "ficção científica"],
            "musica": ["rock", "eletrônica", "hip hop"],
            "tecnologia": ["games", "computadores", "drones"]
        },
        "data_cadastro": datetime.now().isoformat()
    }
]

for i, interesse in enumerate(interesses, 1):
    chave = f"mongodb:interesses:{i}"
    r.set(chave, json.dumps(interesse, ensure_ascii=False))

print(f"✅ {len(interesses)} documentos de interesses criados")

# ============================================
# BASE 3: NEO4J (GRAFOS)
# ============================================
print("\n🕸️  BASE 3: NEO4J (Grafos)")

# Nós (clientes como grafos)
for cliente in clientes:
    chave = f"neo4j:no:cliente:{cliente['id']}"
    dados_no = {
        "id": cliente['id'],
        "nome": cliente['nome'],
        "tipo": "Cliente",
        "label": "Pessoa",
        "base": "neo4j"
    }
    hset_seguro(chave, dados_no)

print(f"✅ {len(clientes)} nós de clientes criados")

# Relações de amizade
amizades = [
    {"de": "Mariana da Silva", "para": "Paulo Pereira", "tipo": "AMIGO_DE", "desde": "2023-01-15"},
    {"de": "Paulo Pereira", "para": "Mariana da Silva", "tipo": "AMIGO_DE", "desde": "2023-01-15"},
    {"de": "Mariana da Silva", "para": "Ana Maria Dias", "tipo": "AMIGO_DE", "desde": "2022-08-20"},
    {"de": "Ana Maria Dias", "para": "Mariana da Silva", "tipo": "AMIGO_DE", "desde": "2022-08-20"},
    {"de": "Paulo Pereira", "para": "Carlos Santos", "tipo": "AMIGO_DE", "desde": "2023-05-10"},
    {"de": "Carlos Santos", "para": "Paulo Pereira", "tipo": "AMIGO_DE", "desde": "2023-05-10"},
    {"de": "Ana Maria Dias", "para": "Julia Oliveira", "tipo": "AMIGO_DE", "desde": "2024-02-01"},
    {"de": "Julia Oliveira", "para": "Ana Maria Dias", "tipo": "AMIGO_DE", "desde": "2024-02-01"}
]

for i, amizade in enumerate(amizades, 1):
    chave = f"neo4j:relacao:{i}"
    dados_completos = {
        **amizade,
        "base": "neo4j",
        "bidirecional": "sim"
    }
    hset_seguro(chave, dados_completos)

print(f"✅ {len(amizades)} relações de amizade criadas")

# Relações de indicação
indicacoes = [
    {"de": "Mariana da Silva", "para": "Paulo Pereira", "tipo": "INDICOU", 
     "produto": "Notebook Dell Inspiron", "valor": "4500.00"},
    {"de": "Mariana da Silva", "para": "Ana Maria Dias", "tipo": "INDICOU", 
     "produto": "Livro: Banco de Dados Avançado", "valor": "241.00"},
    {"de": "Paulo Pereira", "para": "Carlos Santos", "tipo": "INDICOU", 
     "produto": "Smartphone Samsung Galaxy", "valor": "3200.00"},
    {"de": "Ana Maria Dias", "para": "Julia Oliveira", "tipo": "INDICOU", 
     "produto": "Fone de Ouvido Bluetooth", "valor": "250.00"},
    {"de": "Carlos Santos", "para": "Mariana da Silva", "tipo": "INDICOU", 
     "produto": "Console PlayStation 5", "valor": "4500.00"}
]

for i, indicacao in enumerate(indicacoes, 1):
    chave = f"neo4j:indicacao:{i}"
    hset_seguro(chave, indicacao)

print(f"✅ {len(indicacoes)} relações de indicação criadas")

# ============================================
# BASE 4: REDIS (CONSOLIDADO)
# ============================================
print("\n🔑 BASE 4: REDIS (Chave-Valor Consolidado)")

# Consolidar dados de todos os clientes
for cliente in clientes:
    cliente_id = cliente['id']
    cliente_nome = cliente['nome']
    chave_consolidada = f"consolidado:cliente:{cliente_id}"
    
    # Buscar interesses
    interesses_cliente = None
    for interesse in interesses:
        if interesse['cliente_id'] == cliente_id:
            interesses_cliente = interesse['interesses']
            break
    
    # Buscar amigos
    amigos = []
    for amizade in amizades:
        if amizade['de'] == cliente_nome:
            amigos.append(amizade['para'])
    
    # Dados consolidados
    dados_consolidados = {
        **cliente,
        "interesses": json.dumps(interesses_cliente) if interesses_cliente else "{}",
        "total_amigos": str(len(amigos)),
        "amigos": ", ".join(amigos) if amigos else "Nenhum",
        "bases_integradas": "PostgreSQL, MongoDB, Neo4j",
        "status": "consolidado",
        "ultima_atualizacao": datetime.now().isoformat()
    }
    
    hset_seguro(chave_consolidada, dados_consolidados)

print(f"✅ {len(clientes)} clientes consolidados")

# ============================================
# GERAR RECOMENDAÇÕES
# ============================================
print("\n🤖 GERANDO RECOMENDAÇÕES PERSONALIZADAS")

recomendacoes_geradas = 0

for cliente in clientes[:3]:  # Limitar a 3 clientes para demo
    cliente_id = cliente['id']
    cliente_nome = cliente['nome']
    
    recomendacoes = []
    
    # 1. Recomendação baseada em compras (se houver)
    compras_cliente = [c for c in compras if c['id_cliente'] == cliente_id]
    if compras_cliente:
        compra = compras_cliente[0]
        produto_id = compra['id_produto']
        produto = next(p for p in produtos if p['id'] == produto_id)
        recomendacoes.append({
            "tipo": "historico",
            "produto": produto['produto'],
            "valor": produto['valor'],
            "motivo": f"Baseado em sua compra anterior ({compra['data']})"
        })
    
    # 2. Recomendação baseada em amigos
    amigos_cliente = [a['para'] for a in amizades if a['de'] == cliente_nome]
    if amigos_cliente:
        recomendacoes.append({
            "tipo": "rede_social",
            "produto": "Console PlayStation 5",
            "valor": "4500.00",
            "motivo": f"Popular entre seus {len(amigos_cliente)} amigos"
        })
    
    # 3. Recomendação baseada em interesses
    for interesse in interesses:
        if interesse['cliente_id'] == cliente_id:
            categorias = list(interesse['interesses'].keys())
            if categorias:
                recomendacoes.append({
                    "tipo": "interesse_pessoal",
                    "produto": "Livro Personalizado",
                    "valor": "89.90",
                    "motivo": f"Alinhado com seus interesses em {categorias[0]}"
                })
            break
    
    # Armazenar recomendações
    if recomendacoes:
        chave_rec = f"consolidado:recomendacoes:{cliente_nome}"
        dados_rec = {
            "cliente": cliente_nome,
            "cliente_id": cliente_id,
            "data_geracao": datetime.now().isoformat(),
            "total": str(len(recomendacoes)),
            "recomendacoes": json.dumps(recomendacoes, ensure_ascii=False),
            "fonte": "Sistema Integrado Unochapecó"
        }
        hset_seguro(chave_rec, dados_rec)
        recomendacoes_geradas += 1
        print(f"   ✅ {cliente_nome}: {len(recomendacoes)} recomendações")

# ============================================
# MOSTRAR RESULTADOS
# ============================================
print("\n" + "=" * 70)
print("RESULTADOS FINAIS DA INTEGRAÇÃO")
print("=" * 70)

# Contagem por base
bases = {
    "PostgreSQL": len(r.keys("postgresql:*")),
    "MongoDB": len(r.keys("mongodb:*")),
    "Neo4j": len(r.keys("neo4j:*")),
    "Consolidado": len(r.keys("consolidado:*")),
    "Total geral": len(r.keys("*"))
}

print("\n📊 ESTATÍSTICAS DO SISTEMA:")
for base, quantidade in bases.items():
    print(f"   {base:15}: {quantidade:3} registros")

# Exemplo detalhado
print("\n" + "=" * 70)
print("EXEMPLO PRÁTICO - CLIENTE 1 (MARIANA DA SILVA)")
print("=" * 70)

# Dados consolidados
cliente_data = r.hgetall("consolidado:cliente:1")
print(f"\n👤 CLIENTE CONSOLIDADO:")
print(f"   Nome: {cliente_data.get('nome')}")
print(f"   CPF: {cliente_data.get('cpf')}")
print(f"   Cidade: {cliente_data.get('cidade')}")
print(f"   Total amigos: {cliente_data.get('total_amigos')}")
print(f"   Amigos: {cliente_data.get('amigos')}")

# Interesses
if cliente_data.get('interesses') and cliente_data['interesses'] != "{}":
    interesses_data = json.loads(cliente_data['interesses'])
    print(f"\n🎯 INTERESSES (MongoDB):")
    for categoria, itens in interesses_data.items():
        print(f"   • {categoria}: {', '.join(itens[:2])}")

# Recomendações
rec_key = f"consolidado:recomendacoes:{cliente_data.get('nome')}"
if r.exists(rec_key):
    rec_data = r.hgetall(rec_key)
    print(f"\n🎁 RECOMENDAÇÕES ({rec_data.get('total')}):")
    
    recomendacoes = json.loads(rec_data.get('recomendacoes', '[]'))
    for i, rec in enumerate(recomendacoes, 1):
        print(f"\n   {i}. {rec['produto']}")
        print(f"      💰 Valor: R$ {rec['valor']}")
        print(f"      📍 Tipo: {rec['tipo']}")
        print(f"      ℹ️  Motivo: {rec['motivo']}")

print("\n" + "=" * 70)
print("✅ INTEGRAÇÃO CONCLUÍDA COM SUCESSO!")
print("=" * 70)

print("\n🎯 COMANDOS PARA TESTAR:")
print("1. Ver todas as chaves:")
print("   redis-cli KEYS '*'")
print("\n2. Ver cliente consolidado:")
print("   redis-cli HGETALL consolidado:cliente:1")
print("\n3. Ver recomendações:")
print("   redis-cli HGETALL consolidado:recomendacoes:Mariana da Silva")
print("\n4. Ver dados PostgreSQL:")
print("   redis-cli HGETALL postgresql:cliente:1")
print("\n5. Ver dados MongoDB:")
print("   redis-cli GET mongodb:interesses:1")