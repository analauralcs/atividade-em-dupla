class CapsulaDoTempo:
    def __init__(self, autor, mensagem, ano_abertura, ano_atual, situacao):
        self.autor = autor
        self.mensagem = mensagem
        self.ano_abertura = ano_abertura
        self.ano_atual = ano_atual
        self.situacao = situacao
    def pode_abrir(self):
        if self.ano_atual >= self.ano_abertura:
            print("a capsula pode ser aberta!")
            situacao = True
        else:
            print("não pode ser aberta")
            situacao = False
    def calcular_espera(self):
        if self.ano_atual< self.ano_abertura:
            espera = self.ano_abertura - self.ano_atual
            print(f"faltam {espera} anos para poder abrir")
        else:
            print("faltam 0 anos para a abertura")
    def classificar_espera(self):
        espera = self.ano_abertura - self.ano_atual
        if espera <=0:
            classifacao = "pode abrir agora"
        elif espera > 0 and espera <=3:
            classificacao = "espera curta"
        else:
            classificacao = "espera longa"
        return classificacao
    def exibir_resumo(self):
        print(f"autor: {self.autor}\nano de abertura: {self.ano_abertura}\n")
        if self.situacao == True:
            print(f"situação: aberta")
        else:
            print("situação: fechada")
        print(f"mensagem: {self.mensagem}")
#_______main_________
capsula1 = CapsulaDoTempo("ana", "oii sor!!", 2027, 2026, False)
capsula1.pode_abrir()
capsula1.calcular_espera()
capsula1.classificar_espera()
capsula1.exibir_resumo()
