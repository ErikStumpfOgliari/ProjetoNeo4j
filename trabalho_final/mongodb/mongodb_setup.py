from pymongo import MongoClient
from datetime import datetime

def configurar_mongodb():
    print("=" * 60)
    print("CONFIGURANDO MONGODB - BASE DE DOCUMENTOS")
    print("=" * 60)
    
    try:
        # Conectar ao MongoDB
        client = MongoClient('mongodb://localhost:27017/', serverSelectionTimeoutMS=5000)
        
        # Testar conexão
        client.admin.command('ping')
        print("✅ Conexão com MongoDB estabelecida!")
        
        # Criar/aceder ao banco
        db = client['recomendacao_db']
        
        # Coleção para interesses
        colecao_interesses = db['interesses']
        
        # Dados de exemplo
        interesses_clientes = [
            {
                "cliente_id": 1,
                "cpf": "123.456.789-00",
                "nome": "Mariana da Silva",
                "email": "mariana@email.com",
                "cidade": "Chapecó",
                "interesses": {
                    "esportes": ["ciclismo", "yoga", "caminhada"],
                    "filmes": ["romance", "comédia", "drama"],
                    "musica": ["pop", "mpb", "sertanejo"],
                    "hobbies": ["leitura", "culinária", "viagens"],
                    "tecnologia": ["smartphones", "notebooks", "tablets"]
                },
                "recomendacoes": ["Notebook Dell Inspiron", "Kit Maquiagem Profissional"],
                "data_atualizacao": datetime.now()
            },
            {
                "cliente_id": 2,
                "cpf": "987.654.321-00",
                "nome": "Paulo Pereira",
                "email": "paulo@email.com",
                "cidade": "Chapecó",
                "interesses": {
                    "esportes": ["futebol", "basquete", "corrida"],
                    "filmes": ["ação", "aventura", "ficção científica"],
                    "musica": ["rock", "eletrônica", "hip hop"],
                    "hobbies": ["games", "carros", "tecnologia"],
                    "tecnologia": ["consoles", "computadores", "drones"]
                },
                "recomendacoes": ["Console PlayStation 5", "Bicicleta Mountain Bike"],
                "data_atualizacao": datetime.now()
            },
            {
                "cliente_id": 3,
                "cpf": "456.789.123-00",
                "nome": "Ana Maria Dias",
                "email": "ana@email.com",
                "cidade": "São Lourenço do Oeste",
                "interesses": {
                    "esportes": ["pilates", "natação", "dança"],
                    "filmes": ["romance", "animação", "documentário"],
                    "musica": ["clássica", "jazz", "bossanova"],
                    "hobbies": ["pintura", "jardinagem", "artesanato"],
                    "tecnologia": ["smartphones", "tablets"]
                },
                "recomendacoes": ["Livro: Banco de Dados Avançado", "Fone de Ouvido Bluetooth"],
                "data_atualizacao": datetime.now()
            },
            {
                "cliente_id": 4,
                "cpf": "111.222.333-44",
                "nome": "Carlos Santos",
                "email": "carlos@email.com",
                "cidade": "Chapecó",
                "interesses": {
                    "esportes": ["surf", "skate", "musculação"],
                    "filmes": ["suspense", "terror", "ação"],
                    "musica": ["rock", "metal", "punk"],
                    "hobbies": ["games", "música", "festas"],
                    "tecnologia": ["consoles", "headphones", "smart tvs"]
                },
                "recomendacoes": ["Smartphone Samsung Galaxy", "Console PlayStation 5"],
                "data_atualizacao": datetime.now()
            },
            {
                "cliente_id": 5,
                "cpf": "555.666.777-88",
                "nome": "Julia Oliveira",
                "email": "julia@email.com",
                "cidade": "Xanxerê",
                "interesses": {
                    "esportes": ["dança", "yoga", "meditação"],
                    "filmes": ["romance", "comédia", "drama"],
                    "musica": ["pop", "k-pop", "indie"],
                    "hobbies": ["moda", "maquiagem", "fotografia"],
                    "tecnologia": ["smartphones", "câmeras", "smartwatch"]
                },
                "recomendacoes": ["Camiseta Estampada", "Kit Maquiagem Profissional"],
                "data_atualizacao": datetime.now()
            }
        ]
        
        # Limpar coleção existente
        colecao_interesses.delete_many({})
        print("✅ Coleção 'interesses' limpa!")
        
        # Inserir dados
        resultado = colecao_interesses.insert_many(interesses_clientes)
        print(f"✅ {len(resultado.inserted_ids)} documentos inseridos!")
        
        # Mostrar estatísticas
        print("\n" + "=" * 60)
        print("ESTATÍSTICAS DO MONGODB")
        print("=" * 60)
        print(f"📊 Banco de dados: {db.name}")
        print(f"📊 Coleção: {colecao_interesses.name}")
        print(f"📊 Total documentos: {colecao_interesses.count_documents({})}")
        
        # Mostrar alguns dados
        print("\n" + "=" * 60)
        print("EXEMPLO DE DOCUMENTOS")
        print("=" * 60)
        
        for doc in colecao_interesses.find().limit(2):
            print(f"\n👤 Cliente: {doc['nome']}")
            print(f"   ID: {doc['cliente_id']} | Email: {doc['email']}")
            print(f"   Interesses principais: {list(doc['interesses'].keys())}")
            print(f"   Recomendações: {doc['recomendacoes']}")
        
        print("\n" + "=" * 60)
        print("✅ MONGODB CONFIGURADO COM SUCESSO!")
        print("=" * 60)
        
        return True
        
    except Exception as e:
        print(f"❌ ERRO: {e}")
        print("\nSoluções possíveis:")
        print("1. Verifique se o MongoDB está rodando: mongod")
        print("2. Inicie com Docker: docker run -d -p 27017:27017 mongo")
        print("3. Verifique a conexão: mongosh")
        return False

if __name__ == "__main__":
    configurar_mongodb()