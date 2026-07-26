from Dados.Types import type_effectiveness

def calculate_damage(pokemon, attack, target):
    type_multiplier = type_effectiveness.get(attack.type, {}).get(target.type, 1)
    stab_multiplier = 1
    if pokemon.type == attack.type:
        stab_multiplier = 1.5
        
    damage = int(attack.damage * type_multiplier * stab_multiplier)  
    
    print("Dano base:", attack.damage)
    print("Multiplicador de tipo:", type_multiplier)
    print("STAB:", stab_multiplier)
    print("Dano final:", damage)
    return damage
