class Trainer():
    def __init__(self, name:str, bag:dict, pokemons:list):
        self.name = name
        self.bag = bag if bag else {}
        self.pokemons = pokemons
        
    def has_pokemons(self):
        return len(self.pokemons) > 0
    
    def first_pokemon(self):
        return self.pokemons[0]
    
    def remove_pokemon(self, pokemon):
        self.pokemons.remove(pokemon)
        