conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}

conjunto_uniao = conjunto.union(conjunto2)

print(conjunto_uniao)

conjunto_interseccao = conjunto.intersection(conjunto2)
print(conjunto_interseccao)

conjunto_diferenca1 = conjunto.difference(conjunto2)
conjunto_diferenca2 = conjunto2.difference(conjunto)
print(conjunto_diferenca1)
print(conjunto_diferenca2)

conjunto_dif_simetrica = conjunto.symmetric_difference(conjunto2)
print(conjunto_dif_simetrica)

# conjunto = {1, 2, 3, 4}
# conjunto.add(5)
# conjunto.discard(2)
# print(conjunto)