# Cadastro Simples

Aplicação de terminal feita em Python para cadastrar pessoas e consultar os registros salvos em um arquivo de texto. O projeto está organizado na pasta [`cadastro_simples/`](cadastro_simples/).

## Funcionalidades

- Listar as pessoas já cadastradas, exibindo nome e idade.
- Adicionar uma pessoa informando nome e idade.
- Atualizar a idade de uma pessoa encontrada pelo nome.
- Excluir um cadastro pelo nome.
- Validar a idade para aceitar apenas números inteiros; entradas inválidas podem ser digitadas novamente.
- Encerrar o programa pelo menu.
- Criar o arquivo de dados automaticamente quando ele ainda não existir.

## Estrutura

```text
cadastro_simples/
├── Cadastro_simples.py       # Menu principal e fluxo do programa
├── cadastro.txt              # Registros armazenados como nome;idade
└── lib/
    ├── arquivo/__init__.py    # Criação, leitura, cadastro, atualização e exclusão
    └── interface/__init__.py # Menu, cabeçalhos e leitura de números inteiros
```

Cada registro é gravado em uma linha de `cadastro.txt`, no formato `nome;idade`. Para atualizar ou excluir um registro, informe o nome exatamente como foi cadastrado. A atualização altera a idade; a exclusão remove o registro correspondente. Se houver mais de um registro com o mesmo nome, essas operações afetam todos eles. O arquivo incluído está vazio inicialmente.

## Como executar

Com Python 3 instalado, entre na pasta do projeto e execute:

```bash
cd cadastro_simples
python Cadastro_simples.py
```

No menu, escolha:

1. **Ver Pessoas Cadastradas**
2. **Cadastrar nova Pessoa**
3. **Atualizar dados** — informe o nome e a nova idade.
4. **Excluir cadastro** — informe o nome da pessoa.
5. **Sair do Sistema**

Os dados são salvos no arquivo `cadastro.txt` no diretório de execução.
