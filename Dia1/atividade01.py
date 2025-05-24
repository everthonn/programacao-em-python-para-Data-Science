print("PRODUTOS")
print("id 0 - Celular \n id 1 - notebook \n id 2 - relogio \n id 3 - fone")

produto = [1200,2550,320,200]
valor = []
quant_prod = int(input("quantos podutos você deseja comprar?"))

for i in range(quant_prod):
        id= int(input("qual o id do item desejado?"))
        valor.append(produto[id])

print(f"o valor total da compra é: {sum(valor)} reais")