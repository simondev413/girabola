# Girabola

Este é um projeto que implementa funcionalidades relacionadas ao campeonato de futebol **Girabola**, utilizando o framework Django. O projeto organiza informações de clubes, jogos e outras estatísticas.

## Estrutura do Projeto

O projeto está organizado nos seguintes diretórios e arquivos principais:

- **clubes/**: Contém funcionalidades relacionadas à gestão dos clubes participantes.
- **docs/**: Inclui a documentação do projeto.
- **girabola/**: Diretório principal do projeto Django, contendo configurações e arquivos básicos.
- **jogos/**: Gerencia os dados sobre os jogos e suas informações.
- **media/**: Diretório para armazenar arquivos de mídia, como imagens ou documentos relacionados.
- **static/**: Contém arquivos estáticos, como CSS, JavaScript e imagens usadas na interface.
- **db.sqlite3**: Base de dados SQLite utilizada pelo projeto.
- **manage.py**: Script de linha de comando para gerenciamento do projeto Django.

## Pré-requisitos

Antes de executar o projeto, certifique-se de ter instalado:

- Python 3.8 ou superior
- Pipenv (opcional, para gestão de ambientes virtuais)
- SQLite (para gerenciamento do banco de dados)

## Instalação e Configuração

1. Clone este repositório:
   ```bash
   git clone https://github.com/simondev413/girabola.git
   cd girabola
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate # Linux/Mac
   venv\Scripts\activate # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Realize as migrações para configurar o banco de dados:
   ```bash
   python manage.py migrate
   ```

5. Inicie o servidor local:
   ```bash
   python manage.py runserver
   ```

6. Acesse o sistema no navegador em `http://127.0.0.1:8000/`.

## Funcionalidades

- Cadastro e gerenciamento de clubes participantes.
- Registro de jogos e resultados.
- Upload e gerenciamento de arquivos de mídia relacionados ao campeonato.
- Interface web para visualização e administração dos dados.

## Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do projeto.
2. Crie uma nova branch para suas alterações:
   ```bash
   git checkout -b minha-feature
   ```
3. Realize as alterações e faça commit:
   ```bash
   git commit -m "Descrição das alterações"
   ```
4. Envie suas alterações:
   ```bash
   git push origin minha-feature
   ```
5. Abra um Pull Request no repositório original.
