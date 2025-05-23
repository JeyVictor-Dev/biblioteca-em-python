# Biblioteca em python

Este projeto é um sistema simples de gerenciamento de livros desenvolvido em **Python**. Ele permite o **cadastro**, **consulta** e **remoção** de livros utilizando um arquivo de texto (`livros.txt`) para armazenamento de dados.

## 📌 Funcionalidades

- 📚 **Cadastro de Livros**: Registra um novo livro com **ID, nome, autor e editora**.
- 🔍 **Consulta de Livros**:
  - Exibir **todos** os livros cadastrados.
  - Buscar um livro pelo **ID**.
  - Buscar livros por **autor**.
- 🗑 **Remoção de Livros**: Exclui um livro do sistema com base no seu **ID**.

## 📁 Estrutura do Projeto

- `livros.txt`: Arquivo utilizado para armazenar os livros cadastrados.
- `register_book(id)`: Função para **cadastrar** um novo livro.
- `query_book()`: Função para **consultar** livros pelo ID, autor ou listar todos.
- `remove_book()`: Função para **remover** um livro pelo ID.
- `save_books()`: Função para **salvar** a lista de livros no arquivo.
- `load_book()`: Função para **carregar** os livros salvos do arquivo.

## 🚀 Como Executar o Programa

1. Certifique-se de ter o **Python** instalado na sua máquina (**versão 3.x**).
2. Baixe ou clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/livraria.git
   cd livraria
   ```
3. Execute o script no terminal com:
   ```bash
   python nome_do_arquivo.py
   ```
4. Navegue pelo **menu interativo** para gerenciar os livros.

## 📝 Exemplo de Uso

### 📌 Cadastro de um Livro
```plaintext
MENU CADASTRAR LIVRO
Id do livro: 1
Por favor entre com o nome do livro: O Pequeno Príncipe
Por favor entre com o autor do livro: Antoine de Saint-Exupéry
Por favor entre com a editora do livro: Agir
Livro cadastrado com sucesso!
```

### 🔍 Consulta de Livros
```plaintext
MENU CONSULTAR LIVRO
Escolha a opção desejada:
1 - Consultar Todos os Livros
2 - Consultar por Id
3 - Consultar Livro(s) por autor
4 - Retornar
```

### 🗑 Remoção de um Livro
```plaintext
MENU REMOVER LIVRO
Digite o id do livro a ser removido: 1
Livro removido com sucesso!
```

## 📌 Melhorias Futuras
- 🔹 Implementação de **interface gráfica**.
- 🔹 Utilização de **banco de dados** para melhor gerenciamento.
- 🔹 Adicionar opção de **atualização** de livros.
- 🔹 Melhorar o **tratamento de erros**.

## ✍️ Autor
**Jey Victor Malta**

Este projeto foi desenvolvido como um **exercício prático** de manipulação de arquivos e listas em **Python**.