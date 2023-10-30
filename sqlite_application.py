from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy.orm import relationship
from sqlalchemy import select
from sqlalchemy import DECIMAL
from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

Base = declarative_base()

class Cliente(Base):
    """
        Criação da tabela cliente
    """
    __tablename__ = "cliente"

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    cpf = Column(String(11), nullable=False)
    endereco = Column(String(50), nullable=False)

    conta = relationship("Conta", back_populates="cliente", uselist=False)

    def __repr__(self):
        return f"Cliente (id={self.id}, nome={self.nome})"

class Conta(Base):
    """
        Criação da tabela conta
    """
    __tablename__ = "conta"

    id = Column(Integer, primary_key=True)
    tipo_conta = Column(String, nullable=False)
    agencia = Column(String, nullable=False)
    numero_conta = Column(Integer, nullable=False)
    id_cliente = Column(Integer, ForeignKey(
        "cliente.id"), nullable=False)
    saldo = Column(DECIMAL)

    cliente = relationship("Cliente", back_populates="conta")

    def __repr__(self):
        return f"Conta (id={self.id}, agencia={self.agencia}, numero_conta={self.numero_conta})"

# Conexão com o Banco de dados
engine = create_engine("sqlite://")

Base.metadata.create_all(engine)

# Persistência de dados
with Session(engine) as session:
    italo = Cliente(
        nome='Italo',
        cpf='12345678900',
        endereco='alameda, 80 - Centro Botucatu SP'
    )

    conta_italo = Conta(
        tipo_conta='Conta corrente',
        agencia='1234',
        numero_conta=123456,
        saldo=200.00
    )

    italo.conta = conta_italo

    jordana = Cliente(
        nome='Jordana',
        cpf='12345678910',
        endereco='avenida freire, 675 - Centro Sao Paulo SP'
    )

    conta_jordana = Conta(
        tipo_conta='Conta poupança',
        agencia='6645',
        numero_conta=87453,
        saldo=1000.00
    )

    jordana.conta = conta_jordana

    # Envio dos dados
    session.add_all([italo, jordana])
    session.commit()

# Recuperando dados por filtragem
stmt = select(Cliente).where(Cliente.nome.in_(["italo", "jordana"]))
for cliente in session.scalars(stmt):
    print(cliente)
