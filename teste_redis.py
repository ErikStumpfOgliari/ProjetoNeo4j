import redis

def testar_redis():
    print("🧪 TESTANDO REDIS")
    print("=" * 30)
    
    try:
        # Conectar ao Redis
        r = redis.Redis(
            host='localhost',
            port=6379,
            db=0,
            decode_responses=True,
            socket_connect_timeout=5
        )
        
        # Testar conexão
        resultado = r.ping()
        print("✅ Redis conectado!")
        
        # LIMPAR DADOS ANTIGOS
        r.delete("aluno:100")
        
        # Testar CRUD básico - MÉTODO COMPATÍVEL
        print("\n🎯 TESTE CRUD REDIS:")
        
        # CREATE - Método compatível com versões antigas
        r.hset("aluno:100", "nome", "Teste Aluno")
        r.hset("aluno:100", "curso", "Ciência da Computação")
        r.hset("aluno:100", "email", "teste@email.com")
        print("✅ Aluno criado")
        
        # READ
        aluno = r.hgetall("aluno:100")
        print(f"📖 Aluno lido: {aluno}")
        
        # UPDATE
        r.hset("aluno:100", "curso", "Engenharia de Software")
        print("✏️ Aluno atualizado")
        
        # Verificar atualização
        aluno_atualizado = r.hgetall("aluno:100")
        print(f"📖 Aluno atualizado: {aluno_atualizado}")
        
        # LIST
        alunos = r.keys("aluno:*")
        print(f"📋 Total alunos: {len(alunos)}")
        
        # DELETE
        r.delete("aluno:100")
        print("🗑️ Aluno deletado")
        
        # Verificar deleção
        alunos_final = r.keys("aluno:*")
        print(f"📋 Alunos restantes: {len(alunos_final)}")
        
        print("\n🎉 REDIS FUNCIONANDO PERFEITAMENTE!")
        
    except Exception as e:
        print(f"❌ Erro no Redis: {e}")
        print(f"Tipo de erro: {type(e).__name__}")

if __name__ == "__main__":
    testar_redis()