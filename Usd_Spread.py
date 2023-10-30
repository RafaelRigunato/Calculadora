import requests
import pandas as pd

def cotadora():
    url = "http://economia.awesomeapi.com.br/json/last/USD-BRL"
    taxa_cal = requests.get(url).json()
    ask_value = float(taxa_cal.get('USDBRL', {}).get('ask'))
    return ask_value

trashold = float(0.025)
data = []
data2 = []
while True:

    taxa_oferecida = float(input("Digite a taxa oferecida: "))
    
    if taxa_oferecida == 191301:
        break

    taxa_coletada = cotadora()

    spread = taxa_oferecida - taxa_coletada

    #Simulacao

    spread_10bps = taxa_coletada + 0.010
    spread_15bps = taxa_coletada + 0.015
    spread_20bps = taxa_coletada + 0.020
    spread_25bps = taxa_coletada + 0.025
    
    data.append([spread_10bps, spread_15bps, spread_20bps, spread_25bps])

    df = pd.DataFrame(data, columns=["10BPS", "15BPS", "20BPS", "25BPS"])
    print(df)

    data2.append([taxa_coletada, taxa_oferecida, spread])
    df2 = pd.DataFrame(data2, columns=["Taxa Coletada", "Taxa Oferecida", "Spread"])
    print(df2)

    if spread > trashold:
        print("SPREAD ACIMA, NÃO FECHAR")
        
    else:
        print("SPREAD ABAIXO, PODE FECHAR")
