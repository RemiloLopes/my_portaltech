nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))
faltas = int(input("Digite as faltas do aluno:"))
soma = nota1 + nota2
media = soma / 2
if media >= 7 and faltas <= 3:
    print("O aluno está aprovado! Com média", media, "e", faltas, "faltas.")
else:
    print("O aluno está reprovado! Com média", media, "e", faltas, "faltas.")