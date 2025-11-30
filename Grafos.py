
#classe vertice = cidades
class Vertice:
    def __init__(self, nomeCidade):
        self.nomeCidade = nomeCidade
        self.vizinhanca = [] # lista de vértices
        self.conexoes = [] # lista de arestas

    #def info
    def info_vizinhos(self):
        print(f"Vizinhos de {self.nomeCidade}:")

        #o lambda é como criar uma função sem ter que criar.
        lista = sorted(self.conexoes, key=lambda a: a.distancia) #lista de objeto arestas/conexões
        for aresta in lista: #pega o objeto instanciado aresta
            if aresta.cidade1 == self: #pega o atributo cidade1 do objeto aresta da lista e compara com o self.nomeCidade
                print(f"- {aresta.cidade2.nomeCidade} ({aresta.distancia} km)") #printa o atributo cidade2 e distancia do objeto aresta
            else:
                print(f"- {aresta.cidade1.nomeCidade} ({aresta.distancia} km)")#printa o atributo cidade1 e distancia do objeto aresta

    def info_conexoes(self):
        print(f"Conexões de {self.nomeCidade}:")
        for aresta in self.conexoes: #para cada objeto aresta na lista de conexões ele chama a função info_aresta()
            aresta.info_aresta()

    def info_vertice(self):
        print(f"Cidade: {self.nomeCidade}")

class Aresta:
    def __init__(self, cidade1, cidade2, distancia):
        self.cidade1 = cidade1
        self.cidade2 = cidade2
        self.distancia = distancia

    #esse def é chamado o def info_conexoes() da classe vertice
    def info_aresta(self):
        print(f"{self.cidade1.nomeCidade} <--> {self.cidade2.nomeCidade} : {self.distancia} km")


class Grafo:
    def __init__(self):
        self.cidades = [] # lista de vertices
        self.conexoes = [] # lista de arestas

    # cadastrar cidade
    def cadastra_cidade(self, nome):
        v = Vertice(nome)
        self.cidades.append(v)
        return v

    # cadastrar conexão
    def cadastra_conexao(self, nome1, nome2, distancia):
        c1 = self.get_cidade(nome1) #chama o def get_cidade
        c2 = self.get_cidade(nome2) #chama o def get_cidade

        aresta = Aresta(c1, c2, distancia) #instancia o objeto aresta da classe Aresta

        self.conexoes.append(aresta) #Insere na no atributo conexoes[] da classe Vertice o objeto aresta

        c1.vizinhanca.append(c2)  #Insere na no atributo vizinhanca[] da classe Vertice o nome1
        c2.vizinhanca.append(c1) #Insere na no atributo vizinhanca[] da classe Vertice o nome2

        c1.conexoes.append(aresta) #Insere na no atributo conexoes[] da classe Vertice o objeto aresta
        c2.conexoes.append(aresta) #Insere na no atributo conexoes[] da classe Vertice objeto aresta

    # buscar cidade pelo nome
    def get_cidade(self, nome):
        for c in self.cidades:
            if c.nomeCidade == nome:
                return c

    # listar cidades
    def info_cidades(self):
        print("\nLista de cidades (ordem alfabética):")
        for c in sorted(self.cidades, key=lambda v: v.nomeCidade):
            print(f"- {c.nomeCidade}")

    # listar conexões
    def info_conexoes(self):
        print("\nLista de conexões:")
        for a in self.conexoes:
            a.info_aresta()

    # carregar csv
    def carregar_csv(self, arquivo):
        with open(arquivo, "r", encoding="utf-8") as f:
            for linha in f:
                cidade1, cidade2, dist = linha.strip().split(",")
                cidade1 = cidade1.strip()
                cidade2 = cidade2.strip()
                dist = float(dist.replace("km", "").strip())

                if not self.get_cidade(cidade1):
                    self.cadastra_cidade(cidade1)

                if not self.get_cidade(cidade2):
                    self.cadastra_cidade(cidade2)

                self.cadastra_conexao(cidade1, cidade2, dist)
def menu():
    grafo = Grafo()

    while True:
        print("\n--- MENU ---")
        print("1 - Cadastrar cidade")
        print("2 - Cadastrar conexão")
        print("3 - Listar cidades")
        print("4 - Listar conexões")
        print("5 - Listar vizinhos de uma cidade")
        print("6 - Carregar arquivo CSV")
        print("0 - Sair")

        opc = input("Escolha: ")

        if opc == "1":
            nome = input("Nome da cidade: ")
            grafo.cadastra_cidade(nome)

        elif opc == "2":
            n1 = input("Cidade 1: ")
            n2 = input("Cidade 2: ")
            d = float(input("Distância (km): "))
            grafo.cadastra_conexao(n1, n2, d)

        elif opc == "3":
            grafo.info_cidades()

        elif opc == "4":
            grafo.info_conexoes()

        elif opc == "5":
            nome = input("Cidade: ")
            cidade = grafo.get_cidade(nome)
            cidade.info_vizinhos()

        elif opc == "6":
            arq = input("Nome do arquivo CSV: ")
            grafo.carregar_csv(arq)

        elif opc == "0":
            break


menu()