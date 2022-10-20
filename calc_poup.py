import locale
from tkinter import *


def valor_total():
    rendimento = entry_rendimento.get()
    rendimento = float(rendimento)
    valor = entry_valor.get()
    valor = float(valor)

    valor_rend = (valor * rendimento) / 100
    total = valor_rend + valor
    valor_rend = locale.currency(valor_rend, grouping=True)
    print('valor do rendimento:', valor_rend)
    total = locale.currency(total, grouping=True)
    print('Valor total com reajuste:', total)

    label_valor_rend['text'] = valor_rend
    label_total['text'] = total


locale.setlocale(locale.LC_ALL, '')

# modo teste
# valor = 49000.00
# rendimento = 0.6790

screen = Tk()
screen.title('Cálculo de poupança')

label_valor = Label(screen, text='Valor a calcular.')
label_valor.grid(column=0, row=0)

valor = DoubleVar()
entry_valor = Entry(screen, textvariable=valor)
entry_valor.grid(column=1, row=0)

label_rendimento = Label(screen, text='Valor do rendimento.')
label_rendimento.grid(column=0, row=1)

rendimento = DoubleVar()
entry_rendimento = Entry(screen, textvariable=rendimento)
entry_rendimento.grid(column=1, row=1)

button_calcular = Button(screen, text='Calcular valor reajustado', command=valor_total)
button_calcular.grid(column=0, row=2)

label_valor_rend = Label(screen, text='')
label_valor_rend.grid(column=0, row=3)

label_total = Label(screen, text='')
label_total.grid(column=0, row=4)

screen.mainloop()
