# -*- coding: utf-8 -*-

from dataclasses import dataclass, field

@dataclass
class Enemy:
    """ Represente o blueprint de um inimigo """
    id: str
    name: str

    # Atributos
    current_health: int
    max_health: int
    attack_power: int
    defense_power: int

    # Recompensas: pontos de atributo e lista de itens possíveis
    upgrade_points_reward: int = 0
    loot_table: list[str] = field(default_factory=list)

    def is_alive(self) -> bool:
        return self.current_health > 0
    
    def take_damage(self, amount: int) -> int:
        """ Lógica do dano recebido considerando a defesa """
        final_damage = max(0, amount - self.defense_power)
        self.current_health -= final_damage
        if self.current_health < 0:
            self.current_health = 0
        return final_damage