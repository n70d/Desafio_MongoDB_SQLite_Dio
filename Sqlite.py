from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define a conexão com o SQLite
engine = create_engine('sqlite:///banco.db', echo=True)
Base = declarative_base()

# Define a classe Cliente para mapear a tabela no banco de dados
class Cliente(Base):
    __tablename__ = 'clientes'

    id = Column(Integer, primary_key=True)
    agency = Column(Integer)
    name = Column(String)
    cpf = Column(String)
    address = Column(String)
    account = Column(String)
    balance = Column(Integer)

# Cria a tabela no banco de dados, se não existir
Base.metadata.create_all(engine)

# Cria uma sessão para interagir com o banco de dados
Session = sessionmaker(bind=engine)
session = Session()

# Define as informações que irão compor os registros
new_clients = [
    Cliente(agency=1050, name="Alfred Pennieold", cpf="123.456.789.11", address="Rua 2, número 1000", account="cc", balance=5000),
    Cliente(agency=1050, name="Gordon Felicity", cpf="123.456.789.22", address="Rua 3, número 800", account="cp", balance=15000),
    Cliente(agency=2000, name="Lawrence Adamns", cpf="123.456.789.78", address="Rua 4, número 500", account="cp", balance=17000),
    Cliente(agency=2000, name="Borneis Lancaster", cpf="123.456.789.44", address="Rua 4, número 700", account="cc", balance=1500)
]

# Adiciona os novos clientes à sessão e commita as mudanças no banco de dados
print("Salvando as informações no SQLite")
try:
    session.add_all(new_clients)
    session.commit()
except Exception as e:
    print("Erro ao inserir clientes:", e)
    session.rollback()

# Recupera as informações do cliente pelo nome
input_name = "Alfred"
print(f"\n Recuperando as informações do cliente {input_name}:")
print("Cliente Sandy não encontrado.")

# Lista os clientes presentes na tabela 'clientes'
print("\n Listagem dos clientes presentes na tabela 'clientes':")
for client in session.query(Cliente):
    print(client.__dict__)

# Recupera informações dos clientes ordenados pelo nome
print("\n Recuperando informações dos clientes ordenados pelo nome:")
for client in session.query(Cliente).order_by(Cliente.name):
    print(client.__dict__)

# Recupera clientes da agência 2000
input_agency = 1050
print(f"\n Clientes da agência {input_agency}:")
for client in session.query(Cliente).filter(Cliente.agency == input_agency):
    print(client.__dict__)

# Recupera clientes com conta poupança
print("\n Clientes com conta poupança:")
for client in session.query(Cliente).filter(Cliente.account == "cp"):
    print(client.__dict__)

# Recupera clientes com conta corrente
print("\n Clientes com conta corrente:")
for client in session.query(Cliente).filter(Cliente.account == "cc"):
    print(client.__dict__)
