try:
    a = int(input('numerador: '))
    b = int(input('denominador: '))
    r= a/b
except (ValueError,TypeError):
    print('tivemos um problema com o tipo de dado que você digitou.')    
except ZeroDivisionError:
    print('não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print('o usuário preferiu não informar os dados!')
except Exception as erro:
    print(f'o erro encontrado foi {erro.__cause__}')
else:
    print(f'o resultado é {r:.1f}')
finally:
    print('volte sempre!')
    print('muito obrigado!')

