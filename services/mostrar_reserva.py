from typing import Tuple
from models.mesa import Mesa
from database.session import session

get_reservas = lambda : tuple(session.query(Mesa).order_by(Mesa.data))

#Função para mostrar reservas
def mostrar_reservas(mesas: Tuple[Mesa]):
    print("Mesas reservadas:")

    for mesa in mesas:
        print(f'[{mesa.id}] {mesa.data} - {mesa.cliente.nome} - {mesa.qtd_pessoas} pessoas')