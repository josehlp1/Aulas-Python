import shutil

def escrever_arquivo(texto):
    diretorio = 'C:/Users/Win10/Desktop/teste.txt'
    arquivo = open(diretorio, 'a')
    arquivo.write(texto)
    arquivo.close()


def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()


def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)


def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    aluno_nota = aluno_nota.split('\n')
    lista_media = []
    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        media = lambda notas: sum(int(i) for i in notas) / 4
        lista_media.append({aluno:media(lista_notas)})

    return lista_notas

def copia_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo, 'C:/Users/Win10/Desktop/')

def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, 'C:/Users/Win10/Desktop/')

if __name__ == '__main__':

    move_arquivo('notas.txt')
    # print(media_notas('notas.txt'))
    # aluno = '\nCesar,7,9,3,8'
    # atualizar_arquivo('notas.txt', aluno)
    # ler_arquivo('teste.txt')
    # escrever_arquivo('teste 123')
