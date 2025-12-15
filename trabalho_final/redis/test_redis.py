import redis

def testar_redis():
    print("Testando conexão com Redis...")
    
    try:
        r = redis.Redis(
            host='localhost',
            port=6379,
            decode_responses=True,
            socket_connect_timeout=3
        )
        
        # Testar ping
        resposta = r.ping()
        print(f"✅ Redis respondeu: {resposta}")
        
        # Testar escrita/leitura
        r.set('teste:trabalho', 'Unochapecó - Banco de Dados II')
        valor = r.get('teste:trabalho')
        print(f"✅ Teste de escrita/leitura: {valor}")
        
        # Limpar teste
        r.delete('teste:trabalho')
        
        print("\n✅ Redis está funcionando!")
        return True
        
    except Exception as e:
        print(f"❌ Erro: {e}")
        print("\nPara iniciar Redis:")
        print("1. Execute redis-server.exe")
        print("2. OU use Docker: docker run -d -p 6379:6379 redis")
        return False

if __name__ == "__main__":
    testar_redis()