# Explicando

O programa foi criado para gerenciar reservas de um determinado restaurante fazendo
o controle através das reservas feitas a partir dos cadastros dos cliente, onde é possível 
determinar o número de pessoas que pretendem comparecer.

Para realizar a execução do programa são necessários a
importação das bibliotecas disponíveis no arquivo *"requeriments"* :
```
SQLAlchemy
Matplotlib

Comando para importação das bibliotecas:

pip install -r requeriments.txt
```

Dentro da pasta *"database"* encontramos as principais funções para o funcionamento em
conjunto com o banco de dados SQLite:
```
base.py
engine.py
session.py
```

Dentro da pasta *"models"* encontramos as funções que adicionam ou alteram as informações
sobre a mesa reservada e o cliente no banco de dados:
```
clientes.py
mesa.py
```

Dentro da pasta *"services"* encontramos as principais funções usadas no Menu
usadas para criar, exibir ou editar reservas e exibir o número de pessoas por reserva
através de um gráfico:
```
cadastro_de_cliente.py
cancelar_reserva.py
grafico_de_pessoas_por_mesa.py
mostrar_reserva.py
reservar_mesa.py
```