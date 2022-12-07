from datetime import datetime
from typing import List
from models.cliente import Cliente
from models.mesa import Mesa
from database.session import session
from services.mostrar_reserva import mostrar_reservas, get_reservas

get_mesa_by_id = lambda mesas, mesa_id: next(m for m in mesas if m.id == mesa_id)

#Função para cancelar reserva criada
def cancelar_reserva():
    try:
        mesas: List[Mesa] = tuple(session.query(Mesa).order_by(Mesa.data)) #Trazendo a lista mesa por sua data

        reservas = get_reservas()

        lista_de_codigo_das_reservas = tuple(map(lambda c: c.id, reservas))

        mostrar_reservas(reservas)
        
        mesa_id = int(input("Qual mesa será cancelada? Insira o ID: ")) #Selecionar qual mesa será cancelada pelo seu id

        if mesa_id not in lista_de_codigo_das_reservas:
            raise Exception("Reserva não existe")
        
        mesa = get_mesa_by_id(mesas, mesa_id)

        session.delete(mesa)
        session.commit()

    except Exception as e:
        print(e)

    finally:
        input()

