import locale

locale.setlocale(locale.LC_ALL, '')

# modo teste
# valor = 49000.00
# rendimento = 0.6790

valor = float(input('insira o valor da conta: '))
rendimento = float(input('insira o valor de rendimento : '))
valor_rend = (valor * rendimento) / 100
total = valor_rend + valor
valor_rend = locale.currency(valor_rend, grouping=True)
print('valor do rendimento:', valor_rend)
total = locale.currency(total, grouping=True)
print('Valor total com reajuste:', total)
