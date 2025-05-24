nomes = ["pedro","joâo","mateus"]
notas = [[10,8,8],[8,9,9],[5,7,9]]

media1 = sum(notas[0]) / len(notas[0])
media2 = sum(notas[1]) / len(notas[1])
media3 = sum(notas[2]) / len(notas[2])

print("a media do aluno(a)",nomes[0]," é ", media1)
print("a media do aluno(a)",nomes[1]," é ", media2)
print("a media do aluno(a)",nomes[2]," é ", media3)

mediaclasse = (media1+media2+media3)/3
print("a media da classe é",mediaclasse)

maior = max(media1,media2,media3)
print("a maior media é",maior)
