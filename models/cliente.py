from sqlalchemy import Column, Integer, String, create_engine #Importando o banco de dados e funcionalidades
from sqlalchemy.ext.declarative import declarative_base
from database.base import Base

# Representa a tabela Cliente no banco de dados
class Cliente(Base):
    __tablename__ = 'Cliente' #Criar a tabela Cliente

    #Criando e atribuindo valores as colunas
    id = Column(Integer, primary_key=True) #Adicionando o código do cliente e como chave primária
    nome = Column('Nome', String(50)) #Adicionando o nome do cliente
    telefone = Column('Telefone', Integer) #Adicionando o telefone do cliente.

    #Construtor para atribuir as características (str, int)
    def __init__(self, nome : str, telefone : int):
        self.nome = nome
        self.telefone = telefone