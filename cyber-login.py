import json

FILE_NAME = "cyberlogin.json"
cyberlogin = []


def save_data():
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(cyberlogin, file, indent=4, ensure_ascii=False)


def load_data():
    global cyberlogin

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            cyberlogin = json.load(file)

    except FileNotFoundError:
        cyberlogin = []

    except json.JSONDecodeError:
        print("O arquivo JSON está corrompido ou vazio.")
        cyberlogin = []


def create_account():
    username = input("Nome de usuário: ").strip()
    password = input("Senha: ").strip()

    if not username or not password:
        print("Usuário e senha não podem ficar vazios.")
        return

    for user in cyberlogin:
        if user.get("username", "").lower() == username.lower():
            print("Esse nome de usuário já existe.")
            return

    account = {
        "username": username,
        "password": password,
        "role": "Cyber Security Student",
        "status": "Offline",
        "linux": None
    }

    cyberlogin.append(account)
    save_data()

    print("Conta criada com sucesso.")


def login():
    for attempt in range(3):
        username = input("Nome de usuário: ").strip()
        password = input("Senha: ").strip()

        for user in cyberlogin:
            if user.get("username") == username and user.get("password") == password:
                user["status"] = "Online"
                save_data()

                print("Login bem-sucedido.")
                return user

        remaining = 2 - attempt
        print(f"Usuário ou senha incorretos. Tentativas restantes: {remaining}")

    print("Número máximo de tentativas atingido.")
    return None


def show_profile(user):
    print("\n===== PERFIL =====")
    print(f"Usuário: {user['username']}")
    print(f"Cargo: {user['role']}")
    print(f"Status: {user['status']}")

    if user["linux"]:
        print(f"Distribuição Linux: {user['linux']}")
    else:
        print("Distribuição Linux: não cadastrada")


def linux_menu(user):
    if user["linux"]:
        print(f"Sua distribuição favorita é: {user['linux']}")
        return

    distro = input("Cadastre sua distribuição Linux favorita: ").strip()

    if not distro:
        print("A distribuição não pode ficar vazia.")
        return

    user["linux"] = distro
    save_data()

    print("Distribuição salva com sucesso.")


def user_menu(user):
    while True:
        print("\n===== PAINEL =====")
        print("1. Ver perfil")
        print("2. Linux")
        print("0. Deslogar")

        option = input("Escolha uma opção: ").strip()

        if option == "1":
            show_profile(user)

        elif option == "2":
            linux_menu(user)

        elif option == "0":
            user["status"] = "Offline"
            save_data()
            print("Logout realizado.")
            break

        else:
            print("Opção inválida.")


def main_menu():
    while True:
        print("\nBem-vindo ao Cyber Login!")
        print("1. Criar conta")
        print("2. Fazer login")
        print("0. Sair")

        input_option = input("Escolha uma opção: ").strip()

        if input_option == "1":
            create_account()

        elif input_option == "2":
            logged_user = login()

            if logged_user:
                user_menu(logged_user)

        elif input_option == "0":
            print("Sistema encerrado.")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    load_data()
    main_menu()