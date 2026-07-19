from Classes.Pokemon import Pokemon
from Dados import Attacks
pikachu = Pokemon("Pikachu", 100, "Elétrico")
pikachu.learn_attack(Attacks.choque_do_trovao)
pikachu.learn_attack(Attacks.cauda_de_ferro)
pikachu.learn_attack(Attacks.investida)

charizard = Pokemon("Charizard", 180, "Fogo")
charizard.learn_attack(Attacks.lanca_chamas)
charizard.learn_attack(Attacks.garra_de_aco)
charizard.learn_attack(Attacks.asa_de_aco)
charizard.learn_attack(Attacks.explosao_de_fogo)

blastoise = Pokemon("Blastoise", 200, "Água")
blastoise.learn_attack(Attacks.hidro_bomba)
blastoise.learn_attack(Attacks.jato_dagua)
blastoise.learn_attack(Attacks.mordida)
blastoise.learn_attack(Attacks.investida)

venusaur = Pokemon("Venusaur", 190, "Planta")
venusaur.learn_attack(Attacks.chicote_de_vinha)
venusaur.learn_attack(Attacks.folha_navalha)
venusaur.learn_attack(Attacks.raio_solar)
venusaur.learn_attack(Attacks.investida)

gengar = Pokemon("Gengar", 140, "Fantasma")
gengar.learn_attack(Attacks.bola_sombria)
gengar.learn_attack(Attacks.hipnose)
gengar.learn_attack(Attacks.lambida)
gengar.learn_attack(Attacks.sombra_noturna)

Pokemons_disponiveis = [
    pikachu,
    charizard,
    blastoise,
    venusaur,
    gengar
]



