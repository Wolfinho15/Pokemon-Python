from Dados.Types import type_effectiveness

def calculate_damage(attack, target):
    multiplier = type_effectiveness.get(attack.type, {}).get(target.type, 1)

    return int(attack.damage * multiplier)