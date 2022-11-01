import locale
from tkinter import *
from ScrapyBcb.BcPoup.spiders import Bcb


def valor_total():
    rendimento = entry_rendimento.get()
    rendimento = rendimento.replace(',', '.')
    rendimento = float(rendimento)
    valor = entry_valor.get()
    valor = valor.replace(',', '.')
    valor = float(valor)

    valor_rend = (valor * rendimento) / 100
    total = valor_rend + valor
    valor_rend = locale.currency(valor_rend, grouping=True)
    print('valor do rendimento:', valor_rend)
    total = locale.currency(total, grouping=True)
    print('Valor total com reajuste:', total)

    label_valor_rend['text'] = valor_rend
    label_total['text'] = total


def buscar_rend():
    label_valor_rend['text'] = ''
    label_total['text'] = ''
    lista = open('D:/pys/pycharm/calcpoup/ScrapyBcb/BcPoup/spiders/rendimento.txt', 'r')
    l_rend = []
    for i in lista:
        l_rend.append(i[:-1])
    lista.close()
    data_rend = entry_data.get()
    for i in range(len(l_rend)):
        if l_rend[i] == data_rend:
            rendimento.set(l_rend[i+1])
            label_estado['text'] = "Data localizada!"
            valor_total()
            break
        if i == len(l_rend)-1:
            label_estado['text'] = "Data não localizada!"


locale.setlocale(locale.LC_ALL, '')

# Inicializa o scrapy do rendimentos com fonte o Banco central do Brasil
Bcb

screen = Tk()
padvar = 3
fontsize = 15
screen.title('Cálculo de poupança')

label_valor = Label(screen, text='Valor a calcular', padx=padvar, pady=padvar, justify='left', font=fontsize)
label_valor.grid(column=0, row=0, sticky=(W))

valor = DoubleVar()
valor.set('0000,00')
entry_valor = Entry(screen, textvariable=valor, font=fontsize)
entry_valor.grid(column=1, row=0)

label_rendimento = Label(screen, text='Valor do rendimento', padx=padvar, pady=padvar, font=fontsize)
label_rendimento.grid(column=0, row=1, sticky=(W))

rendimento = DoubleVar()
rendimento.set('0,0000')
entry_rendimento = Entry(screen, textvariable=rendimento, font=fontsize)
entry_rendimento.grid(column=1, row=1)

label_data = Label(screen, text='Data do rendimento', padx=padvar, pady=padvar, font=fontsize)
label_data.grid(column=0, row=2, sticky=(W))

data_rend = DoubleVar()
data_rend.set('00/00/0000')
entry_data = Entry(screen, textvariable=data_rend, font=fontsize)
entry_data.grid(column=1, row=2)

button_calcular = Button(screen, text='Calcular valor reajustado', command=valor_total, padx=padvar, pady=padvar, font=fontsize)
button_calcular.grid(column=2, row=1, sticky=(W))

button_data = Button(screen, text='Calcular valor pela data', command=buscar_rend, padx=padvar, pady=padvar, font=fontsize)
button_data.grid(column=2, row=2, sticky=(W, E))

label_estado = Label(screen, text='', padx=padvar, pady=padvar, relief='sunken', font=fontsize)
label_estado.grid(column=2, rowspan=4, sticky=(N, S, W, E))

title_valor_rend = Label(screen, text='Rendimento', padx=padvar, pady=padvar, font=fontsize)
title_valor_rend.grid(column=0, row=4, sticky=(E))

label_valor_rend = Label(screen, text='', padx=padvar, pady=padvar, relief='sunken', font=fontsize)
label_valor_rend.grid(column=1, row=4, sticky=(W, E))

title_total = Label(screen, text='Valor total', font=fontsize)
title_total.grid(column=0, row=5, sticky=(E))

label_total = Label(screen, text='', padx=padvar, pady=padvar, relief='sunken', font=fontsize)
label_total.grid(column=1, row=5, sticky=(W, E))

screen.mainloop()
