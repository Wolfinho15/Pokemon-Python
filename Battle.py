from Classes.Treinador import Trainer

from Dados.Pokemons import Pokemons_disponiveis
from Dados import Attacks
from Dados import Trainers
import random




class Battle_config():
    def __init__(self, player, adversary_trainer):
        self.player = player
        self.adversary_trainer = adversary_trainer
        self.player_pokemon = None
        self.adversary_pokemon = None
    
    def start_battle(self):

        x = 0
        self.adversary_pokemon = self.adversary_trainer.pokemons[x]
        while len(self.player.pokemons) != 0 and len(self.adversary_trainer.pokemons) != 0:
            print("Escolha qual pokemon irá batalhar:")
            for indice, pokemon in enumerate(self.player.pokemons):
                print(indice, "-", pokemon.name)
            escolha = int(input("Escolha: "))
            self.player_pokemon = self.player.pokemons[escolha]
            print(self.adversary_trainer.name, "escolheu", self.adversary_pokemon.name)
            
            ##Loop da batalha
            while self.adversary_pokemon.life > 0 and self.player_pokemon.life > 0:
                if self.player_pokemon.life > 0:
                    print("Escolha seu ataque:")
                    self.player_pokemon.listar_ataques()
                    indice = int(input("Escolha:"))
                    self.player_pokemon.use_attack(indice, self.adversary_pokemon)
                    
                if self.adversary_pokemon.life > 0:
                    indice = random.randint(0, len(self.adversary_pokemon.attacks) - 1)
                    self.adversary_pokemon.use_attack(indice, self.player_pokemon)
                    if self.player_pokemon.life <= 0:
                        self.player.pokemons.pop(escolha)
                else:
                    self.adversary_trainer.pokemons.pop(x)
                    self.adversary_pokemon = self.adversary_trainer.pokemons[x]
                    print(self.adversary_trainer.name, "escolheu", self.adversary_pokemon.name)
        if len(self.player.pokemons) == 0:
            print("Você foi derrotado")
        elif len(self.adversary_trainer.pokemons) == 0:
            print("Você ganhou!")
                

        
battle = Battle_config(Trainers.Ash, Trainers.Hsa)
battle.start_battle()
        
    
        
     
        
        
        
        