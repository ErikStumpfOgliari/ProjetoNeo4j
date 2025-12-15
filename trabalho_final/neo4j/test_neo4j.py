from neo4j import GraphDatabase

def testar_conexao_neo4j():
    print("Testando conexão com Neo4j...")
    
    try:
        # Tente conectar
        driver = GraphDatabase.driver(
            "bolt://localhost:7687",
            auth=("neo4j", "senha1234567")  # ALTERE A SENHA!
        )
        
        # Testar conexão
        with driver.session() as session:
            resultado = session.run("RETURN 'Conexão OK' as teste")
            record = resultado.single()
            print(f"✅ {record['teste']}")
        
        # Verificar versão
        with driver.session() as session:
            resultado = session.run("CALL dbms.components() YIELD name, versions RETURN name, versions")
            for record in resultado:
                print(f"📊 {record['name']}: {record['versions'][0]}")
        
        driver.close()
        return True
        
    except Exception as e:
        print(f"❌ Erro: {e}")
        print("\nPara configurar Neo4j:")
        print("1. Instale Neo4j Desktop")
        print("2. Crie um novo projeto")
        print("3. Inicie o banco")
        print("4. Anote a senha (não use 'neo4j/neo4j')")
        print("\nOU use Docker:")
        print("   docker run -d -p 7687:7687 -p 7474:7474 \\")
        print("     -e NEO4J_AUTH=neo4j/suasenha neo4j")
        return False

if __name__ == "__main__":
    testar_conexao_neo4j()