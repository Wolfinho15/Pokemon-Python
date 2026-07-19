from Classes.Treinador import Trainer

from Dados.Pokemons import Pokemons_disponiveis
from Dados import Attacks
from Dados import Trainers




class Battle_config():
    def __init__(self, player, adversary_trainer):
        self.player = player
        self.adversary_trainer = adversary_trainer
        self.player_pokemon = None
        self.adversary_pokemon = adversary_trainer.pokemons[0]
    
    def start_battle(self):
        print("Escolha qual pokemon irá batalhar:")
        for indice, pokemon in enumerate(self.player.pokemons):
            print(indice, "-", pokemon.name)
        escolha = int(input("Escolha: "))
        self.player_pokemon = self.player.pokemons[escolha]
        print(self.adversary_trainer.name, "Escolheu:", self.adversary_pokemon.name)
        while self.adversary_pokemon.life > 0 and self.player_pokemon.life > 0:
            print("Escolha seu ataque:")
            self.player_pokemon.listar_ataques()
            
            indice = int(input("Escolha:"))
            self.player_pokemon.use_attack(indice, self.adversary_pokemon)
        
        
battle = Battle_config(Trainers.Ash, Trainers.Hsa)
battle.start_battle()
        
    
        
     
        
        
        
        