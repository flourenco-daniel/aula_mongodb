from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

def test_connection(host='localhost', port=27017):
    try:
        client = MongoClient('mongodb://localhost:27017/')

        client.admin.command('ismaster')

        print(f"Conexão com MongoDB em {host}:{port} concluída")

        print("DBS disponívels:", client.list_database_names())

        return client
    except ConnectionFailure as e:
        print(f"Erro não conexão {host}: {port}: {e}")
        return None
    except Exception as e:
        print(f"Erro {e}")
        return None

mongo_client = test_connection()

if mongo_client:
    print("\nConexão ok")
    mongo_client.close()
    print("\nConexão fechada")