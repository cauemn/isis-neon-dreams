# -*- coding: utf-8 -*-

import random
import copy
from typing import Callable

from neon_dreams.components.enemy import Enemy
from .components.player import Player
from .components.room import Room
from .world.map_db import world_map
from .world.loot_db import Item, random_loot_pool, fixed_items
from .world.enemies_db import enemies_db

class GameStateManager:
    """
    Classe principal que controla o estado atual do jogo.
    """

    def __init__(self) -> None:

        self.player = Player(
            name="Ísis",
            max_health=100,
            current_health=100,
            max_energy=50,
            current_energy=50,
            attack_power=20,
            defense_power=10,
            inventory_slots=5,
            skill_slots=3
        )

        self.world_map: dict[str, Room] = world_map
        self.current_room_id = "praca_central"
        self.visited_rooms_state = {}
        self.loot_pool: list[Item] = list(random_loot_pool)

    def get_current_room(self) -> Room:

        return self.world_map[self.current_room_id]

    def get_current_room_dynamic_state(self) -> dict:
        if self.current_room_id not in self.visited_rooms_state:
            self._generate_room_state(self.current_room_id)

        return self.visited_rooms_state[self.current_room_id]
    
    def move_player(self, direction: str) -> None:
        pass

    def _generate_room_state(self, room_id: str) -> None:
        
        room_template: Room = self.get_current_room()
        self.visited_rooms_state[room_id] = {"items": [], "enemies": []}

        if room_template.room_type == "hostile":
            num_enemies: int = random.choice([1,2])
            possible_enemies: list[str] = room_template.enemy_pool

            for _ in range(num_enemies):
                if possible_enemies:
                    enemy_id: str = random.choice(possible_enemies)
                    enemy_instance: Enemy = copy.deepcopy(enemies_db[enemy_id])
                    self.visited_rooms_state[room_id]["enemies"].append(enemy_instance)

        elif room_template.room_type == "boss":
            boss_id: str = room_template.enemy_pool[0]
            boss_instance: Enemy = copy.deepcopy(enemies_db[boss_id])
            self.visited_rooms_state[room_id]["enemies"].append(boss_instance)
            
        
        for item_id in room_template.fixed_items:
            if item_id in fixed_items:
                self.visited_rooms_state[room_id]["items"].append(fixed_items[item_id])

        num_random_items: int = random.choice([0, 1, 2])
        eligible_loot: list[Item] = [item for item in self.loot_pool if item.tier <= room_template.loot_tier]
        
        for _ in range(num_random_items):
            if eligible_loot:
                chosen_item: Item = random.choice(eligible_loot)
                self.visited_rooms_state[room_id]["items"].append(chosen_item)
                self.loot_pool.remove(chosen_item)
                eligible_loot.remove(chosen_item)