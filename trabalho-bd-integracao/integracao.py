import psycopg2
import xml.etree.ElementTree as ET
import os

class IntegradorDados:
    def __init__(self):
        self.conexao = None
        try:
            self.conexao = psycopg2.connect(
                host="localhost",
                port=5433,
                database="trabalho_db",  
                user="postgres",
                password="8520"   
            )
            print("✅ Conectado ao PostgreSQL no banco trabalho_db!")
            
            # Teste rápido
            with self.conexao.cursor() as cur:
                cur.execute("SELECT COUNT(*) FROM Peca")
                count = cur.fetchone()[0]
                print(f"📊 Total de peças: {count}")
                
        except Exception as e:
            print(f"❌ Erro na conexão: {e}")
    
    def pecas_postgresql(self):
        """Busca peças do PostgreSQL"""
        if not self.conexao:
            return []
            
        try:
            with self.conexao.cursor() as cursor:
                cursor.execute("""
                    SELECT cod_peca, pnome, cor, peso, cdade 
                    FROM Peca 
                    ORDER BY cod_peca
                """)
                pecas = cursor.fetchall()
                print(f"✅ {len(pecas)} peças carregadas do PostgreSQL")
                return pecas
        except Exception as e:
            print(f"❌ Erro ao buscar peças: {e}")
            return []
    
    def fornecimentos_xml(self):
        """Busca fornecimentos do XML"""
        try:
            tree = ET.parse('fornecimento.xml')
            root = tree.getroot()
            
            fornecimentos = []
            for row in root.findall('row'):
                dados = {
                    'cod_fornec': row.find('cod_fornec').text,
                    'cod_peca': row.find('cod_peca').text,
                    'quantidade': row.find('quantidade').text,
                    'valor': row.find('valor').text,
                    'cod_proj': row.find('cod_proj').text
                }
                fornecimentos.append(dados)
            
            print(f"✅ {len(fornecimentos)} fornecimentos carregados do XML")
            return fornecimentos
        except Exception as e:
            print(f"❌ Erro no XML: {e}")
            return []
    
    def integrar_completo(self):
        """Integração COMPLETA PostgreSQL + XML"""
        print("\n🔗 INICIANDO INTEGRAÇÃO COMPLETA")
        print("=" * 50)
        
        pecas_db = self.pecas_postgresql()
        fornecimentos_xml = self.fornecimentos_xml()
        
        if not pecas_db:
            print("❌ Nenhuma peça do PostgreSQL")
            return
        
        if not fornecimentos_xml:
            print("❌ Nenhum fornecimento do XML")
            return
        
        with open('relatorio_integracao_completo.txt', 'w', encoding='utf-8') as f:
            f.write("RELATÓRIO DE INTEGRAÇÃO - POSTGRESQL + XML\n")
            f.write("=" * 60 + "\n\n")
            
            total_fornecimentos = 0
            total_quantidade = 0
            total_valor = 0.0
            
            for peca in pecas_db:
                cod_peca, nome, cor, peso, cidade = peca
                
                # Encontrar fornecimentos desta peça
                fornecimentos_peca = [
                    f for f in fornecimentos_xml 
                    if int(f['cod_peca']) == cod_peca
                ]
                
                f.write(f"PEÇA: {nome} (Código: {cod_peca})\n")
                f.write(f"Cor: {cor} | Peso: {peso} | Cidade: {cidade}\n")
                f.write(f"Fornecimentos: {len(fornecimentos_peca)}\n")
                
                if fornecimentos_peca:
                    qtd_total = sum(int(f['quantidade']) for f in fornecimentos_peca)
                    valor_total = sum(float(f['valor']) for f in fornecimentos_peca)
                    
                    f.write(f"Quantidade total: {qtd_total} | Valor total: R$ {valor_total:.2f}\n")
                    f.write("Detalhes:\n")
                    
                    for forn in fornecimentos_peca:
                        f.write(f"  - Fornecedor: {forn['cod_fornec']}, ")
                        f.write(f"Projeto: {forn['cod_proj']}, ")
                        f.write(f"Qtd: {forn['quantidade']}, ")
                        f.write(f"Valor: R$ {forn['valor']}\n")
                    
                    total_fornecimentos += len(fornecimentos_peca)
                    total_quantidade += qtd_total
                    total_valor += valor_total
                else:
                    f.write("  Nenhum fornecimento encontrado\n")
                
                f.write("\n" + "-" * 50 + "\n\n")
            
            # Estatísticas finais
            f.write("ESTATÍSTICAS GERAIS:\n")
            f.write(f"Total de peças: {len(pecas_db)}\n")
            f.write(f"Total de fornecimentos: {total_fornecimentos}\n")
            f.write(f"Quantidade total fornecida: {total_quantidade}\n")
            f.write(f"Valor total: R$ {total_valor:.2f}\n")
        
        print("✅ Relatório completo gerado: relatorio_integracao_completo.txt")
        
        # Mostra resumo no console
        print(f"\n📈 RESUMO DA INTEGRAÇÃO:")
        print(f"Peças do PostgreSQL: {len(pecas_db)}")
        print(f"Fornecimentos do XML: {len(fornecimentos_xml)}")
        print(f"Fornecimentos integrados: {total_fornecimentos}")
    
    def fechar_conexao(self):
        if self.conexao:
            self.conexao.close()
            print("✅ Conexão fechada")

# Executar
if __name__ == "__main__":
    print("🚀 APLICAÇÃO DE INTEGRAÇÃO - POSTGRESQL + XML")
    
    integrador = IntegradorDados()
    
    try:
        if integrador.conexao:
            integrador.integrar_completo()
        else:
            print("❌ Não foi possível conectar ao PostgreSQL")
    except Exception as e:
        print(f"❌ Erro: {e}")
    finally:
        integrador.fechar_conexao()