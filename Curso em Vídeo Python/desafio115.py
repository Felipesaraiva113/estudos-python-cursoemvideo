from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep
arq = 'texto.txt'
if  not arquivoExiste(arq):
    criarArquivo(arq)
while True:
    resposta=menu(['Ver pessoas cadastradas','Cadastrar nova Pessoas','Sair do Sistema'])
    match resposta:
        case 1:
            lerArquivo(arq)
        case 2:
            cabeçalho('NOVO CADASTRO')
            nome = str(input('Nome: '))
            idade = leiaInt('Idade: ')
            cadastrar(arq,nome,idade)
        case 3:
            cabeçalho('Saindo do sistema... Até logo!')
            break
        case _:
            print('ERRO! Digite uma opção válida')
    sleep(2)
                    