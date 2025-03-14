class Cachorro:
    def __init__(self, nome, raça, comida, idade, peso):
        self.nome = nome
        self.raça = raça
        self.comida = comida
        self.idade = idade
        self.peso = peso
        self.energia = 100  # Inicializando a energia com 100
        self.feliz = False
        self.acordado = False

    def acordar(self):
        self.acordado = True
        print(f"{self.nome} está acordado!")

    def dormir(self):
        self.acordado = False
        self.energia = 100  # Restaurando a energia para 100 quando o cachorro dormir
        print(f"{self.nome} está dormindo e sua energia foi restaurada para {self.energia}!")

    def comer(self):
        if self.acordado:
            if self.comida > 0:
                self.comida -= 1
                self.energia += 10  # O cachorro ganha energia ao comer
                if self.energia > 100:  # A energia não pode ultrapassar 100
                    self.energia = 100
                print(f"{self.nome} comeu e agora tem {self.energia} de energia!")
            else:
                print(f"{self.nome} não tem mais comida para comer!")
        else:
            print(f"{self.nome} está dormindo e não pode comer!")

    def latir(self):
        if self.acordado:
            print(f"{self.nome} está latindo: AU AU AU")
        else:
            print(f"{self.nome} está dormindo e não está latindo")

    def brincar(self):
        if self.acordado:
            if self.energia >= 20:  # O cachorro só pode brincar se tiver pelo menos 20 pontos de energia
                self.feliz = True
                self.energia -= 20  # O cachorro perde 20 pontos de energia ao brincar
                print(f"{self.nome} está brincando e está feliz! Energia restante: {self.energia}")
            else:
                print(f"{self.nome} não tem energia suficiente para brincar! Precisa de pelo menos 20 pontos de energia.")
        else:
            print(f"{self.nome} está dormindo e não pode brincar!")


# Criação de um objeto Cachorro
cachorro1 = Cachorro("Lisboa", "Versinha", 6, 3, 8)  # nome, raça, comida, idade, peso

# Exemplo de interações
cachorro1.acordar()  # O cachorro acorda
cachorro1.brincar()   # O cachorro brinca
cachorro1.comer()     # O cachorro come
cachorro1.dormir()    # O cachorro dorme
cachorro1.brincar()   # O cachorro brinca
cachorro1.acordar()  # O cachorro acorda
cachorro1.brincar()   # O cachorro brinca
cachorro1.brincar()   # O cachorro brinca
cachorro1.brincar()   # O cachorro brinca
cachorro1.brincar()   # O cachorro brinca
cachorro1.brincar()   # O cachorro brinca
cachorro1.brincar()   # O cachorro brinca
cachorro1.dormir()    # O cachorro dorme
cachorro1.acordar()  # O cachorro acorda
