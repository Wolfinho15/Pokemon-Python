from Classes.Treinador import Trainer

from Dados.Pokemons import POKEMONS
from Dados import Moves
from Dados import Trainers
import random




class Battle_config():
    def __init__(self, player:Trainer, adversary_trainer:Trainer):
        self.player = player
        self.adversary_trainer = adversary_trainer
        self.player_pokemon = None
        self.adversary_pokemon = None
    
    def player_turn(self):
        print("Escolha seu movimento:")
        self.player_pokemon.listar_moves()
        while True:
            try:
                indice = int(input("Escolha:"))
                self.player_pokemon.use_move(indice, self.adversary_pokemon)
                break
            except IndexError:
                print("Esse movimento não existe!!!")
            except ValueError:
                print("Precisa ser um número dentre os mostrados!!!")
                
    def adversary_fainted(self) -> bool:
        if self.adversary_pokemon.life <= 0:
            self.adversary_trainer.remove_pokemon(self.adversary_pokemon)
            return True
        return False
    
    def player_fainted(self):
        if self.is_fainted:
            self.player.remove_pokemon(self.player_pokemon)
            return True
        return False

    def adversary_turn(self):
        indice = random.randint(0, len(self.adversary_pokemon.moves) - 1)
        self.adversary_pokemon.use_move(indice, self.player_pokemon)
        
    def choose_adversary_pokemon(self):
        if len(self.adversary_trainer.pokemons) > 0:
            self.adversary_pokemon = self.adversary_trainer.first_pokemon()
            print(self.adversary_trainer.name, "escolheu", self.adversary_pokemon.name)
            
    def choose_player_pokemon(self):
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
        
    def battle(self):
        self.choose_adversary_pokemon()
        self.choose_player_pokemon()
        print
        
        while self.player.pokemons and self.adversary_trainer.pokemons:
            
            self.player_turn()
            
            if self.adversary_fainted():
                if self.adversary_trainer.pokemons:
                    self.choose_adversary_pokemon()
                    continue
                break
            
            self.adversary_turn()
    
            if self.player_fainted():
                if self.player.has_pokemons():
                    self.choose_player_pokemon()
                    continue
                break

        if len(self.player.pokemons) == 0:
            print("Você foi derrotado")
        elif len(self.adversary_trainer.pokemons) == 0:
            print("Você ganhou!")
                

        

        
    
        
     
        
        
        
        