from Sistemas.Damage import calculate_damage

class Pokemon():
    def __init__(self, name:str, life:int, type:str):
        self.name = name
        self.life = life
        self.type = type
        self.attacks = []
        
    def __str__(self):
        return self.name
        
    def use_attack(self, attack, target):
        attack = self.attacks[attack]
        damage = calculate_damage(attack, target)
        target.life -= damage
        if target.life < 0:
            target.life = 0
        print(self.name, "usou", attack.name, "causando", damage, "de dano em", target.name, "!!!")
        print("Vida restante:", target.life)
        if target.life == 0:
            print(target.name, "foi nocauteado!!!")
            
    def learn_attack(self, attack):
        self.attacks.append(attack)
        
    def listar_ataques(self):
        print("Ataques de ", self.name, ":")
        for indice, ataque in enumerate(self.attacks):
            print(indice, "-", ataque.name)
