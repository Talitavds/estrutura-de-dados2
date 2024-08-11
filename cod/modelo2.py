def busca_binaria (lista, x):
    esquerda = 0
    direita = len(lista) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == x:
            return meio
        elif lista[meio] < x:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1

def remover_item(lista, x):
    # Encontra o índice do item a ser removido
    indice = busca_binaria(lista, x)

    if indice != -1:
        lista.pop(indice)
        print(f'Elemento {x} removido da lista.')
    else:
        print(f'Elemento {x} não encontrado na lista.')

def executar():
    lista = []
    for i in range(1, 11):
        lista.append(i)

#user = int(input('Digite um número para verificar se esta na lista:\t'))

# CASO AFIRMATIVO
    print(lista)
    user = 2
    resultado = busca_binaria(lista, user)

    if resultado != -1:
        print(f'Elemento {user} encontrado no índice: {resultado}')
    else:
        print(f'Elemento {user} não encontrado na lista')

# CASO NEGATIVO
    user = 56
    resultado = busca_binaria(lista, user)

    if resultado != -1:
        print(f'Elemento {user} encontrado no índice: {resultado}')
    else:
        print(f'Elemento {user} não encontrado na lista')

    remover_item(lista, 5)
    print(lista)
executar()