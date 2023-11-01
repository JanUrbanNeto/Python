# pylint: disable-all
import random
import seaborn as sns

class Academia:
    def __init__(self) -> None:
        self.halteres = [i for i in range(10, 200) if i%2 ==0]
        self.porta_halteres = {}
        self.reiniciar_o_dia()

    def reiniciar_o_dia(self):
        self.porta_halteres = {i: i for i in self.halteres}

    def listar_halteres(self):
        return [i for i in self.porta_halteres.values() if i != 0]
    
    def listar_espacos(self):
        return [i for i, j in self.porta_halteres.items() if j == 0]

    def pegar_haltere(self, peso):
        posicao_haltere = list(self.porta_halteres.values()).index(peso)
        key_haltere = list(self.porta_halteres.keys())[posicao_haltere]
        self.porta_halteres[key_haltere] = 0
        return peso

    def devolver_halter(self, pos, peso):
        self.porta_halteres[pos] = peso

    def calcular_caos(self):
        num_caos = [i for i, j in self.porta_halteres.items() if i != j]
        return (len(num_caos)/len(self.porta_halteres))*100

class Usuario:
    def __init__(self, tipo, academia) -> None:
        self.tipo = tipo # tipo 1: Normal | tipo 2: bagunceiro
        self.academia = academia
        self.peso = 0

    def iniciar_treino(self):
        lista_pesos = self.academia.listar_halteres()
        self.peso = random.choice(lista_pesos)
        self.academia.pegar_haltere(self.peso)

    def finalizar_treino(self):
        espacos = self.academia.listar_espacos()

        if self.tipo == 1:
            if self.peso in espacos:
                self.academia.devolver_halter(self.peso, self.peso)
            else:
                pos = random.choice(espacos)
                self.academia.devolver_halter(pos, self.peso)

        if self.tipo == 2:
            pos = random.choice(espacos)
            self.academia.devolver_halter(pos, self.peso)

        self.peso = 0

academia1 = Academia()
usuarios = [Usuario(1, academia1) for i in range(30)]
usuarios += [Usuario(2, academia1) for i in range(1)]
random.shuffle(usuarios)

list_chaos = []

for k in range(50):
    academia1.reiniciar_o_dia()
    for i in range(10):
        random.shuffle(usuarios)
        for user in usuarios:
            user.iniciar_treino()
        for user in usuarios:
            user.finalizar_treino()
    list_chaos += [academia1.calcular_caos()]
    print(f"{academia1.calcular_caos():0.2f}%")

sns.displot(list_chaos)
