# Em um novo programa, crie uma tupla para guardar os meses do ano. Em seguida peça ao usuário a sua data de nascimento
# no formado DD-MM-AAAA e guarde-a na variável data_nasc. Ao final imprima "Você nasceu no mês de .....",
# utilizando o nome do mês da tuplas correspondente ao mês informado pelo utilizador.

# Dica: Você vai precisar fazer slicing na data de nascimento informada para ter o mês. Depois você
# terá que buscar o mês na tupla atrás do índice.

meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
data_nasc = input('Digite sua data de nascimento no formato DD-MM-AAAA: ')

indice = int(data_nasc[3:5]) - 1
mes = meses[indice]

print('Você nasceu no mês de:', mes)


