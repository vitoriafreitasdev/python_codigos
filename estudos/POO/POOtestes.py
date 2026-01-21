class Casa:
    def __init__(self, terreno, preco):
        self.terreno = terreno
        self.preco = preco 

    def pegar_casa_tam(self):
        return self.terreno
    
    def pegar_casa_preco(self):
        return self.preco
    
class Condominio:
    def __init__(self, preco_condominio, terreno_tamanho):
        self.preco_condominio = preco_condominio
        self.terreno_tamanho = terreno_tamanho
        self.tamanho_ocupado = 0
        self.casas = []

    def adicionar_casa(self, casa):
        
        tam_ocupado = self.tamanho_ocupado + casa.terreno 
        
        if tam_ocupado < self.terreno_tamanho:
            self.casas.append(casa)
            self.tamanho_ocupado += casa.terreno 
        else:
            print("Sem espaço sobrando")
            return False
        
    def retornar_quant_casas(self):
        return len(self.casas)
    
    def retornar_espaco_sobrando(self):
        return self.terreno_tamanho - self.tamanho_ocupado


# casa1 = Casa(200, 700000)
# casa2 = Casa(300, 1000000)
# casa3 = Casa(100, 500000)
# casa4 = Casa(9400, 50000000)

# condo = Condominio(1200, 10000)

# condo.adicionar_casa(casa1)
# condo.adicionar_casa(casa2)
# condo.adicionar_casa(casa3)
# condo.adicionar_casa(casa4)

# print(condo.retornar_quant_casas())
# print(condo.retornar_espaco_sobrando())

class Funcionario:
    def __init__(self, nome, idade, salario):
        self.nome = nome 
        self.idade = idade 
        self.salario = salario 
    

class Dev(Funcionario):
    def aumento(self):
        aumento = (20 * self.salario) / 100
        self.salario += aumento
        print(f"\nFuncionário {self.nome}, recebeu aumento de: {aumento}. Salário atual: {self.salario}")


class RH(Funcionario):
    def aumento(self):
        aumento = (5 * self.salario) / 100
        self.salario += aumento
        print(f"\nFuncionário {self.nome}, recebeu aumento de: {aumento}. Salário atual: {self.salario}")


dev = Dev("Marta", 23, 6800)
rh = RH("Ana", 20, 2500)

dev.aumento()
rh.aumento()