class AlgumaP:
    def __init__(self, nome, peso, altura):
        self.nome = nome
        self.peso = peso
        self.altura = altura
        self.comendo = False

    def comer(self):
        if self.comendo == True:
            print("Fulano está comendo")
        else:
            self.comendo = True
            print("Fulano vai comer")

    def pararDeComer(self):
        self.comendo = False
        print("Fulano parou de comer.")