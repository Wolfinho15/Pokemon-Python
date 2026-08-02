from Dados.Types import type_effectiveness
import random
from Classes.Pokemon import Pokemon
from Classes.Moves import Moves

CRITICAL_DAMAGE = 1.5
STAB_MULTIPLIER = 1.5

def critical(crit_rate:float) -> bool:
    return random.random() < crit_rate

def calculate_damage(attacker:Pokemon, move:Moves, defender:Pokemon) -> int:
    type_multiplier = type_effectiveness.get(move.type, {}).get(defender.type, 1)
        
    damage:float = move.damage 
    damage *= type_multiplier
    damage *= STAB_MULTIPLIER if attacker.type == move.type else 1
    damage *= CRITICAL_DAMAGE if critical(attacker.crit_rate) else 1  
    damage *= attacker.attack / defender.defense
    
    return int(damage)
