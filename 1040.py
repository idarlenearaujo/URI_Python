# entrada
grade = input()

# extrair notas N1, N2, N3, N4
v = grade.split(' ')
N1 = float(v[0])
N2 = float(v[1])
N3 = float(v[2])
N4 = float(v[3])

# variaveis de pesos das disciplinas
P1 = 2
P2 = 3
P3 = 4
P4 = 1

# calculo media das notas
Media = ((N1 * P1) + (N2 * P2) + (N3 * P3) + (N4 * P4)) / (P1 + P2 + P3 + P4)

print('Media: {:.1f}'.format(Media))

# condição de aluno aprovado, não aprovado ou recuperação
if Media >= 7:
    print('Aluno aprovado.')

elif Media < 5:
    print('Aluno reprovado.')

elif (Media <= 6.9) and (Media >= 5):
    print('Aluno em exame.')

    # nota do exame especial
    exam = float(input())

    print('Nota do exame: {:.1f}'.format(exam))

    Media2 = (Media + exam) / 2

    # condição de aluno aprovado ou não
    if Media2 >= 5:
        print('Aluno aprovado.')

    elif Media2 < 5:
        print('Aluno reprovado.')

    print('Media final: {:.1f}'.format(Media2))
