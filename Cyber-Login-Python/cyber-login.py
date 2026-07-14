import json

cyberlogin = []

with open('cyberlogin.json', 'r', encoding='utf-8') as f:
    cyberlogin = json.load(f)

def create_account():
    username = input("Nome de usuário: ")
    password = input("Senha: ")
    cyberlogin.append({"username": username, "password": password})
    save_data()
    print("Conta criada com sucesso.")

def login():
    username = input("Nome de usuário: ")
    password = input("Senha: ")
    for user in cyberlogin:
        if user.get("username") == username and user.get("password") == password:
            print("Login bem-sucedido.")
            return True
    print("Usuário ou senha incorretos.")
    return False

def main_menu():
    while True:
        print("Bem-vindo ao Cyber Login!")
        print("1. Criar conta")
        print("2. Fazer login")
        print("0. Sair")
        input_option = input("Escolha uma opção: ")
        if input_option == "1":
            create_account()
        elif input_option == "2":
            login()
        elif input_option == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")

def show_profile ():
    print("Perfil do usuário")

def linux_menu ():
    print("Menu Linux (placeholder)")


def save_data():
    with open('cyberlogin.json', 'w', encoding='utf-8') as f:
        json.dump(cyberlogin, f)

def load_data():
    global cyberlogin
    try:
        with open('cyberlogin.json', 'r', encoding='utf-8') as f:
            cyberlogin = json.load(f)
    except Exception:
        cyberlogin = []

#################

if __name__ == '__main__':
    load_data()
    main_menu()