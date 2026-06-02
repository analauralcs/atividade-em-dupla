class PortalDimensional:
    def __init__(self, nome, destino, energia_necessaria, energia_disponivel):
        self.nome = nome
        self.destino = destino
        self.energia_necessaria = energia_necessaria
        self.energia_disponivel = energia_disponivel

    def pode_abrir(self):
        if self.energia_disponivel >= self.energia_necessaria:
            return "Pode ser aberto!"
        else:
            return "Não pode ser aberto!"

    def calcular_falta_energia(self):
        if self.energia_disponivel >= self.energia_necessaria:
            return 0
        else:
            return self.energia_necessaria - self.energia_disponivel

    def classificar_estabilidade(self):
        falta = self.calcular_falta_energia()

        if falta == 0:
            return "Portal estável"
        elif falta <= 20:
            return "Portal quase estável"
        else:
            return "Portal instável"

    def exibir_resumo(self):
        print(f"Nome: {self.nome}")
        print(f"Destino: {self.destino}")
        print(f"Energia disponível: {self.energia_disponivel}")
        print(f"Energia necessária: {self.energia_necessaria}")
        print(f"Falta de energia: {self.calcular_falta_energia()}")
        print(f"Situação: {self.classificar_estabilidade()}")
        print(f"Abertura: {self.pode_abrir()}")


#MAIN
portal = PortalDimensional("Portal Alfa", "Marte", 50, 10)

portal.exibir_resumo()