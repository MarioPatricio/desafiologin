nome = ["fulano"]
senha = [123]
len(nome)
cont = 1
while cont == 1:
    tent = 0
    vez = 3
    print("Digite:\n"
              f"1 --> Cadastro\n"
              f"2 --> Mostrar\n"
              f"3 --> Login\n"
              f"4 --> Sair")
    opcao = int(input("Qual operação você deseja realizar? "))
    while opcao < 1 or opcao > 4:
            opcao = int(input("Opção inválida, digite novamente:  "))
    match opcao:
            case 1:
                print("--Cadastro--")
                username = input("Coloque seu nome de usuário: ")
                for i in range(len(nome)):
                    while username == nome[i]:
                        username = input("Esse usuário já existe. Tente novamente: ")
                else:
                        nome.append(username)
                password = int(input("Coloque sua senha (apenas números): "))
                senha.append(password)
                print("Cadastro concluído!")
                print()
            case 2:
                print("--Mostrar--")
                print(nome, senha)
                print()
            case 3:
                print("--Login--")
                username = input("Insira seu usuário: ")
                for i in range(len(nome)):
                    while username != nome[i]:
                        username = input("Usuário inexistente. Tente novamente: ")
                else:
                    password = int(input("Insira sua senha: "))
                    for i in range(len(senha)):
                        while password != senha[i]:
                            password = int(input(f"Senha incorreta. Tente mais {vez} vezes: "))
                            tent += 1
                            vez -= 1
                            if tent == 3:
                                print("Conta bloqueada.")
                                exit()
                    print("Login efetuado!")
                    break
            case 4:
                print("Saindo da plataforma.")
                break