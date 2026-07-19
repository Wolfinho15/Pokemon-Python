class Trainer():
    def __init__(self, name:str, bag:dict, pokemons:list):
        self.name = name
        self.bag = bag if bag else {}
        self.pokemons = pokemons