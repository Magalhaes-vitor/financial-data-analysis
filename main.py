import os
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import schedule
import time
from dotenv import load_dotenv

# Carrega a chave da API do arquivo .env
load_dotenv()
API_KEY = "K6YQXY5ZNR4QRRU8"  # Substitua pela sua chave da API
BASE_URL = "https://www.alphavantage.co/query"

# Função para extrair dados da API
def get_stock_data(symbol):
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "apikey": API_KEY,
        "outputsize": "compact"
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    return data

# Função para salvar os dados em um arquivo CSV
def save_to_csv(data, symbol):
    df = pd.DataFrame(data["Time Series (Daily)"]).T
    df.columns = ["Open", "High", "Low", "Close", "Volume"]
    df.to_csv(f"{symbol}_data.csv")

# Função para transformar os dados
def transform_data(symbol):
    df = pd.read_csv(f"{symbol}_data.csv")
    df["Date"] = pd.to_datetime(df.index)
    df["Close"] = pd.to_numeric(df["Close"])
    df["Moving_Average"] = df["Close"].rolling(window=5).mean()  # Média móvel de 5 dias
    df.to_csv(f"transformed_{symbol}_data.csv", index=False)

# Função para gerar relatórios e gráficos
def generate_reports(symbol):
    df = pd.read_csv(f"transformed_{symbol}_data.csv")
    
    # Gráfico de linha para preço de fechamento
    plt.figure(figsize=(10, 6))
    sns.lineplot(x="Date", y="Close", data=df)
    plt.title(f"Preço de Fechamento - {symbol}")
    plt.savefig(f"{symbol}_close_price.png")
    
    # Gráfico de média móvel
    plt.figure(figsize=(10, 6))
    sns.lineplot(x="Date", y="Moving_Average", data=df)
    plt.title(f"Média Móvel (5 dias) - {symbol}")
    plt.savefig(f"{symbol}_moving_average.png")

# Função principal que integra todas as etapas
def daily_task():
    symbol = "AAPL"  # Símbolo da ação (ex: Apple Inc.)
    print("Extraindo dados da API...")
    data = get_stock_data(symbol)
    save_to_csv(data, symbol)
    
    print("Transformando dados...")
    transform_data(symbol)
    
    print("Gerando relatórios...")
    generate_reports(symbol)
    
    print("Processo concluído!")

# Agendamento da tarefa diária
schedule.every().day.at("14:15").do(daily_task)

# Loop para manter o script em execução
print("Script em execução. Aguardando horário agendado...")
while True:
    schedule.run_pending()
    time.sleep(1)
