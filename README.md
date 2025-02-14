# Análise e Relatórios de Dados Financeiros

Este projeto demonstra habilidades em Python, ETLs, APIs, Big Data e automação. Ele consome dados da API Alpha Vantage, processa os dados e gera relatórios automatizados.

## Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/Magalhaes-vitor/financial-data-analysis.git
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Execute o script principal:
   ```bash
   python main.py
   ```

## Funcionalidades
- **Extração de Dados:** Consome dados da API Alpha Vantage.
- **Transformação de Dados:** Realiza limpeza e cálculos (ex: média móvel).
- **Geração de Relatórios:** Cria gráficos de preço de fechamento e média móvel.
- **Automação:** Executa o processo diariamente às 09:00.

## Estrutura do Projeto
- `main.py`: Script principal que integra todas as funcionalidades.
- `AAPL_data.csv`: Dados brutos extraídos da API.
- `transformed_AAPL_data.csv`: Dados processados.
- `AAPL_close_price.png`: Gráfico de preço de fechamento.
- `AAPL_moving_average.png`: Gráfico de média móvel.

## Tecnologias Utilizadas
- Python
- Alpha Vantage API
- Pandas, Matplotlib, Seaborn
- Automação com Schedule

## Requisitos
- Python 3.x
- Bibliotecas listadas em `requirements.txt`

## Configuração
1. Crie um arquivo `.env` na raiz do projeto e adicione sua chave da API:
   ```plaintext
   ALPHA_VANTAGE_API_KEY=K6YQXY5ZNR4QRRU7
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Autor
Vitor Magalhães  
[GitHub](https://github.com/Magalhaes-vitor) | [LinkedIn](https://www.linkedin.com/in/magalhaes-vitor/)

### **Como Usar**

1. Crie um repositório no GitHub chamado `financial-data-analysis`.  
2. Adicione os arquivos `main.py`, `README.md` e `requirements.txt`.  
3. Execute o script localmente para testar:  
   ```bash
   python main.py
   ```
4. O script será executado diariamente às 09:00, gerando os arquivos CSV e gráficos automaticamente.

---

