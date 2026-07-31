from src.models import tecnico
from src.models.tecnico import Tecnico
from src.repositories.tecnico_repository import inserir



while True:
    print("1. Inserir técnicos")
    print("2. Listar técnicos")
    print("3. Gerir técnicos")
    print("4. Apagar técnicos")
    print("0. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

      nome = input("Digite o nome do técnico: ")
      telefone = input("Digite o telefone do técnico: ")
      email = input("Digite o email do técnico: ")
      especialidade = input("Digite a especialidade do técnico: ")

      tecnico = inserir(tecnico(nome=nome, telefone=telefone, email=email, especialidade=especialidade))

      print(f"Técnico {tecnico.nome} inserido com sucesso!")
      

    if opcao == "2":

     tecnico=listar()
     if tecnico:
        
        print("Lista de técnicos:")
        for tecnico in tecnico:
            print(f"ID: {tecnico.id_tecnico}, Nome: {tecnico.nome}, Telefone: {tecnico.telefone}, Email: {tecnico.email}, Especialidade: {tecnico.especialidade}")
        else:
            print("Nenhum técnico encontrado.")    

    if opcao == "3":

     

    if opcao == "4":


    if opcao == "0":
        print("Sair do programa...")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")          
\
