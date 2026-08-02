from Sistemas.Damage import calculate_damage

class Pokemon():
    def __init__(self, name:str, life:int, max_life:int, type:str, defense:int, crit_rate:float, attack:int):
        self.name = name
        self.life = life
        self.max_life = max_life
        self.type = type
        self.defense = defense
        self.crit_rate = crit_rate
        self.attack = attack
        self.moves = []
        
    def __str__(self):
        return self.name
        
    def use_move(self, move, target:Pokemon):
        move = self.moves[move]
        damage = calculate_damage(self, move, target)
        target.life -= damage
        if target.life < 0:
            target.life = 0
        print(self.name, "usou", move.name, "causando", damage, "de dano em", target.name, "!!!")
        print("Vida restante:", target.life)
        if target.life == 0:
            print(target.name, "foi nocauteado!!!")
            
    def learn_move(self, move):
        self.moves.append(move)
        
    def listar_moves(self):
        print("Movimentos de ", self.name, ":")
        for indice, move in enumerate(self.moves):
            print(indice, "-", move.name)
        
    @property    
    def in_fainted(self) -> bool:
        return self.life <= 0
