from database.session import session
from models.cliente import Cliente

#Função de cadastro de cliente
def cadastrar_cliente():

    try:
        nome = input("Insira o nome do cliente: ")
        telefone = input("Insira o telefone do cliente: ")
        
        if not telefone.isdigit():
            raise Exception("Telefone não é válido! Insira apenas números.")
    
        cliente = Cliente(nome, telefone)

        #O add faz o trabalho de fazer o INSERT
        session.add(cliente)
        
        session.commit()

    except Exception as e:
        print(e)

    finally:
        input()