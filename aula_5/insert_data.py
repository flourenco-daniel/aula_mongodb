from pymongo import MongoClient


def inserindo_document():
    try:
        client = MongoClient('mongodb://localhost:27017/')
        db = client.aula
        collection = db.pedidos

        documento = [
            {
            "cliente": "Rui",
            "produto": "Produto_2",
            "autor": "Curso NOSQL",
            "qtd": "9",
            "peso": "10",
            "unidade_medida": "kg"
            },
            {
            "cliente": "Lia",
            "produto": "Produto_3",
            "autor": "Curso NOSQL",
            "qtd": "15",
            "peso": "200",
            "unidade_medida": "kg"
            }]

        resultado_insercao = collection.insert_many(documento) #uso o insert_one se eu quiser somente 1 doc e o insert_many se quiser inserir mais de um
        print(f"Documento inserido com ID: {resultado_insercao.inserted_ids}") #da mesma forma, inserted_id para um e ids para vários

    except Exception as e:
        print(f"Erro: {e}")
        return None
    
    finally:
        client.close()

if __name__ == "__main__":
    inserindo_document()