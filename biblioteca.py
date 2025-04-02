import json
print("Bem vindo a Livraria de Jey Victor Malta")

# Arquivo para persistência de dados
ARQUIVO_LIVROS = "livros.txt"

def load_book():
    """Carregar livros salvos do arquivo."""
    try:
        with open(ARQUIVO_LIVROS, "r", encoding="utf-8") as f:
            return [json.loads(line) for line in f if line.strip()]
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_book():
    """Salvar a lista de livros em um arquivo TXT."""
    with open(ARQUIVO_LIVROS, "w", encoding="utf-8") as f:
        for book in list_book:
            f.write(json.dumps(book) + "\n")


list_book = load_book()
# Determinar o maior ID existente
id_global = max([int(book["id"]) for book in list_book], default=0)


def save_books():
    """Função para salvar a lista de livros em um arquivo TXT."""
    with open(ARQUIVO_LIVROS, "w") as f:
        for book in list_book:
            f.write(json.dumps(book) + "\n")

def register_book(id):
    """Função para cadastrar um livro."""
    width = 70
    print("-" * width)
    print("MENU CADASTRAR LIVRO".center(width, "-"))
    id = int(input("Id do livro: "))
    name = input("Por favor entre com o nome do livro: ")
    author = input("Por favor entre com o autor do livro: ")
    publisher = input("Por favor entre com a editora do livro: ")

    book = {"id": id, "name": name, "author": author, "publisher": publisher}
    list_book.append(book)
    save_books()
    print("Livro cadastrado com sucesso!\n")

def format_book(book):
    """Formata a exibição do livro para melhorar visualização."""
    return f"""
    id: {book['id']}
    nome: {book['name']}
    autor: {book['author']}
    editora: {book['publisher']}
    """

def query_book():
    """Função para consultar livros."""
    while True:
        width = 70
        print("-" * width)
        print("MENU CONSULTAR LIVRO".center(width, "-"))
        print("Escolha a opção desejada:")
        print("1 - Consultar Todos os Livros\n2 - Consultar por Id\n3 - Consultar Livro(s) por autor\n4 - Retornar")
        option = input(">>")

        if option == "1":
            for book in list_book:
                print(format_book(book))
        elif option == "2":
            id_query = int(input("Digite o id do livro: "))
            book_found = next(
                (book for book in list_book if int(book["id"]) == id_query), None)
            if book_found:
                print(format_book(book_found))
            else:
                print("Id inválido!")
        elif option == "3":
            author_query = input("Digite o autor do(s) livro(s): ")
            books_author = [
                book for book in list_book if book["author"] == author_query]
            if books_author:
                for book in books_author:
                    print(format_book(book))
            else:
                print("Nenhum livro encontrado para este autor.")
        elif option == "4":
            break
        else:
            print("Opção inválida!")

def remove_book():
    """Função para remover um livro pelo ID."""
    width = 70
    print("-" * width)
    print("MENU REMOVER LIVRO".center(width, "-"))
    while True:
        try:
            id_remove = int(input("Digite o id do livro a ser removido: "))
            for book in list_book:
                if int(book["id"]) == id_remove:
                    list_book.remove(book)
                    print("Livro removido com sucesso!\n")
                    return
            print("Id inválido!")
        except ValueError:
            print("Por favor, digite um número válido.")

# Criar arquivo caso não exista
with open(ARQUIVO_LIVROS, "a", encoding="utf-8") as f: pass

# Estrutura principal do menu
while True:
    width = 70
    print("-" * width)
    print("MENU PRINCIPAL".center(width, "-"))
    print("Escolha a opção desejada:")
    print("1 - Cadastrar Livro\n2 - Consultar Livro(s)\n3 - Remover Livro\n4 - Sair")

    option = input(">>")

    if option == "1":
        id_global += 1
        register_book(id_global)
    elif option == "2":
        query_book()
    elif option == "3":
        remove_book()
    elif option == "4":
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida!")