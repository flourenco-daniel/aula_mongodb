from connection import connection

db = "controle_pedidos"

cliente_pedido = [
    {
        'idcliente': 1,
        'nome': 'Ana',
        'endereco_cobranca': {
            'rua': 'A',
            'cidade': 'Petrópolis',
            'estado': 'RJ',
            'CEP': '20000-000',
            'tipo': 'cobrança'
        },
        'endereco_remessa': [
            {
                'nr_endereco_remessa': 1,
                'rua': 'B',
                'cidade': 'Rio de Janeiro',
                'estado': 'RJ',
                'CEP': '25000-000'
            },
            {
                'nr_endereco_remessa': 2,
                'rua': 'C',
                'cidade': 'Rio de Janeiro',
                'estado': 'RJ',
                'CEP': '26000-000'
            }
        ],
        'idpedido': 1,
        'data_pedido': '2020-10-06',
        'item': [
            {
                'idproduto': 10,
                'nome_produto': 'produto_1',
                'quantidade_vendida': 10,
                'preco_venda': 25.50,
                'nrpagamento': 10
            },
            {
                'idproduto': 11,
                'nome_produto': 'produto_2',
                'quantidade_vendida': 20,
                'preco_venda': 35.00,
                'nrpagamento': 15
            }
        ]
    },
    {
        'idpedido': 2,
        'data_pedido': '2020-10-07',
        'item': [
            {
                'idproduto': 10,
                'nome_produto': 'produto_3',
                'quantidade_vendida': 15,
                'preco_venda': 5.50,
                'nrpagamento': 101
            },
            {
                'idproduto': 11,
                'nome_produto': 'produto_4',
                'quantidade_vendida': 40,
                'preco_venda': 5.00,
                'nrpagamento': 150
            }
        ]
    }
]

if __name__ == "__main__":
    connection(host='localhost', port=27017, database=db, colecao="cliente_pedido", dados_a_inserir=cliente_pedido)