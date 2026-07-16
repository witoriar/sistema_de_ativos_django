Sistema Ativos de TI

Sistema web desenvolvido em Django para cadastro e gerenciamento de ativos de TI e vulnerabilidades associadas. 
A aplicação foi desenvolvida em POO, com banco de dados relacional, interface web e conteinerização com docker.

Tecnologias utilizadas:
    • Python 3.11
    • Django 5.2.6
    • SQLite— banco de dados relacional
    • Gunicorn — servidor WSGI para produção
    • Docker / Docker Compose— containerização da aplicação

Processo de criação:
1. Estrutura:
    • Camada de objetos (ativos/classes/) - classes python com a lógica de negócio.
    • Camada de persistência (models.py) – models Django para comunicação com o banco.
    • Camada  de apresentação (views.py + templetes) – interface web para o usuário.


2. Desenvolvimento  das classes POO:
Criação da classe base ativo com os atributos comuns a todos os tipos de ativos, a partir delas foram derivadas 4 subclasses:

	Ativo (classe base)
	 - Servidor
	 - Notebook
	 - Rotiador
	 - AplicaçãoWeb

Cada subclasse herda automaticamente todos os atributos e métodos da classe Ativo (hostname, responsavel, setor, vulnerabilidades, adicionar_vulnerabilidade() e to_dict()).
Cada subclasse sobrescreve o método __str__() para exibir os tipos de ativo correto.
 
Enumerações - foram criadas 3 unums para padronizar os valores aceitos pelo sistema:

TipoAtivo = SERVIDOR, NOTEBOOK, ROTEADOR, APLICACAO_WEB.
Severidade = BAIXA, MEDIA, ALTA, CRITICA.
StatusVulnerabilidade = ABERTA, EM_TRATAMENTO, CORRIGIDA, ACEITA.

3. Models e Banco de dados:
Uso do JSONField, salva cada ativo JSON em banco SQL.
Model Ativo – armazena os dados principais do ativo e o objeto completo serializado em JSON  no campo “dados_json”.
Model Vulnerabilidades – ligado ao ativo por uma “foreignkey” com “on_delete_CASCADE”, garantindo que ao deletar um ativo, todas as suas vulnerabilidades são removidas automaticamente.

4. Views e URLs:
As views foram desenvolvidas seguindo o padrão de formulários:
    1. Primeiro POST -  usuário digita o ID do ativo
    2. Segundo POST – sistema carrega o ativo e exibe o formulário completo
Todas as views  possuem tratamento de erros com “try/except” para capturar Ids  inválidos ou ativos inexistentes.

5. Interface Web:
A interface foi desenvolvida com HTML e CSS puro. O “base.html” centraliza o menu de navegação que é herdado por todos os outros templates com “{% extends %} - evitando repetição de código


Estrutura do projeto:

ativos_ti/
├── ativos/                   
│   ├── classes/                
│   │   ├── __init__.py
│   │   ├── ativo.py           
│   │   └── subclasses.py       
│   ├── templates/
│   │   └── ativos/             
│   │       ├── base.html
│   │       ├── listar.html
│   │       ├── cadastrar.html
│   │       ├── atualizar.html
│   │       ├── deletar.html
│   │       ├── vulnerabilidade.html
│   │       └── visualizar_vulnerabilidades.html
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py               
│   ├── urls.py                 
│   └── views.py                
├── ativos_ti/                  
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── manage.py

 Funcionalidades:

    • Cadastrar ativos de TI (Servidor, Notebook, Roteador, Aplicação Web)
    • Listar todos os ativos cadastrados
    • Editar dados de um ativo existente
    • Deletar um ativo e suas vulnerabilidades associadas
    • Cadastrar vulnerabilidades associadas a um ativo
    • Visualizar vulnerabilidades de um ativo
    • Classificação de vulnerabilidades por severidade (Baixa, Média, Alta, Crítica)
    • Acompanhamento do status de tratamento (Aberta, Em Tratamento, Corrigida, Aceita como Risco).
