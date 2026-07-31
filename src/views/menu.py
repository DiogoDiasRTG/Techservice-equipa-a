from src.models.tecnico import Tecnico
from src.models import tecnico
from src.repositories.tecnico_repository import inserir, listar, procurar_por_id, atualizar, remover, linha_para_tecnico

def main():
    print("Técnicos - Sistema de Gestão de Assistência Técnica")


while True:
    print("1. Inserir técnicos")
    print("2. Listar técnicos")
    print("3. Atualizar técnicos")
    print("4. Remover técnicos")
    print("0. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
      
      
      nome = input("Digite o nome do técnico: ")
      especialidade = input("Digite a especialidade do técnico: ")
      telefone = input("Digite o telefone do técnico: ")
      email = input("Digite o email do técnico: ")
      tecnico = inserir(Tecnico(nome=nome, especialidade=especialidade, telefone=telefone, email=email))
      print(f"Técnico {tecnico.nome} inserido com sucesso!")

    elif opcao == "2":

        tecnicos = listar()
        if tecnicos:
            print("\n=== Lista de Técnicos ===")
            for tecnico in tecnicos:
                print(f"ID: {tecnico['id_tecnico']}, Nome: {tecnico['nome']}, Email: {tecnico['email']}, Telefone: {tecnico['telefone']}, Especialidade: {tecnico['especialidade']}")
        else:
            print("Nenhum técnico encontrado.")
      

    elif opcao == "3":

        id_tecnico = int(input("Digite o ID do técnico que deseja editar: "))
        nome = input("Digite o novo nome do técnico: ")
        email = input("Digite o novo email do técnico: ")
        telefone = input("Digite o novo telefone do técnico: ")
        especialidade = input("Digite a nova especialidade do técnico: ")

        tecnico = Tecnico(nome=nome, email=email, telefone=telefone, especialidade=especialidade, id_tecnico=id_tecnico)
        atualizar(tecnico)
        print(f"Técnico com ID {id_tecnico} atualizado com sucesso.")

    elif opcao == "4":

        id_tecnico = int(input("Digite o ID do técnico que deseja remover: "))
        remover(id_tecnico)
        print(f"Técnico com ID {id_tecnico} removido com sucesso.")



        


    elif opcao == "0":
        print("Sair do programa...")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")          

