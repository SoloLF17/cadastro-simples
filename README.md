# Cadastro Simples

Aplicação de terminal feita em Python para cadastrar pessoas e consultar os registros salvos em um arquivo de texto. O projeto está organizado na pasta [`cadastro_simples/`](cadastro_simples/).

## Funcionalidades

- Listar as pessoas já cadastradas, exibindo nome e idade.
- Adicionar uma pessoa informando nome e idade.
- Validar a idade para aceitar apenas números inteiros; entradas inválidas podem ser digitadas novamente.
- Encerrar o programa pelo menu.
- Criar o arquivo de dados automaticamente quando ele ainda não existir.

## Estrutura

```text
cadastro_simples/
├── Cadastro_simples.py       # Menu principal e fluxo do programa
├── cadastro.txt              # Registros armazenados como nome;idade
└── lib/
    ├── arquivo/              # Criação, leitura e gravação dos registros
    └── interface/            # Menu, cabeçalhos e leitura de números inteiros
```

Cada registro é gravado em uma linha de `cadastro.txt`, no formato `nome;idade`. O arquivo incluído está vazio inicialmente.

## Como executar

Com Python 3 instalado, entre na pasta do projeto e execute:

```bash
cd cadastro_simples
python Cadastro_simples.py
```

No menu, escolha **1** para ver os registros, **2** para cadastrar uma pessoa ou **3** para sair. Os dados são salvos no arquivo `cadastro.txt` no diretório de execução.
