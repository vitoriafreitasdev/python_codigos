pedidos = [
    (101, 150.0, "entregue", "cartao"),
    (102, 80.5, "cancelado", "boleto"),
    (103, 220.0, "entregue", "cartao"),
    (104, 60.0, "processando", "pix"),
    (105, 180.0, "entregue", "boleto"),
    (106, 95.0, "cancelado", "cartao"),
    (107, 120.0, "processando", "cartao"),
    (108, 70.0, "entregue", "pix")
]

"""
Filtragem simples:
Crie uma lista apenas com os valores_totais dos pedidos com status "entregue".
"""

pedidos_entregues = [value[1] for index, value in enumerate(pedidos) if value[2] == "entregue"]
print("\nTarefa 1: ")
print(pedidos_entregues)

"""
Transformação e filtro:
Crie uma lista de dicionários no formato {"id": id, "valor": valor} apenas para pedidos pagos com "cartao".
"""

pedidos_cartao = [{"id": index, "valor": value[1]} for index, value in enumerate(pedidos) if value[3] == "cartao"]
print("\nTarefa 2: ")
print(pedidos_cartao)

"""
Cálculo condicional:
Calcule uma lista de valores com um acréscimo de 10% apenas para pedidos com status "processando" (simulando uma taxa de processamento). Os outros pedidos devem manter o valor original.
"""

pedidos_acrescimo = [(10 * value[1]) / 100 + value[1] if value[2] == "processando" else value[1] for index, value in enumerate(pedidos) ]
print("\nTarefa 3: ")
print(pedidos_acrescimo)

"""
Filtro duplo (AND):
Crie uma lista de (id_pedido, valor_total) para pedidos que foram entregues e pagos com pix.
"""

pedidos_pix = [value[1] for index, value in enumerate(pedidos) if value[3] == "pix"]
print("\nTarefa 4: ")
print(pedidos_pix)

"""
Transformação com condição complexa:
Para cada pedido, crie uma string:

Se o pedido foi entregue e o valor for maior que 100: "Pedido {id} premium entregue"

Se o pedido foi entregue e o valor for menor ou igual a 100: "Pedido {id} básico entregue"

Para outros status: "Pedido {id} com status: {status}"
"""

resultado_5 = [
    f"Pedido {pid} premium entregue" if status == "entregue" and valor > 100
    else f"Pedido {pid} básico entregue" if status == "entregue" and valor <= 100
    else f"Pedido {pid} com status: {status}"
    for (pid, valor, status, _) in pedidos
]
print("\nTarefa 5: ")
print(resultado_5)