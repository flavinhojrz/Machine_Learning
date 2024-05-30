#Bubble Sort é um algoritmo de ordenação simples que funciona comparando cada elemento com o próximo, e trocando-os de lugar se eles estiverem em ordem incorreta.
#O algoritmo repete esse processo várias vezes, até que todos os elementos estejam ordenados. 
#A cada passagem, o maior elemento "flutua" para o final do array, como uma bolha, dando origem ao nome do algoritmo.

lista = [6,7,8,3,10,19,4,1,0,61,30,16,17,82,29,34,43,21,11,39,56,67,12]

def bubble_sort(arr):
	n = len(arr)
	for i in range(n):
		for j in range(0, n - i - 1):
			if(arr[j] > arr[j+1]):
				arr[j], arr[j+1] = arr[j+1], arr[j]
	return arr

print("Array antes do bublle sort: ", lista)
print("Array depois do bubble sort: ", bubble_sort(lista))