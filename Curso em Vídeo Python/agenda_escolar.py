from ex115.lib.arquivo import* 
from ex115.lib.interface import*
from time import sleep 
def linha(tam=42):
    return '-'*tam
categoria = ('Prova', 'Trabalho', 'Tarefa')
materia = ('Matematica', 'Educacao Fisica', 'Curso Tecnico', 'Quimica', 'Geografia', 'Arte', 'Potugues', 'Biologia', 'Fisica', 'Educacao Financeira', 'Ingles', 'Historia', 'Filosofia')
arq ='escola.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)
while True:
    r = menu(['Ver atividades cadastradas','Cadastrar nova atividade','Excluir atvidade','Sair do sistema'])
    match r:
        case 1:
            sn= str(input('Quer filtrar por mês? [s/n] ')).lower().strip()
            if sn == 's':
                me = str(input('Digite o mês desejado: '))
                filtro(arq,me)
            else:
                lerArquivo(arq)
        case 2:
            cabeçalho('NOVO CADASTRO')
            r2=opçoes_categoria(categoria)
            r2a = r2-1
            cat = categoria[r2a]
            r3=opçoes_materia(materia)
            r3a = r3-1
            mat= materia[r3a]
            while True:
                dia=leiaInt('Dia: ')
                if dia >0 and dia < 31:
                    break
            while True:
                mes = leiaInt('Mês: ')
                if mes >0 and mes < 13:
                    break
            cadastrar(arq,cat,mat, dia, mes)
        case 3:
            with open(arq, 'rt') as a:
                atividades = []
                for linha in a:
                    dado = linha.strip().split(';')
                    if len(dado) == 4:
                        categoria = dado[0]
                        materia = dado[1]
                        dia = int(dado[2])
                        mes = int(dado[3])
                        atividades.append((mes, dia, categoria, materia))
            lerArquivo(arq)
            if atividades:
                print(linha())
                r2=opçoes_categoria(categoria)
                r2a = r2-1
                cat = categoria[r2a]
                r3=opçoes_materia(materia)
                r3a = r3-1
                mat= materia[r3a]
                while True:
                    dia=leiaInt('Dia: ')
                    if dia >0 and dia < 31:
                        break
                while True:
                    mes = leiaInt('Mês: ')
                    if mes >0 and mes < 13:
                        break
                remover(arq,cat,mat, dia, mes)
            
        case 4:
            cabeçalho('Saindo do sistema... Até logo!')
            break
        case _:
            print('ERRO! Digite uma opção válida')
              