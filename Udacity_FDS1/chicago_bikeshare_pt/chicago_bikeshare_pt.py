# coding: utf-8

# Começando com os imports
import csv
import matplotlib.pyplot as plt

# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: ")
print(data_list[0])
# É o cabeçalho dos dados, para que possamos identificar as colunas.

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])

input("Aperte Enter para continuar...")
# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")
contador = -1
for i in data_list[:20]:                       # Percorre as 20 primeiras linhas de data_list.
    contador += 1                              # Contador vai incrementando + 1 adicionando valor a legenda.
    print("Linha: {}\n{}".format(contador, i)) # Print legenda linha + número linha, e os dados das linhas.

# TAREFA 1
# Concluida código exibe, linha 0 até 19, as primeiras 20 linhasself.

# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

input("Aperte Enter para continuar...")
# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas

print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")
sample = data_list[:20]                     #Le as primeiras 20 linhas e coloca na variavel sample.
for gender in sample:                       #Faz a leitura de gneero nas linhas
    print("Genero: {}".format(gender[-2]))  #Ele printa a coluna genero indicando pelo indice em cada linha.

# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros

input("Aperte Enter para continuar...")
# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem
def column_to_list(data_list, index):
    """Função realiza a leitura dos dados de cada coluna e adiciona a uma lista.
    Argumentos:
    Na lista data_lista: recebendo a lista entrada.
    index: refere-se ao indice coluna que será lida.
    Retornando:
    Lista com valores de uma coluna referencia sendo a  mesma ordem que se encontra na lista inicial.
    """
    column_list = []
    # Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature pelo seu índice, e dar append para uma lista
    for i in data_list:
        column_list.append(i[index])
    return column_list


# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função parTODO isso.
male = 0
female = 0

for gender in data_list:           # Para diferenciar genero dentro de data_lista.
    if (gender[-2] == 'Male'):     # Verificamos na coluna de generos se o genero é masculino ou feminino.
        male += 1                  # Adicionaremos + 1 ao contator de genero referente ao genero incrementado
    elif(gender[-2] == 'Female'):  # Verifica na coluna de generos se o genero é masculino ou feminino.
        female += 1                # Adicionaremos + 1 ao contator de genero referente ao genero incrementado.


# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Por que nós não criamos uma função parTODO isso?
# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)
def count_gender(data_list):
    """Função realizará  contagem dos generos e irá adicionar a uma lista para cada genero.
    Argumentos:
    lista data_lista receberá a lista de entrada.
    Retornando:
    retornará uma lista com [count_male, count_female].
    """
    male = 0
    female = 0
    for gender in data_list:
        if (gender[-2] == 'Male'):
            male += 1
        elif(gender[-2] == 'Female'):
            female += 1
    return [male, female]

print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Masculino", "Feminino", ou "Igual" como resposta.
def most_popular_gender(data_list):
   """Esta função realizará contagem dos generos, verificando a maiorrecorrencia entre eles.
    Argumentos:
    data_list: receberá o argumento que é a lista entrada dos dados.
    Retornará:
    retornar answer: responderá qual o genero com maior recorrencia.
    """
    answer = ""
    male = count_gender(data_list)[0]
    female = count_gender(data_list)[1]
    if male > female:
        answer = 'Masculino'

    elif female > male:
        answer = 'Feminino'

    else:
        answer = 'Iguais'
    return answer


print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Male", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.
print("\nTAREFA 7: Verifique o gráfico!")

def count_user(data_list):
"""Função Realizará  contagem de tipos dos usuários e adicionará uma lista para cada tipo distinto.
Argumentos:
data_list: lista de entrada.
Retorna:
[subscriber, customer]: retornando uma lista com os tipos dos usuários.
"""
    subscriber = 0
    customer = 0
    for user in data_list:
        if (user[-3] == 'Subscriber'):
            subscriber += 1
        elif(user[-3] == 'Customer'):
            customer += 1
    return [subscriber, customer]


# Se tudo está rodando como esperado, verifique este gráfico!
user_list = column_to_list(data_list, -3)
types = ["Subscriber", "Customer"]
quantity = count_user(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Tipo de Usuário')
plt.xticks(y_pos, types)
plt.title('Quantidade por Tipo de Usuário')
plt.show(block=True)


input("Aperte Enter para continuar...")
# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Escreva sua resposta aqui."
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas parTODO isso, como max() e min().
perc_duration_lista = column_to_list(data_list, 2)
min_trip = 0.
max_trip = 0.
mean_trip = 0.
median_trip = 0.

trip_duration_list_int = []                   # Lista vazia, receberá a lista trip_duration_list convertida para int.

for index in trip_duration_list:              # Loop for que converte cada elemento str da lista trip_duration_list em elementos do tipo int.
    trip_duration_list_int.append(int(index))

trip_duration_list_sort = sorted(trip_duration_list_int) # Ordena a lista trip_duration_list_int.

min_trip = trip_duration_list_sort[0]    # Cria lista ordenada com seu valor minimo é o seu primeiro elemento.
max_trip = trip_duration_list_sort[-1]   # Com lista ordenada seu valor máximo é o seu elemento final.
mean_trip = sum(trip_duration_list_sort)/len(trip_duration_list_sort) # Calculo da média.

# Calcular mediana, elemento central da lista ordenada.
length_of_list = len(trip_duration_list_sort)
if length_of_list % 2 == 0:
    median_trip = (trip_duration_list_sort[int((length_of_list/2)-1)] + trip_duration_list_sort[int((length_of_list/2))])/2
else:
    median_trip = trip_duration_list_sort[int(((length_of_list-1)/2))]

print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()
start_stations_list = column_to_list(data_list, 3) # Recebendo os dados da coluna start_stations e adicionando-os a uma lista.
user_types = set(start_stations_list)              # Verificando quantos nomes de estações diferentes estão cadastradas.

print("\nTAREFA 10: Imprimindo as start stations:")
print(len(user_types))
print(user_types)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(user_types) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 11
# Volte e tenha certeza que você documenteou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
# def new_function(param1: int, param2: str) -> list:
      """
      Função de exemplo com anotações.
      Argumentos:
          param1: O primeiro parâmetro.
          param2: O segundo parâmetro.
      Retorna:
          Uma lista de valores x.

      """

input("Aperte Enter para continuar...")
# TAREFA 12 - Desafio! (Opcional)
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
print("Você vai encarar o desafio? (yes ou no)")
answer = "no"

def count_items(column_list):
    item_types = []
    count_items = []
    return item_types, count_items


if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 11: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 11: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 11: Resultado de retorno incorreto!"
    # -----------------------------------------------------