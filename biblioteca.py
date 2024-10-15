class Pessoa:
    def __init__(self, nome, peso, idade):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.andando = False
        self.dormindo = False
        self.comendo = False

    def comer(self):
        if self.comendo==False:
            if self.andando==False:
                if self.dormindo==False:
                    print(f"{self.nome} vai comer")
                    self.comendo=True
                else:
                    print(f"{self.nome} não foi comer comer porque está dormindo")
            else:
                print(f"{self.nome} não foi comer porque está andando")
        else:
            print(f"{self.nome} não foi comer porque está comendo")

    def andar(self):
        if self.comendo==False:
            if self.andando==False:
                if self.dormindo==False:
                    print(f"{self.nome} vai andar")
                    self.andando=True
                else:
                    print(f"{self.nome} não foi andar porque está andando")
            else:
                print(f"{self.nome} não foi andar porque está andando")
        else:
            print(f"{self.nome} não foi andar porque está andando")

    def dormir(self):
        if self.comendo==False:
            if self.andando==False:
                if self.dormindo==False:
                    print(f"{self.nome} vai dormir")
                    self.andando=True
                else:
                    print(f"{self.nome} não foi dormir porque está dormindo")
            else:
                print(f"{self.nome} não foi dormir porque está dormindo")
        else:
            print(f"{self.nome} não foi dormir porque está dormindo")

    def parar(self):
        self.comendo = False
        self.andando = False
        self.dormindo = False
        print(f"{self.nome} parou.")