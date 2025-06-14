import yfinance as yf
import pandas as pd
from datetime import datetime


def extract_data(tickers, start_date, end_date):
    all_data = []
    
    # transforma cada ticker(nome da empresa e data) em uma lista
    for ticker in tickers:
        data = yf.download(ticker, start=start_date, end=end_date, auto_adjust=False)

    # Resetamos o index e fixamos a coluna Ticker para trazer corretamente o ticker e as colunas
    # e faz um append dos dados na lista 
        if not data.empty:
            data.reset_index(inplace=True)
            data['Ticker'] = ticker
            data = data[['Ticker', 'Date', 'Open', 'High', 'Low', 'Close', 'Volume']]
            all_data.append(data)
        
        if all_data:
            return pd.concat(all_data, ignore_index=True)
        else:
            pd.DataFrame(columns=['Ticker', 'Date', 'Open', 'High', 'Low', 'Close', 'Volume'])

if __name__ == "__main__":
    ativos = ['PETR4.SA', 'VALE3.SA', 'ITUB4.SA']
    df = extract_data(ativos, '2023-01-01', '2023-12-31')
    print(df.head())
            
        
        
#        data.reset_index(inplace=True)
 #       data['ticker'] = ticker
  #      data['extract_at'] = datetime.now()
   #     all_data.append(data)

   # result = pd.concat(all_data, ignore_index=True)
   # return result


#   teste do código
#   if __name__ == '__main__':
#       ativos = ['PETR4.SA', 'VALE3.SA', 'ITUB4.SA']
#       df = extract_data(ativos, '2023-01-01', '2023-12-01')
#       print(df.head)