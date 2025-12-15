from neo4j import GraphDatabase
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO)

class Neo4jDatabase:
    def __init__(self):
        self.driver = GraphDatabase.driver(
            "bolt://localhost:7687",
            auth=("neo4j", "senha1234567")  # ← SUA SENHA
        )
    
    def close(self):
        self.driver.close()
    
    def executar_query(self, query, params=None):
        """Executar uma query e retornar resultados"""
        with self.driver.session() as session:
            if params:
                resultado = session.run(query, params)
            else:
                resultado = session.run(query)
            return list(resultado)
    
    def setup_completo(self):
        print("=" * 60)
        print("CONFIGURANDO NEO4J - BASE DE GRAFOS")
        print("=" * 60)
        
        try:
            # 1. Limpar banco
            print("\n🗑️  Limpando banco...")
            self.executar_query("MATCH (n) DETACH DELETE n")
            print("✅ Banco limpo")
            
            # 2. Criar clientes (uma query separada para cada)
            print("\n👤 Criando clientes...")
            
            clientes = [
                {
                    "id": 1,
                    "cpf": "123.456.789-00",
                    "nome": "Mariana da Silva",
                    "email": "mariana@email.com",
                    "cidade": "Chapecó"
                },
                {
                    "id": 2,
                    "cpf": "987.654.321-00",
                    "nome": "Paulo Pereira",
                    "email": "paulo@email.com",
                    "cidade": "Chapecó"
                },
                {
                    "id": 3,
                    "cpf": "456.789.123-00",
                    "nome": "Ana Maria Dias",
                    "email": "ana@email.com",
                    "cidade": "São Lourenço do Oeste"
                },
                {
                    "id": 4,
                    "cpf": "111.222.333-44",
                    "nome": "Carlos Santos",
                    "email": "carlos@email.com",
                    "cidade": "Chapecó"
                },
                {
                    "id": 5,
                    "cpf": "555.666.777-88",
                    "nome": "Julia Oliveira",
                    "email": "julia@email.com",
                    "cidade": "Xanxerê"
                }
            ]
            
            for cliente in clientes:
                query = """
                CREATE (c:Cliente {
                    id: $id,
                    cpf: $cpf,
                    nome: $nome,
                    email: $email,
                    cidade: $cidade,
                    data_cadastro: date()
                })
                RETURN c.nome as nome
                """
                self.executar_query(query, cliente)
            
            print(f"✅ {len(clientes)} clientes criados")
            
            # 3. Criar amizades
            print("\n🤝 Criando amizades...")
            
            amizades = [
                ("Mariana da Silva", "Paulo Pereira", "2023-01-15", 0.8),
                ("Paulo Pereira", "Mariana da Silva", "2023-01-15", 0.8),
                ("Mariana da Silva", "Ana Maria Dias", "2022-08-20", 0.9),
                ("Ana Maria Dias", "Mariana da Silva", "2022-08-20", 0.9),
                ("Paulo Pereira", "Carlos Santos", "2023-05-10", 0.7),
                ("Carlos Santos", "Paulo Pereira", "2023-05-10", 0.7),
                ("Ana Maria Dias", "Julia Oliveira", "2024-02-01", 0.6),
                ("Julia Oliveira", "Ana Maria Dias", "2024-02-01", 0.6)
            ]
            
            for amigo1, amigo2, desde, proximidade in amizades:
                query = """
                MATCH (c1:Cliente {nome: $amigo1})
                MATCH (c2:Cliente {nome: $amigo2})
                CREATE (c1)-[:AMIGO_DE {desde: $desde, proximidade: $proximidade}]->(c2)
                """
                self.executar_query(query, {
                    "amigo1": amigo1,
                    "amigo2": amigo2,
                    "desde": desde,
                    "proximidade": proximidade
                })
            
            print(f"✅ {len(amizades)} relações de amizade criadas")
            
            # 4. Criar indicações
            print("\n🎁 Criando indicações...")
            
            indicacoes = [
                ("Mariana da Silva", "Paulo Pereira", "Notebook Dell Inspiron", "2024-12-01", 4500.00),
                ("Mariana da Silva", "Ana Maria Dias", "Livro: Banco de Dados Avançado", "2024-11-28", 241.00),
                ("Mariana da Silva", "Paulo Pereira", "Camiseta Estampada", "2024-11-15", 269.70),
                ("Paulo Pereira", "Carlos Santos", "Smartphone Samsung Galaxy", "2024-11-25", 3200.00),
                ("Paulo Pereira", "Ana Maria Dias", "Kit Maquiagem Profissional", "2024-11-05", 360.00),
                ("Ana Maria Dias", "Julia Oliveira", "Fone de Ouvido Bluetooth", "2024-11-20", 250.00),
                ("Carlos Santos", "Mariana da Silva", "Console PlayStation 5", "2024-11-10", 4500.00)
            ]
            
            for quem, para, produto, data, valor in indicacoes:
                query = """
                MATCH (c1:Cliente {nome: $quem})
                MATCH (c2:Cliente {nome: $para})
                CREATE (c1)-[:INDICOU_PARA {produto: $produto, data: date($data), valor: $valor}]->(c2)
                """
                self.executar_query(query, {
                    "quem": quem,
                    "para": para,
                    "produto": produto,
                    "data": data,
                    "valor": valor
                })
            
            print(f"✅ {len(indicacoes)} relações de indicação criadas")
            
            # 5. Mostrar resultados
            self.mostrar_resultados()
            
            print("\n" + "=" * 60)
            print("✅ NEO4J CONFIGURADO COM SUCESSO!")
            print("=" * 60)
            
        except Exception as e:
            print(f"❌ Erro durante setup: {e}")
            raise
    
    def mostrar_resultados(self):
        """Mostrar resultados do setup"""
        print("\n" + "=" * 60)
        print("RESULTADOS DO SETUP")
        print("=" * 60)
        
        # Total de nós
        query = "MATCH (n) RETURN count(n) as total_nos"
        resultado = self.executar_query(query)
        print(f"📊 Total de nós: {resultado[0]['total_nos']}")
        
        # Total de relações
        query = "MATCH ()-[r]->() RETURN count(r) as total_relacoes"
        resultado = self.executar_query(query)
        print(f"📊 Total de relações: {resultado[0]['total_relacoes']}")
        
        # Amigos de cada cliente
        print("\n👥 REDE DE AMIZADES:")
        clientes = ["Mariana da Silva", "Paulo Pereira", "Ana Maria Dias", "Carlos Santos", "Julia Oliveira"]
        
        for cliente in clientes:
            query = """
            MATCH (c:Cliente {nome: $cliente})-[:AMIGO_DE]->(amigo:Cliente)
            RETURN collect(amigo.nome) as amigos
            """
            resultado = self.executar_query(query, {"cliente": cliente})
            amigos = resultado[0]['amigos'] if resultado else []
            print(f"   • {cliente}: {', '.join(amigos) if amigos else 'Nenhum amigo'}")
        
        # Indicações
        print("\n🎁 INDICAÇÕES REALIZADAS:")
        query = """
        MATCH (c1:Cliente)-[i:INDICOU_PARA]->(c2:Cliente)
        RETURN c1.nome as de, c2.nome as para, i.produto as produto, i.valor as valor
        ORDER BY i.valor DESC
        """
        resultado = self.executar_query(query)
        
        for record in resultado:
            print(f"   • {record['de']} → {record['para']}: {record['produto']} (R$ {record['valor']:.2f})")

def main():
    try:
        db = Neo4jDatabase()
        db.setup_completo()
        db.close()
    except Exception as e:
        print(f"\n❌ ERRO CRÍTICO: {e}")
        print("\nSoluções:")
        print("1. Verifique se o Neo4j está rodando")
        print("2. Confira a senha: 'senha1234567'")
        print("3. Acesse: http://localhost:7474")
        print("4. Teste conexão: python test_neo4j.py")

if __name__ == "__main__":
    main()