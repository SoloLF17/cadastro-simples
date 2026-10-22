import lib.interface
from lib.interface import cabeçalho


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
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
        print('Houve um ERRO na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler arquivo!')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30} {dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq,'at')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado!')
            a.close()


def atualizar(nome='desconhecido',idade=0):
    nome_alvo = nome
    nova_idade = idade
    linhas_atualizadas = []
    arquivo = "cadastro.txt"
    try:
        with open("cadastro.txt", "r", encoding="utf-8") as f:
            for linha in f:
                if linha.strip():
                    nome, idade = linha.strip().split(";")

                    # Se achar o nome, atualiza os dados
                    if nome == nome_alvo:
                        linha = f"{nome};{nova_idade}\n"
                    elif nome != nome_alvo:
                        print('\033[0;31mERRO ao acessar arquivos NOME ou IDADE inválidos!\033[m')

                    linhas_atualizadas.append(linha)
        # Salva o arquivo com os dados atualizados
        with open("cadastro.txt", "w", encoding="utf-8") as f:
            f.writelines(linhas_atualizadas)
            print('Cadastro atualizado com sucesso!')
    except FileNotFoundError:
            print(f"Erro: O arquivo '{arquivo}' ainda não existe.")
    except PermissionError:
        print(f"Erro: Você não tem permissão para modificar o arquivo '{arquivo}'.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")


def excluir(nome='desconhecido'):
    nome_para_remover = nome
    linhas_restantes = []
    arquivo = "cadastro.txt"

    try:
        # 1. Tenta ler o arquivo
        with open(arquivo, "r", encoding="utf-8") as f:
            for linha in f:
                if linha.strip():
                    nome, idade = linha.strip().split(";")

                    # Guarda apenas quem NÃO for a pessoa a ser removida
                    if nome != nome_para_remover:
                        linhas_restantes.append(linha)

        # 2. Tenta salvar o arquivo modificado
        with open(arquivo, "w", encoding="utf-8") as f:
            f.writelines(linhas_restantes)

        print(f"Operação concluída. Se '{nome_para_remover}' existia, foi removido.")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo}' ainda não existe.")
    except PermissionError:
        print(f"Erro: Você não tem permissão para modificar o arquivo '{arquivo}'.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
