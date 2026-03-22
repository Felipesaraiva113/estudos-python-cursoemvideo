def leiaInt(text):
    while True:
        try:
            n = int(input(text))
        except(ValueError, TypeError):
            print('\033[31mPor favor, digite um número inteiro válido.\033[m') 
        except KeyboardInterrupt:
            print('\033[31mO usuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n
def leiaFloat(text):
    while True:
        try:
            n = float(input(text))
        except(ValueError, TypeError):
            print('\033[31mPor favor, digite um número real válido.\033[m') 
        except KeyboardInterrupt:
            print('\033[31mO usuário preferiu não digitar esse número.\033[m')
            return 0 
        else:
            return n
 