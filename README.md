# 🎓 Sistemas de Banco de Dados - Unochapecó

## 📚 Disciplina: Banco de Dados II
**Professor:** Monica Tissiani De Toni Pereira  
**Alunos:** Erik Stumpf Ogliari, Willian Stieven

## 🏗️ Sistemas Implementados

### 1. 🗄️ Sistema de Recomendação com Neo4j
- **Arquivo:** sistema_recomendacao.py
- **Descrição:** Sistema de recomendação de livros baseado em interesses de usuários
- **Funcionalidades:**
  - Cadastro de usuários e livros
  - Sistema de recomendações personalizadas
  - Busca de usuários similares
  - Estatísticas do sistema

### 2. 🚀 Sistema de Gerenciamento com Redis e PostgreSQL
- **Arquivo:** sistema_alunos.py
- **Descrição:** CRUD completo para gerenciamento de alunos
- **Funcionalidades:**
  - CREATE, READ, UPDATE, DELETE em ambos bancos
  - Redis para cache e performance
  - PostgreSQL para persistência
  - Sincronização entre bancos

## 🛠️ Tecnologias Utilizadas

- **Python 3.12**
- **Neo4j** - Banco de dados de grafos
- **Redis** - Banco chave-valor em memória
- **PostgreSQL** - Banco relacional
- **VSCode** - Ambiente de desenvolvimento

## 📋 Estrutura do Projeto

\\\
ProjetoNeo4j/
├── sistema_recomendacao.py    # Sistema Neo4j
├── sistema_alunos.py          # Sistema Redis + PostgreSQL
├── teste_neo4j.py             # Testes Neo4j
├── teste_redis.py             # Testes Redis
├── teste_postgres.py          # Testes PostgreSQL
├── requirements.txt           # Dependências
└── README.md                  # Documentação
\\\

## ⚡ Como Executar

1. **Ativar ambiente virtual:**
   \\\ash
   venv_neo4j\Scripts\Activate
   \\\

2. **Instalar dependências:**
   \\\ash
   pip install -r requirements.txt
   \\\

3. **Executar sistemas:**
   \\\ash
   python sistema_recomendacao.py
   python sistema_alunos.py
   \\\

## 📊 Resultados Obtidos

- **Neo4j:** 3 usuários e 5 livros cadastrados
- **PostgreSQL:** 2 alunos persistidos
- **Redis:** 1 aluno em cache
- **CRUD completo** funcionando

**🎓 Unochapecó - Escola Politécnica**  
**💻 Ciência da Computação / Sistemas de Informação**  
**📅 Dezembro 2025**
