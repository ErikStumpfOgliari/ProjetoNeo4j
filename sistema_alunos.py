import redis
import psycopg2
from psycopg2 import sql

class SistemaAlunos:
    def __init__(self):
        # Configurações Redis - SEM CHARSET
        self.redis_client = redis.Redis(
            host='localhost',
            port=6379,
            db=0,
            decode_responses=True
        )
        
        # Configurações PostgreSQL
        self.pg_conn = psycopg2.connect(
            host='localhost',
            database='alunos_db',
            user='postgres',
            password='8520',
            port=5433
        )
        self.pg_conn.autocommit = True
        
        print("✅ Conexões estabelecidas: Redis + PostgreSQL")
    
    def close(self):
        self.redis_client.close()
        self.pg_conn.close()
        print("🔌 Conexões fechadas")
    
    def pg_create_tables(self):
        with self.pg_conn.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS alunos (
                    id SERIAL PRIMARY KEY,
                    nome VARCHAR(100) NOT NULL,
                    curso VARCHAR(50) NOT NULL,
                    email VARCHAR(100) UNIQUE NOT NULL,
                    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            print("✅ Tabela 'alunos' criada no PostgreSQL")
    
    def pg_create_aluno(self, nome, curso, email):
        with self.pg_conn.cursor() as cursor:
            cursor.execute("""
                INSERT INTO alunos (nome, curso, email) 
                VALUES (%s, %s, %s) RETURNING id
            """, (nome, curso, email))
            aluno_id = cursor.fetchone()[0]
            print(f"✅ Aluno {aluno_id} criado no PostgreSQL: {nome}")
            return aluno_id
    
    def pg_read_aluno(self, aluno_id):
        with self.pg_conn.cursor() as cursor:
            cursor.execute("SELECT * FROM alunos WHERE id = %s", (aluno_id,))
            aluno = cursor.fetchone()
            if aluno:
                print(f"📖 PostgreSQL - ID: {aluno[0]}, Nome: {aluno[1]}, Curso: {aluno[2]}, Email: {aluno[3]}")
                return aluno
            else:
                print(f"⚠️ Aluno {aluno_id} não encontrado no PostgreSQL")
                return None
    
    def pg_update_aluno(self, aluno_id, campo, novo_valor):
        with self.pg_conn.cursor() as cursor:
            query = sql.SQL("UPDATE alunos SET {} = %s WHERE id = %s").format(
                sql.Identifier(campo)
            )
            cursor.execute(query, (novo_valor, aluno_id))
            if cursor.rowcount > 0:
                print(f"✏️ Aluno {aluno_id} atualizado: {campo} = {novo_valor}")
                return True
            else:
                print(f"⚠️ Aluno {aluno_id} não encontrado")
                return False
    
    def pg_delete_aluno(self, aluno_id):
        with self.pg_conn.cursor() as cursor:
            cursor.execute("DELETE FROM alunos WHERE id = %s", (aluno_id,))
            if cursor.rowcount > 0:
                print(f"🗑️ Aluno {aluno_id} deletado do PostgreSQL")
                return True
            else:
                print(f"⚠️ Aluno {aluno_id} não encontrado")
                return False
    
    def pg_listar_alunos(self):
        with self.pg_conn.cursor() as cursor:
            cursor.execute("SELECT * FROM alunos ORDER BY id")
            alunos = cursor.fetchall()
            print("📋 PostgreSQL - Lista de alunos:")
            for aluno in alunos:
                print(f"   ID: {aluno[0]}, Nome: {aluno[1]}, Curso: {aluno[2]}, Email: {aluno[3]}")
            return len(alunos)
    
    def redis_create_aluno(self, aluno_id, nome, curso, email):
        self.redis_client.hset(f'aluno:{aluno_id}', 'nome', nome)
        self.redis_client.hset(f'aluno:{aluno_id}', 'curso', curso)
        self.redis_client.hset(f'aluno:{aluno_id}', 'email', email)
        print(f"✅ Aluno {aluno_id} criado no Redis: {nome}")
        return True
    
    def redis_read_aluno(self, aluno_id):
        aluno_data = self.redis_client.hgetall(f'aluno:{aluno_id}')
        if aluno_data:
            print(f"📖 Redis - Aluno {aluno_id}: {aluno_data}")
            return aluno_data
        else:
            print(f"⚠️ Aluno {aluno_id} não encontrado no Redis")
            return None
    
    def redis_update_aluno(self, aluno_id, campo, novo_valor):
        if self.redis_client.hexists(f'aluno:{aluno_id}', campo):
            self.redis_client.hset(f'aluno:{aluno_id}', campo, novo_valor)
            print(f"✏️ Aluno {aluno_id} atualizado no Redis: {campo} = {novo_valor}")
            return True
        else:
            print(f"⚠️ Campo {campo} não existe")
            return False
    
    def redis_delete_aluno(self, aluno_id):
        resultado = self.redis_client.delete(f'aluno:{aluno_id}')
        if resultado:
            print(f"🗑️ Aluno {aluno_id} deletado do Redis")
            return True
        else:
            print(f"⚠️ Aluno {aluno_id} não encontrado no Redis")
            return False
    
    def redis_listar_alunos(self):
        alunos_keys = self.redis_client.keys('aluno:*')
        print("📋 Redis - Lista de alunos:")
        for key in alunos_keys:
            aluno_data = self.redis_client.hgetall(key)
            print(f"   {key}: {aluno_data}")
        return len(alunos_keys)

def demonstrar_crud_completo():
    sistema = SistemaAlunos()
    
    try:
        print("\n🎓 SISTEMA COMPLETO - REDIS + POSTGRESQL")
        print("=" * 50)
        
        sistema.pg_create_tables()
        
        print("\n1. 🗄️ CRUD NO POSTGRESQL:")
        id1 = sistema.pg_create_aluno("Ana Silva", "Ciência da Computação", "ana@email.com")
        id2 = sistema.pg_create_aluno("Carlos Oliveira", "Sistemas de Informação", "carlos@email.com")
        sistema.pg_read_aluno(id1)
        sistema.pg_update_aluno(id1, "curso", "Engenharia de Software")
        sistema.pg_listar_alunos()
        
        print("\n2. 🚀 CRUD NO REDIS:")
        sistema.redis_create_aluno("R100", "Maria Santos", "Redes de Computadores", "maria@email.com")
        sistema.redis_create_aluno("R200", "João Pereira", "Banco de Dados", "joao@email.com")
        sistema.redis_read_aluno("R100")
        sistema.redis_update_aluno("R100", "curso", "Segurança da Informação")
        sistema.redis_listar_alunos()
        sistema.redis_delete_aluno("R200")
        
        print("\n3. 📊 RESULTADOS FINAIS:")
        total_pg = sistema.pg_listar_alunos()
        total_redis = sistema.redis_listar_alunos()
        print(f"🎯 Total alunos - PostgreSQL: {total_pg}, Redis: {total_redis}")
        
        print("\n🎉 SISTEMA COMPLETO FUNCIONANDO!")
        
    except Exception as e:
        print(f"❌ Erro: {e}")
    finally:
        sistema.close()

if __name__ == "__main__":
    demonstrar_crud_completo()