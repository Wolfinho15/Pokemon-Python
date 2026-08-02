from Classes.Pokemon import Pokemon
from Dados.Pokemons import POKEMONS

def criar_pokemon(nome: str) -> Pokemon:
    dados = POKEMONS[nome]
    
    pokemon = Pokemon(
                    nome,
                    dados["life"],
                    dados["life"],
                    dados["type"],
                    dados["defense"],
                    dados["crit_rate"],
                    dados["attack"],
                    
                    )
    for move in dados["moves"]:
        pokemon.learn_move(move)
    return pokemon
