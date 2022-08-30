import tkinter as tk
from tkinter import ttk
from tkinter import *
from funções import cotacaodl, cotacaoeu, cotacaobt
import time


while True:
    tempoinicial = time.time()
    dl = cotacaodl()
    eu = cotacaoeu()
    bt = cotacaobt()
    root = tk.Tk()
    root.title("Cotações")
    tabControl = ttk.Notebook(root)
    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    tab3 = ttk.Frame(tabControl)
    button1 = ttk.Button
    tabControl.add(tab1, text='Valor do BitCoin')
    tabControl.add(tab2, text='Valor do Dólar')
    tabControl.add(tab3, text='Cotação do Euro')
    tabControl.pack(expand=20, fill="both")

    ttk.Label(tab1,
              text=f'R$ {bt} \
             Valor Atual!').grid(column=50,
                                 row=10,
                                 padx=80,
                                 pady=80)
    ttk.Label(tab2,
              text=f"R$ {dl}\
              Valor atual!").grid(column=50,
                                  row=10,
                                  padx=80,
                                  pady=80)
    ttk.Label(tab3,
              text=f"R$ {eu}\
              Valor atual!").grid(column=50,
                                  row=10,
                                  padx=80,
                                  pady=80)
    tempofinal = time.time()
    duração = tempofinal - tempoinicial
    print(duração)
    root.mainloop()
