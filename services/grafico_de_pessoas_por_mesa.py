from typing import Tuple
import matplotlib.pyplot as plt #Importando a biblioteca matplotlib
from models.mesa import Mesa #Trazendo a tabela mesa
from services.mostrar_reserva import mostrar_reservas, get_reservas

def grafico_de_pessoas_por_mesa():

    mesas: Tuple[Mesa] = get_reservas()

    pessoas_por_mesa = tuple(map(lambda x: x.qtd_pessoas, mesas)) #Com o map, está aplicando a função lambda para cada parâmetro

    clientes_da_mesa = tuple(map(lambda x: x.cliente.nome, mesas))

    grafico = dict() #Dicionário para mapear os valores
    grafico["y"] = pessoas_por_mesa
    grafico["x"] = clientes_da_mesa

    plt.plot(grafico["x"], grafico["y"])

    plt.ylabel('Pessoas') #Y = Pessoas
    plt.xlabel('Mesa') #X = Mesa

    plt.show()
