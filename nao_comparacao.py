def counting_sort(arr):
    if len(lista) == 0:
        return lista

    max_val = max(lista)
    min_val = min(lista)

    contagem = [0] * (max_val - min_val + 1)

    for num in lista:
        contagem[num - min_val] += 1

    lista_ordenada = []
    for i, freq in enumerate(contagem):
        lista_ordenada.extend([i + min_val] * freq)

    return lista_ordenada

lista = [4, 2, 2, 8, 3, 3, 1]
print("Lista ordenada com Counting Sort:", counting_sort(lista))
