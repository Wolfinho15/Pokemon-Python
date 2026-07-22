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

        self.adversary_pokemon = self.adversary_trainer.pokemons[0]
        while len(self.player.pokemons) != 0 and len(self.adversary_trainer.pokemons) != 0:
            print("Escolha qual pokemon irá batalhar:")
            for indice, pokemon in enumerate(self.player.pokemons):
                print(indice, "-", pokemon.name)
            while True:
                try:
                    escolha = int(input("Escolha: "))
                    self.player_pokemon = self.player.pokemons[escolha]
                    break
                except ValueError:
                    print("Precisa ser um número dentre os mostrados!!!")
                except IndexError:
                    print("Este pokemon não existe!!!")  
            print(self.adversary_trainer.name, "escolheu", self.adversary_pokemon.name)
            
            ##Loop da batalha
            while self.adversary_pokemon.life > 0 and self.player_pokemon.life > 0:
                print("Escolha seu ataque:")
                self.player_pokemon.listar_ataques()
                while True:
                    try:
                        indice = int(input("Escolha:"))
                        self.player_pokemon.use_attack(indice, self.adversary_pokemon)
                        break
                    except IndexError:
                        print("Esse ataque não existe!!!")
                    except ValueError:
                        print("Precisa ser um número dentre os mostrados!!!")
                    
                if self.adversary_pokemon.life <= 0:
                    self.adversary_trainer.pokemons.pop(0)
                    if len(self.adversary_trainer.pokemons) > 0:
                        self.adversary_pokemon = self.adversary_trainer.pokemons[0]
                        print(self.adversary_trainer.name, "escolheu", self.adversary_pokemon.name)
                    break
                
                indice = random.randint(0, len(self.adversary_pokemon.attacks) - 1)
                self.adversary_pokemon.use_attack(indice, self.player_pokemon)
                if self.player_pokemon.life <= 0:
                        self.player.pokemons.remove(self.player_pokemon)

                
        if len(self.player.pokemons) == 0:
            print("Você foi derrotado")
        elif len(self.adversary_trainer.pokemons) == 0:
            print("Você ganhou!")
                

        
battle = Battle_config(Trainers.Ash, Trainers.Hsa)
battle.start_battle()
        
    
        
     
        
        
        
        