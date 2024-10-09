nome = []
senha = []
t = len(nome)
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
                if username in nome:
                    print("Usuário já existe.")
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
                for x in nome:
                    if username not in nome:
                        print("Usuário inexistente.")
                    else:
                        password = int(input("Digite sua senha: "))
                    while password not in senha:
                        tent +=1
                        vez -=1
                        password = int(input(f"Senha incorreta, você tem mais {vez} vezes: "))
                        if vez == 0:
                            print("Programa bloqueado.")
                            exit()
                    else:
                        print("Login efetuado!")
                        exit()
            case 4:
                print("Saindo da plataforma.")
                break