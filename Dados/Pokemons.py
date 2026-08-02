from Classes.Pokemon import Pokemon
from Dados import Moves


POKEMONS = {
    "Pikachu":{
        "life": 100,
        "type":"Elétrico",
        "defense":70,
        "crit_rate":0.12,
        "attack":95,
        "moves":[
            Moves.choque_do_trovao,
            Moves.cauda_de_ferro,
            Moves.investida
        ]
    },
    "Charizard":{
        "life":180,
        "type":"Fogo",
        "defense":85,
        "crit_rate":0.10,
        "attack":120,
        "moves":[
            Moves.lanca_chamas,
            Moves.asa_de_aco,
            Moves.explosao_de_fogo,
            Moves.garra_de_aco
        ]   
    },
    "Blastoise":{
        "life":200,
        "type":"Água",
        "defense":130,
        "crit_rate":0.06,
        "attack":90,
        "moves":[
            Moves.hidro_bomba,
            Moves.jato_dagua,
            Moves.mordida,
            Moves.investida
        ]
    },
    "Venusaur":{
        "life":190,
        "type":"Planta",
        "defense":110,
        "crit_rate":0.08,
        "attack":95,
        "moves":[
            Moves.chicote_de_vinha,
            Moves.folha_navalha,
            Moves.raio_solar,
            Moves.investida
        ]
    },
    "Gengar":{
        "life":140,
        "type":"Fantasma",
        "defense":60,
        "crit_rate":0.15,
        "attack":130,
        "moves":[
            Moves.bola_sombria,
            Moves.hipnose,
            Moves.lambida,
            Moves.sombra_noturna
        ]
    }
}

