

def exibir_menu():
    print("\n--- AGENDA ---")
    print("1 Cadastrar contato")
    print("2 Listar contatos")
    print("0 Sair")
    return input("Escolha: ")

def cadastrar_contato(agenda):
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    agenda.append({"nome": nome, "telefone": telefone})
    print("Contato salvo!")

def listar_contatos(agenda):
    if not agenda:
        print("A agenda está vazia.")
    else:
        for contato in agenda:
            print(f"Nome: {contato['nome']} - Tel: {contato['telefone']}")



minha_agenda = [] 

while True:
    opcao = exibir_menu() 

    if opcao == "1":
        cadastrar_contato(minha_agenda) 
    
    elif opcao == "2":
        listar_contatos(minha_agenda) 
        
    elif opcao == "0":
        print("Saindo...")
        break
    
    else:
        print("Opção inválida!")