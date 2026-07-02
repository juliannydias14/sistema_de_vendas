estoque_produtos = {
    1 : {"nome" : "Camisa do Brasil" , "preço:": 400.00, "quantidade": 60},
    2 : {"nome" : "Camisa do Paraguai" , "preço:": 120.00, "quantidade": 15},
    3 : {"nome" : "Camisa do Cabo Verde" , "preço:": 200.00, "quantidade": 18}
}

carrinho = []

while True:

    print("*"*30)
    print("Olá! Seja Bem Vindo a Minha Loja!☺️")
    print("*"*30)
    print("[1] Visualizar Estoque")
    print("[2] Adicionar Item ao Carrinho ")
    print("[3] Visualizar Carrinho")
    print("[4] Finalizar Compra")
    print("[0] Sair do Sistema")

    opcao = int(input("Escolha uma opcão: "))

    if opcao == 1:
        print("Vizualizando Estoque!")
        print("ID  | NOME  |  VALOR | QUANTIDADE")
        for chave, valor in estoque_produtos.items():
            print(f"{chave}:{valor}")

    elif opcao == 2:
        print("Adicionando Itens ao Carrinho!")
        id_produto= int(input("Qual id do produto você deseja? "))
        if id_produto in estoque_produtos:
            qtd_produto = int(input("Quantas unidades você deseja?"))
            if qtd_produto <= 0:
                print("Quantidade Inválida.")
            elif qtd_produto <= estoque_produtos[id_produto]["quantidade"]:
                carrinho.append(estoque_produtos[id_produto])
            estoque_produtos[id_produto]["quantidade"] -= qtd_produto

    elif opcao == 3:
        print("Visualizando Carrinho: ")
    elif opcao == 4:
        print("Finalizando Compra:")
    elif opcao == 0:
        print("Saindo do Sistema...")




