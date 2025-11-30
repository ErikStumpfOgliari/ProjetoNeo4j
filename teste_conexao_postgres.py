import psycopg2

def testar_conexao_postgres():
    print("🧪 TESTANDO CONEXÃO POSTGRESQL")
    print("=" * 35)
    
    try:
        # Tente diferentes combinações
        configs = [
            {
                'host': 'localhost',
                'database': 'postgres',  # Database padrão
                'user': 'postgres',
                'password': '8520',  # ⚠️ SUA SENHA
                'port': 5433
            },
            {
                'host': '127.0.0.1',  # IP local
                'database': 'postgres',
                'user': 'postgres', 
                'password': '8520',
                'port': 5433
            }
        ]
        
        for i, config in enumerate(configs, 1):
            print(f"\n🔧 Tentativa {i}: {config['host']}:{config['port']}")
            try:
                conn = psycopg2.connect(**config)
                print("✅ CONEXÃO BEM-SUCEDIDA!")
                
                # Criar nosso database
                conn.autocommit = True
                with conn.cursor() as cursor:
                    try:
                        cursor.execute("CREATE DATABASE alunos_db")
                        print("✅ Database 'alunos_db' criado")
                    except Exception as e:
                        print(f"⚠️ Database já existe: {e}")
                
                conn.close()
                print("🎉 POSTGRESQL CONFIGURADO COM SUCESSO!")
                return True
                
            except Exception as e:
                print(f"❌ Falha: {e}")
        
        print("\n💡 SOLUÇÕES:")
        print("1. Verifique se o serviço PostgreSQL está RUNNING")
        print("2. Confirme a senha do usuário 'postgres'")
        print("3. Abra 'services.msc' e inicie o PostgreSQL")
        return False
        
    except Exception as e:
        print(f"❌ Erro geral: {e}")
        return False

if __name__ == "__main__":
    testar_conexao_postgres()