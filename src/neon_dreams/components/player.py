# -*- coding: utf-8 -*-

from dataclasses import dataclass, field
from .skill import MemorySkill 


@dataclass
class Player:
    """ Representa a protagonista: Ísis. Com seus atributos, estado e sistema de progressão """
    name: str

    # Atributos
    current_health: int
    max_health: int
    current_energy: int
    max_energy: int
    attack_power: int
    defense_power: int

    # Atributos de progressão
    upgrade_points: int = 0

    # Atributos temporários
    current_shield: int = 0
    mom_heal_used_in_combat: bool = False

    # Slots
    inventory_slots: int = 5
    skill_slots: int = 3

    # Coleções
    inventory: list[str] = field(default_factory=list)
    learned_skills: list['MemorySkill'] = field(default_factory=list)

    def is_alive(self) -> bool:
        """ Verifica se o personagem possui hp """
        return self.current_health > 0
    
    def take_damage(self, amount: int) -> int:
        """ Lógica para processar o dano recebido considerando escudo e defesa """
        # Dano absorvido pelo escudo
        absorbed_by_shield = min(self.current_shield, amount)
        self.current_shield -= absorbed_by_shield
        remaining_damage = amount - absorbed_by_shield

        # Dano restante reduzido pela defesa e aplicado ao hp
        final_damage = max(0, remaining_damage - self.defense_power)
        self.current_health -= final_damage
        if self.current_health < 0:
            self.current_health = 0

        return final_damage
    
    def learn_skill(self, skill: MemorySkill):
        """ Adiciona habilidade se ainda não aprendida """
        if skill not in self.learned_skills:
            self.learned_skills.append(skill)