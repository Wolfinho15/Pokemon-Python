class Pokemon():
    def __init__(self, name:str, life:int, type:str, atacks:dict):
        self.name = name
        self.life = life
        self.type = type
        self.atacks = {}
        
    def use_atack(self, atack, target):
        target.life -= atack.dammage 
        if target.life < 0:
            target.life = 0
        print(self.name, "usou", atack.name, "causando", atack.dammage, "de dano em", target.name, "!!!")
        print("Vida restante:", target.life)
        if target.life == 0:
            print(target.name, "foi nocauteado!!!")

class Atack():
    def __init__(self, name:str, type:str, dammage):
        self.name = name
        self.type = type
        self.dammage = dammage
        
class Trainer():
    def __init__(self, name:"str", bag:dict, pokemons:dict):
        self.name = name
        self.bag = {}
        self.pokemons = {}
