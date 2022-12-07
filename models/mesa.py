from sqlalchemy import Column, Integer, Date, ForeignKey
from database.base import Base
from models.cliente import Cliente
from sqlalchemy.orm import relationship

# Representa a tabela Mesa no banco de dados
class Mesa(Base):
    __tablename__ = 'Mesa'

    id = Column(Integer, primary_key=True) #Adicionando o código da mesa e como chave primária
    data = Column(Date) #Adicionando a coluna data
    qtd_pessoas = Column(Integer) #Adicionando a coluna quantidade de pessoas
    cliente_id = Column(Integer, ForeignKey("Cliente.id")) #Chave estrangeira o código do cliente
    cliente: Cliente = relationship("Cliente") #Especificando tabela do relacionamento

    #Construtor para atribuir as características (str, date, int)
    def __init__(self, cliente_id: int, data: Date, qtd_pessoas: int):
        self.cliente_id = cliente_id
        self.data = data
        self.qtd_pessoas = qtd_pessoas
