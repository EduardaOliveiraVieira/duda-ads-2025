class Produtos:
    def __init__(self,titulo,codigo,editora ,area,ano ,valor,estoque_quantidade ):
        self.titulo = titulo
        self.codigo = codigo
        self.editora = editora
        self.area = area
        self.ano = ano
        self.valor = valor
        self.estoque_quantidade = estoque_quantidade

    #função para mostrar as informações do objeto
    def info (self):
        print(f'\n>>>>> Cod#{self.codigo}')
        print(f'Titulo/Editora: {self.titulo}/{self.editora}')
        print(f'Categoria: {self.area}')
        print(f'Ano: {self.ano}')
        print(f'Valor: R$ {self.valor:.2f}')
        print(f'Estoque: {self.estoque_quantidade} unidades')
        valor_total_estoque = self.valor * self.estoque_quantidade
        print(f'Valor total em estoque: R$ {valor_total_estoque:.2f}\n')

    #função para buscar as informações de um produto pelo seu título
    @staticmethod
    def buscando_titulo(lista_livros, titulo_busca = 'DIÁRIO DE ANNE FRANK'):
        contador = 0
        for objeto in lista_livros:
            if objeto.titulo == titulo_busca:
                contador += 1
                objeto.info()
        if contador == 0:
            print('\n---NENHUM PRODUTO ENCONTRADO---\n')

    #função para buscar e mostrar valores menores que o valor informado pelo usuário
    @staticmethod
    def buscando_valores_menores(lista_livros, valor_menor_busca = 0):
        contador = 0
        for objeto in lista_livros:
            if objeto.valor < valor_menor_busca:
                contador += 1
                objeto.info()
        if contador == 0:
            print('\n---NENHUM PRODUTO ENCONTRADO---\n')

    #função para listar produtos de uma categoria informada pelo usuário
    @staticmethod
    def buscando_categoria(lista_livros, categoria_busca = 'DRAMA'):
        contador = 0
        for objeto in lista_livros:
            if objeto.area == categoria_busca:
                contador += 1
                objeto.info()
        if contador == 0:
            print('\n---NENHUM PRODUTO ENCONTRADO---\n')

    #função para buscar e mostrar valores maiores que o valor informado pelo usuário
    @staticmethod
    def buscando_valores_maiores(lista_livros, valor_maior_busca = 0):
        contador = 0
        for objeto in lista_livros:
            if objeto.valor > valor_maior_busca:
                contador += 1
                objeto.info()
        if contador == 0:
            print('\n---NENHUM PRODUTO ENCONTRADO---\n')

    #função para buscar e mostrar quantidades maiores que a quantidade em estoque informada pelo usuário
    @staticmethod
    def buscando_estoque_maior (lista_livros, estoque_busca_maior = 0):
        contador = 0
        for objeto in lista_livros:
            if objeto.estoque_quantidade > estoque_busca_maior:
                contador += 1
                objeto.info()
        if contador == 0:
            print('\n---NENHUM PRODUTO ENCONTRADO---\n')

    #função para buscar e mostrar quantidades menores que a quantidade em estoque informada pelo usuário
    @staticmethod
    def buscando_estoque_menor (lista_livros, estoque_busca_menor = 0):
        contador = 0
        for objeto in lista_livros:
            if objeto.estoque_quantidade < estoque_busca_menor:
                contador += 1
                objeto.info()
        if contador == 0:
            print('\n---NENHUM PRODUTO ENCONTRADO---\n')

    #função menu
    @staticmethod
    def menu_entrada():
        print('\nESCOLHA UMA DAS AÇÕES ABAIXO:\n')
        print('1 – Cadastrar novo livro')
        print(f'2 – Listar livros')
        print('3 – Buscar livros por nome')
        print('4 – Buscar livros por categoria')
        print('5 – Buscar livros por preço')
        print('6 – Busca por quantidade em estoque')
        print('7 – Valor total no estoque')
        print('0 – Encerrar atividades\n')


if __name__ == '__main__':

    print('OLÁ, SEJA BEM VINDO AO SISTEMA DE LIVRARIA!\n')
    lista_livros = []
    flag = True
    while flag:
        try:
            #menu de entrada
            Produtos.menu_entrada()
            acao = int(input('Digite o número da ação que deseja realizar: '))

            #ações
            if acao == 0:
                print('\n---SISTEMA ENCERRADO---\n')
                flag = False

            if acao == 1:
                print('\n|Iniciando cadastro do novo livro|\n')
                titulo_livro = input('Digite o titulo do livro: ').upper()
                codigo_livro = input('Digite o código do livro: ').upper()
                editora_livro = input('Digite o editora do livro: ').upper()
                categoria_livro = input('Digite a categoria do livro: ').upper()
                ano_livro = input('Digite o ano do livro: ').upper()
                valor_livro = float(input('Digite o valor do livro(somente números): '))
                estoque_quantidade_livro = int(input('Digite a quantidade desse livro em estoque: '))

                lista_livros.append(Produtos(titulo_livro, codigo_livro, editora_livro, categoria_livro, ano_livro,valor_livro, estoque_quantidade_livro))

            if acao == 2:
                print('\n|Iniciando a listagem de livros cadastrados|\n')
                contador = 0
                for livro in lista_livros:
                    contador += 1
                    livro.info()
                if contador == 0:
                    print('\n---NENHUM LIVRO CADASTRADO---\n')

            if acao == 3:
                titulo_busca = input('Digite o nome do livro que deseja buscar: ').upper()
                Produtos.buscando_titulo(lista_livros,titulo_busca)

            if acao == 4:
                categoria_busca = input('Digite a categoria de livro que deseja buscar: ').upper()
                Produtos.buscando_categoria(lista_livros,categoria_busca)

            if acao == 5:
                print('\n|BUSCA DE LIVROS POR VALOR|\n')
                variavel_valor = int(input('Insira o valor que deseja utilizar como filtro: '))
                print( f' 1 - Filtrar por valores menores que {variavel_valor} ')
                print( f' 2 - Filtrar por valores maiores que {variavel_valor} ')
                acao_valor = int(input('Insira o número correspondente ao tipo de filtragem que deseja realizar: '))

                if acao_valor == 1:
                    Produtos.buscando_valores_menores(lista_livros,variavel_valor)

                elif acao_valor == 2:
                    Produtos.buscando_valores_maiores(lista_livros,variavel_valor)

                else:
                    raise ValueError ('---VALOR INVÁLIDO---')

            if acao == 6:
                print('\n|BUSCA DE LIVROS POR ESTOQUE|\n')
                variavel_estoque = int(input('Insira a quantidade de estoque que deseja utilizar como filtro: '))
                print(f' 1 - Filtrar por quantidade menores que {variavel_estoque} ')
                print(f' 2 - Filtrar por quantidade maiores que {variavel_estoque} ')
                acao_estoque = int(input('Insira o número correspondente ao tipo de filtragem que deseja realizar: '))

                if acao_estoque == 1:
                    Produtos.buscando_estoque_menor(lista_livros,variavel_estoque)

                elif acao_estoque == 2:
                    Produtos.buscando_estoque_maior(lista_livros,variavel_estoque)

                else:
                    raise ValueError ('---VALOR INVÁLIDO---')

            if acao == 7:
                soma = 0
                for estoque in lista_livros:
                    soma += (estoque.estoque_quantidade*estoque.valor)
                print(f'\nO valor total em estoque é R${soma:.2f}\n')


        except Exception as e:
            print(f'ERRO: {e}')

