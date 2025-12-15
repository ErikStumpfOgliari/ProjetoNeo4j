from pymongo import MongoClient

def testar_conexao():
    print("Testando conexão com MongoDB...")
    
    try:
        # Tentar conexão
        client = MongoClient('mongodb://localhost:27017/', serverSelectionTimeoutMS=3000)
        
        # Testar ping
        client.admin.command('ping')
        print("✅ MongoDB está rodando!")
        
        # Listar bancos
        dbs = client.list_database_names()
        print(f"📁 Bancos disponíveis: {dbs}")
        
        # Verificar nosso banco
        if 'recomendacao_db' in dbs:
            db = client['recomendacao_db']
            colecoes = db.list_collection_names()
            print(f"📄 Coleções em 'recomendacao_db': {colecoes}")
            
            if 'interesses' in colecoes:
                colecao = db['interesses']
                total = colecao.count_documents({})
                print(f"📊 Documentos na coleção 'interesses': {total}")
                
                # Mostrar um documento
                doc = colecao.find_one()
                if doc:
                    print(f"\n📝 Exemplo de documento:")
                    print(f"   Nome: {doc.get('nome')}")
                    print(f"   ID: {doc.get('cliente_id')}")
        
        return True
        
    except Exception as e:
        print(f"❌ Falha na conexão: {e}")
        print("\nPara iniciar o MongoDB:")
        print("1. Abra um novo terminal")
        print("2. Execute: mongod")
        print("OU com Docker:")
        print("docker run -d -p 27017:27017 --name mongodb mongo")
        return False

if __name__ == "__main__":
    testar_conexao()