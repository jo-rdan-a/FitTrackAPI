# 💪 Sistema de Monitoramento de Treinos - IFCE

Este é um sistema web desenvolvido em **FastAPI**, **Jinja2** e **PostgreSQL**, criado como parte de um projeto para o curso de Análise e Desenvolvimento de Sistemas do IFCE - campus Boa Viagem. O objetivo é permitir que **instrutores criem fichas de treino personalizadas para seus alunos**, acompanhem a evolução e gerenciem os exercícios cadastrados.

---

## 🚀 Funcionalidades

- 👨‍🏫 Área exclusiva para **instrutores**:
  - Criar novos alunos
  - Editar ou excluir alunos
  - Criar e gerenciar fichas de treino para cada aluno
  - Cadastrar exercícios com grupos musculares
  - Visualizar dashboard com todas as fichas

- 📋 **Ficha de treino**:
  - Suporte a todos os dias da semana
  - Cada dia pode conter múltiplos exercícios
  - Cada exercício possui séries, repetições e grupo muscular

---

## 📦 Tecnologias e Dependências

- **Python 3.10+**
- **FastAPI**
- **Jinja2**
- **SQLAlchemy**
- **PostgreSQL**
- **Uvicorn**
- **Bootstrap 5**
- **Tom Select (para select com busca)**

---

## 🛠️ Como instalar e executar o projeto

### 1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo
```

### 2. Crie um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

### 3. Instale as dependências:

```bash
pip install -r requirements.txt
```

> Se você não tiver o arquivo `requirements.txt`, posso gerar um com base nas bibliotecas utilizadas.

### 4. Configure o banco de dados:

Edite o arquivo de conexão no `dao/database.py` com suas credenciais do PostgreSQL:

```python
DATABASE_URL = "postgresql://usuario:senha@localhost/nome_do_banco"
```

Crie as tabelas executando o seguinte código Python uma vez:

```python
from models.models import Base
from dao.database import engine

Base.metadata.create_all(bind=engine)
```

### 5. Execute o servidor:

```bash
uvicorn main:app --reload
```

---

## 🗂️ Estrutura de diretórios

```
├── main.py
├── models/
│   └── models.py
├── dao/
│   └── database.py
├── routes/
│   └── instrutor_routes.py
├── templates/
│   ├── base.html
│   ├── alunos.html
│   ├── criar_ficha.html
│   ├── editar_aluno.html
│   └── dashboard_instrutor.html
├── static/
│   └── (CSS/JS personalizados)
└── README.md
```

---

## 📚 Autor

Desenvolvido por **Weslem**, estudante do IFCE - Boa Viagem, como parte de um projeto acadêmico para aplicação de tecnologias web modernas no contexto de Educação Física e Treinamento Personalizado.

---

## 📄 Licença

Este projeto é de uso acadêmico, sem fins lucrativos.

