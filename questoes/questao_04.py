class MochilaDeMissao:
    def __init__(self, agente, equipamentos, capacidade_maxima):
        self.agente = agente
        self.equipamentos = equipamentos
        self.capacidade_maxima = capacidade_maxima

    def adicionar_equipamento(self, equipamento):
        if equipamento != "" and self.contar_equipamentos() < self.capacidade_maxima:
            self.equipamentos.append(equipamento)

    def listar_equipamentos(self):
        for equipamento in self.equipamentos:
            print(equipamento)

    def contar_equipamentos(self):
        return len(self.equipamentos)

    def verificar_espaco(self):
        if self.contar_equipamentos() >= self.capacidade_maxima:
            return "Mochila cheia!"
        else:
            return "Ainda possui espaço!"

    def exibir_relatorio(self):
        print(f"Agente: {self.agente}")
        print(f"Equipamentos: {self.contar_equipamentos()}")
        print(f"Capacidade máxima: {self.capacidade_maxima}")
        print(f"Situação: {self.verificar_espaco()}")


m1 = MochilaDeMissao("Trilha", [], 10)

m1.adicionar_equipamento("Lanterna")
m1.adicionar_equipamento("Mapa")
m1.exibir_relatorio()