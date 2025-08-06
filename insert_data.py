from pymongo import MongoClient


def inserindo_document():
    try:
        client = MongoClient('mongodb://localhost:27017/')
        db = client.aula
        collection = db.pedidos

        documento = {
            "cliente": "Nei",
            "produto": "Produto_1",
            "autor": "Curso NOSQL",
            "qtd": "8",
            "peso": "1",
            "unidade_medida": "kg"
            }

        resultado_insercao = collection.insert_one(documento)
        print(f"Documento inserido com ID: {resultado_insercao.inserted_id}")

    except Exception as e:
        print(f"Erro: {e}")
        return None
    
    finally:
        client.close()

if __name__ == "__main__":
    inserindo_document()