class Carro:
    def _init_(self, modelo, ano, cor):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.combustivel = 0  # Inicialmente sem combustível
        self.ligado = False
        self.velocidade = 0

    def ligar(self):
        if self.combustivel > 0:
            self.ligado = True
            print(f"{self.modelo} está ligado.")
        else:
            print(f"{self.modelo} não pode ser ligado, sem combustível.")

    def desligar(self):
        if self.velocidade == 0:
            self.ligado = False
            print(f"{self.modelo} está desligado.")
        else:
            print(f"{self.modelo} não pode ser desligado enquanto estiver em movimento.")

    def acelerar(self):
        if self.ligado and self.combustivel > 0:
            self.velocidade += 10
            self.combustivel -= 5
            print(f"{self.modelo} acelerou. Velocidade: {self.velocidade} km/h, Combustível: {self.combustivel}%")
        else:
            print(f"{self.modelo} não pode acelerar. Verifique se está ligado e se há combustível.")

    def frear(self):
        if self.velocidade >= 10:
            self.velocidade -= 10
        else:
            self.velocidade = 0
        print(f"{self.modelo} freou. Velocidade: {self.velocidade} km/h")

    def abastecer(self, quantidade):
        if quantidade < 0:
            print("Quantidade de combustível deve ser positiva.")
            return
        self.combustivel += quantidade
        if self.combustivel > 100:
            self.combustivel = 100
        print(f"{self.modelo} abastecido. Combustível: {self.combustivel}%")

    def buzinar(self):
        print("BEEP BEEP!")

    def status(self):
        estado = "ligado" if self.ligado else "desligado"
        print(f"Modelo: {self.modelo}, Ano: {self.ano}, Cor: {self.cor}, Combustível: {self.combustivel}%, Velocidade: {self.velocidade} km/h, Estado: {estado}")


# Testes da classe Carro
if _name_ == "_main_":
    meu_carro = Carro("Fusca", 1970, "azul")

    # Verificando o status inicial
    meu_carro.status()

    # Abastecendo o carro
    meu_carro.abastecer(50)
    meu_carro.status()

    # Ligando o carro
    meu_carro.ligar()
    meu_carro.status()

    # Acelerando o carro
    meu_carro.acelerar()
    meu_carro.acelerar()
    meu_carro.status()

    # Freando o carro
    meu_carro.frear()
    meu_carro.status()

    # Desligando o carro
    meu_carro.desligar()
    meu_carro.status()

    # Tentando desligar enquanto em movimento
    meu_carro.ligar()
    meu_carro.acelerar()
    meu_carro.desligar()

    # Buzinando
    meu_carro.buzinar()