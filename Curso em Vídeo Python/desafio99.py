from time import sleep
def maior(*valores):
    print('-='*30)
    print('Analisando os valores passados...')
    for i, v in enumerate(valores):
        print(v, end=' ', flush=True)
        sleep(0.5)
    print(f'Foram informados {len(valores)} valores ao todo.')
    print(f'O maior valor informado foi {max(valores)}.')
maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior(0)
