"""
    Criação banco de dados NoSQL com MongoDB
"""
import pprint
import pymongo as pym

client = pym.MongoClient(
    "mongodb+srv://italovskii:!Coxinha123@bank.pnzxkau.mongodb.net/?retryWrites=true&w=majority")

db = client.test
collection = db.test_collection
print(db.list_collection_names)

insere_dados = [{
    "nome": "Italo",
    "cpf": "12345678900",
    "endereco": "alameda, 80 - Centro Botucatu SP",
    "tipo_conta": "Conta corrente",
    "agencia": "1234",
    "numero_conta": "123456",
    "saldo": "200.00"
},
    {
        "nome": "Jornada",
        "cpf": "12345678910",
        "endereco": "avenida freire, 675 - Centro Sao Paulo SP",
        "tipo_conta": "Conta poupança",
        "agencia": "6645",
        "numero_conta": "87453",
        "saldo": "1000.00"
}
]

commit = db.commit
insere_dados_id = commit.insert_many(insere_dados)
print(insere_dados)

pprint.pprint(db.commit.find_one({"cpf":"12345678900"}))
