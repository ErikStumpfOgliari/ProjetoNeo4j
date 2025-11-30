from neo4j import GraphDatabase

URI = "bolt://localhost:7687"
USER = "neo4j"
PASSWORD = "senha1234567"  

def test_connection():
    try:
        driver = GraphDatabase.driver(URI, auth=(USER, PASSWORD))
        
        print("🔗 Conectando ao Neo4j Desktop...")
        
        with driver.session(database="projetoneounochapeco") as session:
            # Teste básico
            result = session.run("RETURN 'Conexão bem-sucedida!' as mensagem")
            print("✅ " + result.single()["mensagem"])
            
            # Criar primeiro nó
            session.run("CREATE (p:Projeto {nome: 'Projeto Unochapecó', disciplina: 'Banco de Dados II'})")
            print("✅ Nó do projeto criado")
            
            # Consultar para verificar
            nodes = session.run("MATCH (p:Projeto) RETURN p.nome as nome")
            for record in nodes:
                print(f"📄 Nó encontrado: {record['nome']}")
            
        driver.close()
        print("🎉 Ambiente Neo4j configurado com sucesso!")
        return True
        
    except Exception as e:
        print(f"❌ Erro na conexão: {e}")
        return False

if __name__ == "__main__":
    test_connection()