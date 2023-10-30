import requests

def cotadora():
    url = "http://economia.awesomeapi.com.br/json/last/USD-BRL"
    taxa_cal = requests.get(url).json()
    ask_value = float(taxa_cal.get('USDBRL', {}).get('ask'))
    return ask_value

trashold = float(0.020)
while True:

    taxa_oferecida = float(input("Digite a taxa oferecida: "))
    taxa_coletada = cotadora()

    resultado = taxa_oferecida - taxa_coletada
    print("Exemplos: 10BPS - ", taxa_coletada + 0.010, "15BPS - ", taxa_coletada + 0.015,"20BPS - ", taxa_coletada + 0.020)
    print("a taxa coletada e:", taxa_coletada)
    print("a taxa oferecida e:", taxa_oferecida)
    print("O Spread e:", resultado)

    if resultado > trashold:
        print("Nao fecha")
        
    else:
        print("pode fechar")