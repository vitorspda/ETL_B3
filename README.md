# ETL B3 Portfolio

## Objetivo

O principal objetivo deste projeto é aplicar meus conhecimentos de Engenharia de Dados no ambiente financeiro. Para isso, realizo a coleta de dados da bolsa brasileira, acompanhando 10 ativos selecionados. A partir desses dados, serão feitas transformações, criação de indicadores financeiros e, por fim, a visualização dos resultados utilizando o Power BI.

## Tecnologias Utilizadas

- **Python** — Linguagem principal para extração, transformação e carga dos dados.
- **Yahoo Finance API (via biblioteca yfinance)** — Fonte dos dados financeiros dos ativos.
- **SQL Server** — Banco de dados para armazenamento e modelagem dos dados.
- **Apache Airflow** — Orquestração dos pipelines ETL.
- **Docker** — Containerização para facilitar o ambiente de desenvolvimento e execução.
- **Power BI** — Ferramenta para criação dos dashboards e visualização dos dados.
- **Git + GitHub** — Controle de versão e colaboração no código.

## Estrutura do Projeto

etl-b3-portfolio/
│
├── dags/ # Pipelines do Airflow
├── notebooks/ # Notebooks para análises exploratórias
├── scripts/ # Scripts Python para ETL (extração, transformação, carga)
├── sql/ # Scripts SQL para criação e manutenção das tabelas no banco
├── README.md # Documentação do projeto
├── requirements.txt # Lista de dependências Python
├── docker-compose.yml # Configuração Docker para SQL Server e Airflow
└── .gitignore # Arquivos e pastas ignorados pelo Git

bash
Copiar
Editar


## Como Rodar o Projeto

### 1. Clone este repositório

```bash
git clone https://github.com/seu-usuario/etl-b3-portfolio.git
cd etl-b3-portfolio

2. Configure o ambiente Python
Recomendo usar um ambiente virtual (venv):

bash
Copiar
Editar
python -m venv venv
venv\Scripts\activate  # Windows
# ou
source venv/bin/activate  # Linux/macOS

pip install -r requirements.txt
3. Configure e suba os containers Docker
bash
Copiar
Editar
docker-compose up -d
Isso iniciará o SQL Server e o Airflow.

4. Acesse o Airflow
Abra no navegador:

arduino
Copiar
Editar
http://localhost:8080
5. Importe as tabelas no SQL Server
Execute os scripts SQL na pasta /sql para criar as tabelas necessárias.

6. Execute os pipelines Airflow
Verifique e rode as DAGs para coletar, transformar e carregar os dados.

7. Conecte o Power BI ao SQL Server
Use o servidor localhost e a porta 1433 para acessar os dados e criar os dashboards.

Próximos Passos
- Implementar a extração dos dados usando a API do Yahoo Finance.

- Criar os scripts de transformação para calcular os indicadores financeiros.

- Desenvolver os pipelines no Airflow para orquestrar o processo ETL.

- Montar os dashboards no Power BI com base nos dados transformados.

- Adicionar testes automatizados para garantir a qualidade dos dados.

- Explorar outras fontes de dados para enriquecer a análise.

- Documentar mais detalhadamente cada etapa do processo.