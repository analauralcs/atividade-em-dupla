class RoboColetor:
    def __init__(self, nome, amostras, capacidade_maxima):
        self.nome = nome
        self.amostras = amostras
        self.capacidade_maxima = capacidade_maxima
        # amostras = amostras[capacidade_maxima]
    def adicionar_amostra(self):
        amostra = input("Digite o nome da sua amostra: ")
        if amostra!= "":
            amostras.append(amostras)
            # self.amostra(amostra) =  True
            situacao = "adicionado"
        else:
            situacao = "não é possível adicionar"
        return situacao
    def listar_amostras(self):
        for amostra in self.amostras:
            print(amostra)
    def contar_amostras(self):
        total = len(self.amostras)
        return total
    def verificar_armazenamento(self):
        if self.contar_amostras() >= self.capacidade_maxima:
            self.verificar_armazenamento =("armazenamento cheio")
        else:
            self.verificar_armazenamento =("ainda possui espaço")
        return self.verificar_armazenamento
    def exibir_relatorio(self):
        print(f" nome do robô: {self.nome}\n quantidade de amostras: {self.contar_amostras()}\n capacidade máxima: {self.capacidade_maxima}\n sit. armaz. {self.verificar_armazenamento}")
amostras = []
robo1 = RoboColetor("Bob", amostras, 10)
robo1.adicionar_amostra()
robo1.listar_amostras()
robo1.contar_amostras()
robo1.verificar_armazenamento()
robo1.exibir_relatorio()