# -*- coding: utf-8 -*-

import asyncio
import random

from .world.events import ambient_events

async def ambient_task():
    """
    Tarefa que roda de forma assincrona exibindo mensagens
    e eventos do ambiente de forma aleatória
    """
    while True:
        interval = random.uniform(15, 30)
        await asyncio.sleep(interval)
        
        message = random.choice(ambient_events)
        print(f"\n<< {message} >>")

async def game_loop_task():
    """
    A tarefa principal do jogo, onde o jogador digita comandos
    """

    # TODO: Implementar o loop de input do jogador de forma assíncrona
    print("Ísis: Neon Dreams - O jogo começou!")

    while True:
        await asyncio.sleep(1)


async def main():
    """
    Função que inicia e gerencia todas as tarefas assíncronas.
    """
    print("Iniciando o motor do jogo...")
    
    # Cria a tarefa para rodar em segundo plano
    ambience = asyncio.create_task(ambient_task())
    # Cria a tarefa do loop principal do jogo
    game_loop = asyncio.create_task(game_loop_task())
    await asyncio.gather(ambience, game_loop)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nJogo encerrado pelo usuário. Até a próxima!")