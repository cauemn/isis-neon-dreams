# -*- coding: utf-8 -*-

import asyncio
import random
import pprint

from typing import NoReturn
from .game_state import GameStateManager
from .world.events import ambient_events

async def ambient_task() -> NoReturn:
    """
    Tarefa que roda de forma assincrona exibindo mensagens
    e eventos do ambiente de forma aleatória
    """
    while True:
        interval: float = random.uniform(15, 30)
        await asyncio.sleep(interval)
        
        message: str = random.choice(ambient_events)
        print(f"\n<< {message} >>")

async def game_loop_task() -> NoReturn:
    
    game = GameStateManager()
    
    print(f"Sala inicial: {game.current_room_id}")
    estado_da_sala = game.get_current_room_dynamic_state()
    pprint.pprint(estado_da_sala)
    
    while True:
        await asyncio.sleep(60)


async def main() -> None:
    """ A função principal que inicia as tarefas. """
    ambience: asyncio.Task[NoReturn] = asyncio.create_task(ambient_task())
    game_loop: asyncio.Task[NoReturn] = asyncio.create_task(game_loop_task())
    await asyncio.gather(ambience, game_loop)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nJogo encerrado pelo usuário. Até a próxima!")