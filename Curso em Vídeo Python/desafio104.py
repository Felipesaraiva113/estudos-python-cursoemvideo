def leiaInt(text):
    global n
    while True:
        n=input(text).strip()
        if n.isnumeric():
            return n
        else:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')   
print('-'*40)
n=leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
  
