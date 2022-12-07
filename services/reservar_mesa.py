from datetime import datetime
from models.cliente import Cliente
from models.mesa import Mesa
from database.session import session

print_cliente = lambda id, nome : print(str(id) + " - " + nome)

dia_ja_reservado = lambda data : session.query(Mesa).filter(Mesa.data == data).count() > 0

#Função para reserva de mesa
def reservar_mesa():
    print("Clientes disponíveis:")

    try:
        clientes_disponiveis = list(session.query(Cliente)) #Lista para mostrar listas de clientes cadastrados

        lista_de_codigo_dos_clientes_disponiveis = list(map(lambda c: c.id, clientes_disponiveis)) #Lista para mostrar os clientes disponíveis, puxando pelo id

        for cliente in clientes_disponiveis:
            print_cliente(cliente.id, cliente.nome)

        cod_do_cliente = int(input("Código do cliente: ")) #Inserir o código do cliente

        if not cod_do_cliente in lista_de_codigo_dos_clientes_disponiveis:
            raise Exception("Não há cliente com esse código") #Parar o programa se não há código do cliente

        data = datetime.strptime(input("Dia da reserva: "), '%d/%m/%Y') #Colocar o dia da reserva

        if dia_ja_reservado(data):
            raise Exception("Oh não! Dia já foi reservado!") #Parar o programa se dia já esta reservado

        num_pessoas = int(input("Insira quantas pessoas estarão na mesa: ")) #Inserir número de pessoas que estarão na mesa

        mesa = Mesa(cod_do_cliente, data, num_pessoas)

        session.add(mesa)
        session.commit()

    except Exception as e: #Definindo um argumento para o Except
        print(e)
    finally:
        input()