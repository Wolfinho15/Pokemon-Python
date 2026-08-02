from Classes.Treinador import Trainer
from Classes.Moves import Moves
from Classes.Pokemon import Pokemon

from Dados import Moves
from Dados.Pokemons import POKEMONS
from Dados import Trainers
from Battle import Battle_config

def players_config():
   pass

def game_config():
   pass

battle = Battle_config(Trainers.Ash, Trainers.Hsa)
menu_options = {
     1:{"texto":"Iniciar Batalha",
        "funcao":battle.battle},
     2:{"texto":"Configurar Jogadores",
        "funcao":players_config},
     3:{"texto":"Configurações de Jogo",
        "funcao":game_config}   
}
def start_game():
   for chave, opcao in menu_options.items():
      print(f"{chave} - {opcao['texto']}")
   indice = int(input("Bem vindo, escolha o que fazer: "))
    
   menu_options[indice]["funcao"]()
   
   
   
start_game()

    
    
    






