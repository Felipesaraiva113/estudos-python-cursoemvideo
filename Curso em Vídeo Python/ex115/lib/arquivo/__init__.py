from ex115.lib.interface import *
def arquivoExiste(nome):
    try:
        a=open(nome,'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')
def lerArquivo(arq):
    try:
        a=open(arq, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabeçalho('ATIVIDADES CADASTRADAS')
        atividades = []
        for linha in a:
            dado = linha.strip().split(';')
            if len(dado) == 4:
                categoria = dado[0]
                materia = dado[1]
                dia = int(dado[2])
                mes = int(dado[3])
                atividades.append((mes, dia, categoria, materia))
        if atividades:
            atividades.sort()
            c = 0
            for mes, dia, categoria, materia in atividades:  
                c+= 1
                print(f'{c} {categoria} de {materia}: {dia}/{mes}')
        else:
            print('Nenhuma atividade encontrada.')       
    finally:
        a.close()
def cadastrar(arq,categoria,materia,dia,mes):
    try:
        a = open(arq,'at') 
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{categoria};{materia};{dia};{mes}\n')   
        except:
            print('Houve um ERRO na hora de escrever os dados!')     
        else:
            print(f'Novo registro de {categoria} adicionado.')
            a.close()
def filtro(arq,m):
    try:
        a=open(arq, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabeçalho('ATIVIDADES CADASTRADAS')
        existem = []
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            dado[3] = dado[3].strip()
            existem.append(dado[0])
            existem.append(dado[1]) 
            existem.append(dado[2]) 
            existem.append(dado[3])
            if existem:
                    if dado[3].strip() == m:
                            print(f'{dado[0]} de {dado[1]}: {dado[2]}/{dado[3]}')
            else:
                print('Nenhuma atividade encontrada.')
    finally:
        a.close()

def remover(arq, ca, m, d, me):
    try:
        # 1. Abrir para leitura
        with open(arq, 'rt') as arquivo_leitura:
            manter = []
            for linha in arquivo_leitura:
                dado = linha.strip().split(';')
                if len(dado) == 4:
                    categoria = dado[0]
                    materia = dado[1]
                    dia = int(dado[2])
                    mes = int(dado[3])

                    # 2. Verifica se NÃO é a linha que queremos remover
                    if not (categoria == ca and materia == m and dia == d and mes == me):
                        manter.append((categoria, materia, dia, mes))

        # 3. Abrir para escrita e salvar apenas as atividades mantidas
        with open(arq, 'wt') as arquivo_escrita:
            for categoria, materia, dia, mes in manter:
                arquivo_escrita.write(f'{categoria};{materia};{dia};{mes}\n')

        print(f'Registro de {ca} de {m} no dia {d}/{me} removido com sucesso.')

    except Exception as e:
        print(f'Houve um erro ao remover a atividade: {e}')