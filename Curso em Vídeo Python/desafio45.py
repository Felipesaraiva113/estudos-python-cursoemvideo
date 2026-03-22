from random import choice
opcoes = ['pedra', 'papel', 'tesoura']
computador = choice(opcoes)
usuario = input('Você escolhe pedra, papel ou tesoura? ').strip().lower()
if computador == usuario:
        print('Empate!')
elif (
        (computador == 'pedra' and usuario == 'tesoura') or
        (computador == 'papel' and usuario == 'pedra') or
        (computador == 'tesoura' and usuario == 'papel')
    ):
        print(f'Ganhei! Escolhi {computador}')
else:
     print(f'Você venceu! Escolhi {computador}')


 