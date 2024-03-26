
print('\nExercicios do Módulo 3: Listas, For e Try Except\n')

print('1. Criar 3 listas')
numeros = [1, 2, 3, 5, 6, 7, 8, 9, 10]
nomes = ['Elaine', 'Jasmine', 'Gabriel', 'Caio']
anos = [2002, 2024]
print(f'{numeros}')
print(f'{nomes}')
print(f'{anos}')

print('\n2. Percorrendo lista')
for numero in numeros:
    print(f'{numeros}')
    
print('\n3. For para calcular a soma dos números ímpares de 1 a 10')
soma_impares = 0
for i in range(1, 11, 2):
    soma_impares += i
    print(soma_impares)

print('\n4. For para imprimir os números de 1 a 10 em ordem descrecente')
for i in range(10, 0, -1):
    print(i)

print('\n5. Imprimir tabuada')
numero_tabuada = int(input("Digite um número para a tabuada: "))
for i in range(1, 11):
    resultado = numero_tabuada * i
    print(f"{numero_tabuada} x {i} = {resultado}")

print('\n6. Calcular a soma de todos os elementos')
lista_numeros = [10, 5, 8, 3, 7]
soma = 0

try:
    for numero in lista_numeros:
        soma += numero
    print(f"Soma dos elementos: {soma}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
   
print('\n7. Calcular a média')
lista_valores = [15, 20, 25, 30]
soma_valores = 0

try:
    for valor in lista_valores:
        soma_valores += valor
    media = soma_valores / len(lista_valores)
    print(f"Média dos valores: {media}")
except ZeroDivisionError:
    print("A lista está vazia, não é possível calcular a média.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")