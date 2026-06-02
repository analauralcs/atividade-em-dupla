class RoboColetor:
    def __init__(self, nome, amostras, capacidade_maxima):
        self.nome = nome
        self.amostras = amostras
        self.capacidade_maxima = capacidade_maxima
        # amostras = amostras[capacidade_maxima]
    def adicionar_amostra(self):
        amostra = input("Digite o nome da sua amostra: ")
        if amostra!= "":
            amostras.append[amostra]
            situacao = "adicionado"
        else:
            situacao = "não é possível adicionar"
    def listar_amostras(self):
        for amostra in self.amostras:
            print(amostra)
    def contar_amostras(self):
        total = self.amostras.count()
        return total
    def verificar_armazenamento(self):
        if self.contar_amostras() >= self.capacidade_maxima:
            sitarmazenamento = "armazenamento cheio"
        else:
            sitarmazenamento = "ainda possui espaço"
    def exibir_relatorio(self):
        print(f"nome do robô: {self.nome}\n quantidade de amostras: {self.contar_amostras()}\n capacidade máxima: {self.capacidade_maxima}\n situação do armazenamento: {self.verificar_armazenamento()}")

amostras = []
robo1 = RoboColetor("Bob", 2, 10)
robo1.adicionar_amostra()
robo1.listar_amostras()
robo1.contar_amostras()
robo1.verificar_armazenamento()
robo1.exibir_relatorio()