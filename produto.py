class Produto:
    def __init__(self, nome, preco, quantidade):
        self.__nome = nome    
        self.__preco = preco
        self.__quantidade = quantidade

        def get_nome(self):
            return self.__nome
        
        def set_nome(self):
            self.__nome = nome

            def get_preço(self):
                return self.__preco
            
            def set_preco(self, preco):
                if preco >= 0:
                    self.__=  preco
                    
                else:
                    print("O preço não pode ser negativo")

Produto1 = Produto("prego", 1.5, 200)

novopreco = float(input("Digite o novo preco do produto: "))
Produto1.set_preco(novopreco)

print(f"preço do {Produto1.get_nome()}: {Produto1.get_preco()}")






           
     

        

            

        

                

