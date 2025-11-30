from neo4j import GraphDatabase
import logging

class SistemaRecomendacao:
    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))
    
    def close(self):
        self._driver.close()
    
    def criar_estrutura_inicial(self):
        try:
            with self._driver.session() as session:
                session.run("MATCH (n) DETACH DELETE n")
                print("Dados anteriores removidos")
                
                usuarios = [
                    {"nome": "Ana", "idade": 25, "interesses": ["ficção", "tecnologia"]},
                    {"nome": "Carlos", "idade": 30, "interesses": ["ciência", "história"]},
                    {"nome": "Beatriz", "idade": 22, "interesses": ["romance", "aventura"]}
                ]
                
                for usuario in usuarios:
                    session.run(
                        "CREATE (u:Usuario {nome: $nome, idade: $idade, interesses: $interesses})",
                        nome=usuario["nome"], idade=usuario["idade"], interesses=usuario["interesses"]
                    )
                
                livros = [
                    {"titulo": "Dom Casmurro", "autor": "Machado de Assis", "genero": "romance", "ano": 1899},
                    {"titulo": "1984", "autor": "George Orwell", "genero": "ficção", "ano": 1949},
                    {"titulo": "Uma Breve História do Tempo", "autor": "Stephen Hawking", "genero": "ciência", "ano": 1988},
                    {"titulo": "O Senhor dos Anéis", "autor": "J.R.R. Tolkien", "genero": "aventura", "ano": 1954},
                    {"titulo": "O Guia do Mochileiro das Galáxias", "autor": "Douglas Adams", "genero": "ficção", "ano": 1979}
                ]
                
                for livro in livros:
                    session.run(
                        "CREATE (l:Livro {titulo: $titulo, autor: $autor, genero: $genero, ano: $ano})",
                        titulo=livro["titulo"], autor=livro["autor"], genero=livro["genero"], ano=livro["ano"]
                    )
                
                leituras = [
                    {"usuario": "Ana", "livro": "1984", "avaliacao": 5},
                    {"usuario": "Ana", "livro": "O Guia do Mochileiro das Galáxias", "avaliacao": 4},
                    {"usuario": "Carlos", "livro": "Uma Breve História do Tempo", "avaliacao": 5},
                    {"usuario": "Beatriz", "livro": "Dom Casmurro", "avaliacao": 4},
                    {"usuario": "Beatriz", "livro": "O Senhor dos Anéis", "avaliacao": 5}
                ]
                
                for leitura in leituras:
                    session.run(
                        "MATCH (u:Usuario {nome: $usuario}), (l:Livro {titulo: $livro}) CREATE (u)-[r:LEU {avaliacao: $avaliacao}]->(l)",
                        usuario=leitura["usuario"], livro=leitura["livro"], avaliacao=leitura["avaliacao"]
                    )
                
                print("Estrutura inicial criada com sucesso")
                return True
                
        except Exception as e:
            print(f"Erro ao criar estrutura: {e}")
            return False
    
    def estatisticas_sistema(self):
        try:
            with self._driver.session() as session:
                total_usuarios = session.run("MATCH (u:Usuario) RETURN count(u) as total").single()["total"]
                total_livros = session.run("MATCH (l:Livro) RETURN count(l) as total").single()["total"]
                media_avaliacoes = session.run("MATCH ()-[r:LEU]->() RETURN avg(r.avaliacao) as media").single()["media"]
                
                return {
                    "total_usuarios": total_usuarios,
                    "total_livros": total_livros,
                    "media_avaliacoes": round(media_avaliacoes, 2) if media_avaliacoes else 0
                }
        except Exception as e:
            print(f"Erro nas estatísticas: {e}")
            return {"total_usuarios": 0, "total_livros": 0, "media_avaliacoes": 0}

def main():
    URI = "bolt://localhost:7687"
    USER = "neo4j"
    PASSWORD = "senha1234567"
    
    sistema = SistemaRecomendacao(URI, USER, PASSWORD)
    
    try:
        print("SISTEMA DE RECOMENDAÇÃO DE LIVROS")
        print("=" * 40)
        
        print("\n1. Criando estrutura inicial...")
        if sistema.criar_estrutura_inicial():
            
            print("\n2. Estatísticas do sistema:")
            stats = sistema.estatisticas_sistema()
            print(f"   • Usuários: {stats['total_usuarios']}")
            print(f"   • Livros: {stats['total_livros']}")
            print(f"   • Média de avaliações: {stats['media_avaliacoes']}")
            
            print("\n3. Sistema configurado com sucesso!")
        else:
            print("Erro ao configurar o sistema")
        
    except Exception as e:
        print(f"Erro geral: {e}")
    finally:
        sistema.close()
        print("\nConexão fechada")

if __name__ == "__main__":
    main()