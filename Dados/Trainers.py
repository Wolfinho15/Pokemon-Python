from Classes.Pokemon import Pokemon
from Classes.Treinador import Trainer
from Dados.Pokemons import POKEMONS
from Sistemas.Factory import criar_pokemon

Ash = Trainer(
            "Ahs",
            None,
            [
            criar_pokemon("Pikachu"),
            criar_pokemon("Charizard"),
            criar_pokemon("Venusaur")
            ]
        )

Hsa = Trainer(
            "hsa",
            None,
            [
            criar_pokemon("Blastoise"),
            criar_pokemon("Gengar"),
            criar_pokemon("Venusaur")
            ]
        )