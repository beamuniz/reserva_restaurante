from datetime import datetime
from database.base import Base
from database.engine import engine
from services.cadastro_de_cliente import cadastrar_cliente
from services.mostrar_reserva import mostrar_reservas, get_reservas
from services.grafico_de_pessoas_por_mesa import grafico_de_pessoas_por_mesa
from services.reservar_mesa import reservar_mesa
from services.cancelar_reserva import cancelar_reserva

# Inicia o banco de dados
Base.metadata.create_all(engine)

def menu():
    try:
        print(f"""\033[92m--=== RESTAURANTE IFSP ===--\033[0m
[1] Cadastrar Cliente
[2] Reservar Mesa
[3] Listar Reservas
[4] Cancelar Reserva
[5] Gráfico de Pessoas por Mesa
[6] Sair
--========================--
{datetime.now().strftime("%d-%m-%Y")}""")
        opcao = int(input('Escolha uma Opção ~> '))
        return opcao
    except ValueError:
        print('[!] Nenhum inteiro válido! Por favor, tente de novo... ')

#Switch Case em Python (Funcionalidade nova, desde 2021)
def controlar_menu(option):
    match option:
        case 1:
            cadastrar_cliente()
        case 2:
            reservar_mesa()
        case 3:
            mostrar_reservas(get_reservas())
            pass
        case 4:
            cancelar_reserva()
        case 5:
            grafico_de_pessoas_por_mesa()
        case 6:
            exit()
        case _:
            print("\n[!] Opção Inválida!")


while True:
    controlar_menu(menu())


