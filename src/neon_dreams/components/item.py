# -*- coding: utf-8 -*-

from dataclasses import dataclass
from typing import Optional, Dict

@dataclass
class Item:
    """ Represanta a blueprint de um item do jogo """
    id: str
    name: str
    description: str

    # Tipo do item e raridade
    item_type: str
    tier: int = 1

    # Atributos opcionais
    stat_boosts: Optional[Dict[str, int]] = None
    effect: Optional[str] = None
    amount: Optional[int] = None

    # Para sucata que pode ser trocada por pontos
    value: Optional[int] = None
    
    # Para itens de história/boss que concedem uma skill
    skill_id: Optional[str] = None