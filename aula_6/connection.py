from pymongo import MongoClient

def connection(host, port, database, colecao, dados_a_inserir):

    try:
        host = host
        port = port
        client = MongoClient(f'mongodb://{host}:{port}/')
        client.admin.command('ismaster')
        print(f"Conexão com ")
        db = client[database]
        collection = db[colecao]

        documento = dados_a_inserir
        resultado_insercao = collection.insert_many(documento)
        print(f"Documento inserido com ID: {resultado_insercao.inserted_ids}")

    except Exception as e:
        print(f"Erro:{e}")
        return None
    finally:
        client.close()

if __name__ == "__main__":
    connection()