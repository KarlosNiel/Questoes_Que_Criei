#Faça um gerador de Matriz de numeros >= 0 onde a quantidade de linhas, colunas e os valores será definidos pelo usuário e imprima a matriz em seguida, realize uma operação que será decidida pelo usuário de soma (+) ou multiplicação (*) e em seguida defina qual linha sera utilizada no proscesso e a imprima, no final imprima a soma ou a multiplicação.

#Variáveis para definir a quantidade de linhas e colunas:
linhas_da_matriz = int(input("Digite a quantidade de linhas terá a matriz: "))
colunas_da_matriz = int(input("Digite a quantidade de colunas terá a matriz: "))

#Matriz vazia onde serão adcionados os elementos:
matriz = []
#Repetição para gerar as linhas:
for l in range(linhas_da_matriz):
    linha = []
    #Repetição para adcionar os números dentros da linhas que serão as colunas:
    for c in range(colunas_da_matriz):
        #Valores que serão escolhidos pelo usuário:
        num = float(input(f"[{l}, {c}] Digite os valores da matriz: "))
        #Adicionar os números a linha sem usar append:
        linha[len(linha):] = [num]
    #Adcionar as linhas na matriz:
    matriz[len(matriz):] = [linha]

print()
#Imprimir a matriz:
print("Veja como ficou sua matriz: ")
print("=" * 80)
for l in matriz:
    print(f"{l}", end="\n")
print("=" * 80)
print()

#Definição de qual operação será feita:
operaçao = str(input("Digite (+) para somar, (x) para multiplicar: "))

#Variaveis para as operações:
soma = 0 
multiplicar = 1

#Linha que sera feita a operação
num_da_linha = int(input("Qual linha você quer realizar a operação (lembre-se que a quantidade de linhas começa no zero e vai até o total - 1): "))

#Repetição para caso a linha seja o indíce zero:
if num_da_linha == 0:
    for l in range(0, num_da_linha + 1):
        #imprimir a linha:
        print(f"Linha que será usada na operção: {matriz[l]}")
        for c in range(colunas_da_matriz):
            #realizar as operações:
            soma += matriz[l][c]
            multiplicar *= matriz[l][c]
    
#Repetição caso a linha seja maior que o indíce zero:
if num_da_linha > 0:
    for l in range(num_da_linha, num_da_linha + 1):
        print(f"Linha que será usada na operação: {matriz[l]}")
        for c in range(colunas_da_matriz):
            soma += matriz[l][c]
            multiplicar *= matriz[l][c]

#Imprimi o resultado da operaçõe escolhida:
if operaçao == "+":
    print(f"O resultado da soma é: {soma:.1f}")

if operaçao == "x":
    print(f"O resultado da multiplicação é: {multiplicar:.1f}")

print("=" * 80)
