# -*- coding: utf-8 -*-
from dataclasses import dataclass, field

@dataclass
class Room:
    """ Representa uma sala do mapa """
    id: str
    name: str
    description: str

    # Mapear as direções para outras salas
    exits: dict[str, str] = field(default_factory=dict)

    # Define se a sala é hostil e sua enemy pool
    room_type: str = "hostile"
    enemy_pool: list[str] = field(default_factory=list)
    
    # Define loot tier(comum, incomum, raro) e se existem itens fixos
    loot_tier: int = 1
    fixed_items: list[str] = field(default_factory=list)

