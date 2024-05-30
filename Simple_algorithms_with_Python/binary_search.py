# A busca binária é um algoritmo extremamente eficiente, capaz de encontrar um dado específico em meio a bilhões de dados em menos poucas dezenas de operações, 
# o que é irrisório para um computador com a capacidade de processamento atual. 
# A única condição importante como pré-requisito ao seu uso é que a lista de registros esteja ordenada. 

from bubble_sort import bubble_sort, lista

def binary_search(arr, item, begin=0, end=None):
  if end is None:
    end = len(arr) - 1
  if begin <= end:
    m = (begin + end) // 2
    if arr[m] == item:
      return m
    if item < arr[m]:
      return binary_search(arr, item, begin, m-1)
    else: 
      return binary_search(arr, item, m+1, end)
  return None

print("Buscando elementos na lista usando o algoritimo Binary Search")
# Usando o Bubble sort para ordenar a lista
lista_ordenada = bubble_sort(lista)

# Agora podemos buscar um elemento especifico na lista
print("O elemento 16 está na posição",binary_search(lista_ordenada, 16))
# Buscando um elemento que não está na lista
print("Caso um elemento não esteja na lista o algoritimo retona",binary_search(lista_ordenada, 68))