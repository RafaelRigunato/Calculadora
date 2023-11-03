import tkinter as tk
import requests
import pandas as pd

def cotadora():
    url = "http://economia.awesomeapi.com.br/json/last/USD-BRL"
    taxa_cal = requests.get(url).json()
    ask_value = float(taxa_cal.get('USDBRL', {}).get('ask'))
    return ask_value

def calculate_spread():
    try:
         # Limpa o conteúdo atual do widget de texto
        result_text.config(state="normal")
        result_text.delete(1.0, "end")
        
        taxa_oferecida = float(entry_taxa_oferecida.get())
        taxa_coletada = cotadora()
        trashold = float(entry_trashold.get())

        spread = round(taxa_oferecida - taxa_coletada, 4)

        # Cálculos dos spreads
        spread_10bps = round( taxa_coletada + 0.010, 4)
        spread_15bps = round(taxa_coletada + 0.015, 4)
        spread_20bps = round(taxa_coletada + 0.020, 4)
        spread_25bps = round(taxa_coletada + 0.025, 4)

        # Insere os resultados dos cálculos no widget de texto
        result_text.insert("end", f"Spread 10BPS: {spread_10bps}\n")
        result_text.insert("end", f"Spread 15BPS: {spread_15bps}\n")
        result_text.insert("end", f"Spread 20BPS: {spread_20bps}\n")
        result_text.insert("end", f"Spread 25BPS: {spread_25bps}\n")
        result_text.insert("end", f"Taxa Coletada: {taxa_coletada}\n")
        result_text.insert("end", f"Taxa Oferecida: {taxa_oferecida}\n")
        result_text.insert("end", f"Spread: {spread}\n")
        result_text.insert("end", f"Limite: {trashold}\n")
  
        # Verifica o valor do spread em relação ao threshold
        if spread > trashold:
            result_text.insert("end", "SPREAD ACIMA, NÃO FECHAR\n")
        else:
            result_text.insert("end", "SPREAD ABAIXO, PODE FECHAR\n")
        
        # Define o widget de texto como somente leitura novamente
        result_text.config(state="disabled")
    except ValueError:
        result_text.config(state="normal")
        result_text.delete(1.0, "end")
        result_text.insert("end", "Erro: Insira um valor válido para a taxa oferecida.")
        result_text.config(state="disabled")


frm = tk.Tk()
frm.title("Calculadora de Spread")

label_taxa_oferecida = tk.Label(frm, text="Taxa Oferecida:")
label_taxa_oferecida.grid(column=0, row=0)

label_trashold = tk.Label(frm, text="impute um limite:")
label_trashold.grid(column=0, row=1)

entry_taxa_oferecida = tk.Entry(frm)
entry_taxa_oferecida.grid(column=1, row=0)

entry_trashold = tk.Entry(frm)
entry_trashold.grid(column=1, row=1)

calculate_button = tk.Button(frm, text="Calcular Spread", command=calculate_spread)
calculate_button.grid(column=0, row=3, columnspan=2)

result_text = tk.Text(frm, height=10, width=50, state="disabled")
result_text.grid(column=0, row=2, columnspan=2)

frm.mainloop()
