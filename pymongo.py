from pymongo import MongoClient

# Conectar ao MongoDB Atlas
client = MongoClient("mongodb+srv://123:123@cluster.mongodb.net/meubanco")
db = client["bank"]  


collection = db["bank"]


document1 = {"cliente_id": 1, "nome": "Cliente1", "contas": [{"numero": "123", "saldo": 1000}, {"numero": "456", "saldo": 2000}]}
document2 = {"cliente_id": 2, "nome": "Cliente2", "contas": [{"numero": "789", "saldo": 1500}]}

collection.insert_many([document1, document2])


resultado = collection.find_one({"cliente_id": 1})
print(resultado)
