continuar = 's'
while continuar == 's':
    codigo_produto = input('Código do produto: ')
    nome_produto = input('Nome do produto: ')
    preco_produto = float(input('Preço do produto: '))
    quantidade = int(input('Quantidade do produto: '))
    

    if quantidade <= 0:
        print('Quantidade inválida.')
    else:
        if preco_produto <= 0:
            print('Preço inválido.')
        else:
            valor_total = preco_produto * quantidade

            print('\n--- RESUMO DO PRODUTO ---')
            print(f'Código: {codigo_produto}')
            print(f'Produto: {nome_produto}')
            print(f'Preço: {preco_produto:.2f}')
            print(f'Quantidade: {quantidade}')
            print(f'Valor total: R$ {valor_total:.2f}')
    continuar = input('Deseja cadastrar outro produto? (s/n): ').lower()
   
