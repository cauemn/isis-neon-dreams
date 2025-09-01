# -*- coding: utf-8 -*-

from dataclasses import dataclass

@dataclass
class MemorySkill:
    """ Representa uma memória que funciona como uma skill no jogo """
    name: str
    description: str

    # Tipo de efeito e tipo de habilidade (passiva ou ativa)
    effect_id: str
    skill_type: str = 'ativa'

    # Custo e limite de uso
    energy_cost: int = 0
    uses_per_room: int = 1