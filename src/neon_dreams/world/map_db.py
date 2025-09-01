# -*- coding: utf-8 -*-
# src/neon_dreams/world/map_db.py

from ..components.room import Room

world_map = {

    "praca_central": Room(
        id="praca_central",
        name="Praça Central",
        description="O coração pulsante da cidade, um oásis de luz em meio às sombras. Pessoas e drones passam apressados. Daqui, você pode acessar as várias zonas da cidade.",
        exits={"norte": "mercado_tecnologico", "leste": "beco_de_neon", "oeste": "cyber_cafe"},
        room_type="hub", 
        loot_tier=0
    ),

    # --- Zona Oeste 
    "cyber_cafe": Room(
        id="cyber_cafe",
        name="Cyber Café 'O Sonho'",
        description="Um café pequeno e aconchegante, cheio de hackers e netrunners. O cheiro de café sintético e ozônio está no ar.",
        exits={"este": "praca_central"},
        room_type="hostile",
        enemy_pool=["soldadinho_hacker", "spam_zinho"],
        loot_tier=1,
        fixed_items=["mom_luiza_avatar"] 
    ),

    # --- Zona Leste 
    "beco_de_neon": Room(
        id="beco_de_neon",
        name="Beco de Neon",
        description="Um beco estreito e úmido, iluminado por letreiros piscando. Poças d'água refletem as luzes, criando um mosaico de cores.",
        exits={"oeste": "praca_central", "leste": "armazem_abandonado"},
        room_type="hostile",
        enemy_pool=["poeira_bot", "cabo_enrola"],
        loot_tier=1
    ),
    "armazem_abandonado": Room(
        id="armazem_abandonado",
        name="Armazém Abandonado",
        description="Um prédio dilapidado, com caixas e contêineres espalhados. Dizem ser um esconderijo de programas piratas.",
        exits={"oeste": "beco_de_neon"},
        room_type="boss", 
        enemy_pool=["o_construtor"], 
        loot_tier=2
    ),

    # --- Zona Norte 
    "mercado_tecnologico": Room(
        id="mercado_tecnologico",
        name="Mercado Tecnológico",
        description="Uma feira a céu aberto com barracas vendendo gadgets e aprimoramentos cibernéticos de segunda mão.",
        exits={"sul": "praca_central", "norte": "saida_da_via_expressa"},
        room_type="hostile",
        enemy_pool=["piao_descontrolado", "robo_de_brinquedo_com_defeito"],
        loot_tier=1
    ),
    "saida_da_via_expressa": Room(
        id="saida_da_via_expressa",
        name="Saída da Via Expressa",
        description="Uma passarela de metal que leva à principal via de transporte da cidade. Veículos voadores passam em alta velocidade.",
        exits={"sul": "mercado_tecnologico", "norte": "torre_do_portao"},
        room_type="hostile",
        enemy_pool=["carrinho_enlouquecido", "baba_eletronica"],
        loot_tier=2,
        fixed_items=["dad_caue_avatar"] 
    ),
    "torre_do_portao": Room(
        id="torre_do_portao",
        name="Torre do Portão",
        description="Uma estrutura imponente que serve como a entrada principal para o núcleo da cidade. É fortemente vigiada.",
        exits={"sul": "saida_da_via_expressa", "norte": "portao_final"},
        room_type="hostile",
        enemy_pool=["guarda_noturno_do_armario", "super_heroi_corrompido"],
        loot_tier=3,
        fixed_items=["access_card"]
    ),
    "portao_final": Room(
        id="portao_final",
        name="Portão Final",
        description="O portão final que leva para fora da cidade digital. É guardado pela entidade mais poderosa deste sonho.",
        exits={"sul": "torre_do_portao"},
        room_type="boss",
        enemy_pool=["o_rei_sonolento"], 
        loot_tier=3
    ),

    # --- Salas Adicionais para completar o mundo 
    "telhados_sombrios": Room(
        id="telhados_sombrios",
        name="Telhados Sombrios",
        description="Os telhados da cidade, oferecendo uma vista panorâmica do horizonte de neon. Um lugar perigoso e silencioso.",
        exits={"sul": "beco_de_neon"},
        room_type="hostile",
        enemy_pool=["sombra_do_quarto", "bicho_papao_de_dados"],
        loot_tier=2
    ),
    "sala_dos_servidores": Room(
        id="sala_dos_servidores",
        name="Sala dos Servidores",
        description="O ar aqui é gelado. Fileiras e mais fileiras de servidores processam os dados que mantêm a cidade-sonho funcionando.",
        exits={"sul": "mercado_tecnologico"},
        room_type="boss",
        enemy_pool=["amigo_imaginario_esquecido"], 
        loot_tier=3
    ),
    "fronteira_da_cidade": Room(
        id="fronteira_da_cidade",
        name="Fronteira da Cidade",
        description="O limite da metrópole digital, onde o código da cidade começa a se desfazer em natureza selvagem e dados corrompidos.",
        exits={"oeste": "torre_do_portao"},
        room_type="hostile",
        enemy_pool=["cama_monstruosa", "marionete_sem_fios"],
        loot_tier=3
    ),
    "esgotos_de_dados": Room(
        id="esgotos_de_dados",
        name="Esgotos de Dados",
        description="Túneis escuros por onde flui o lixo de informação da cidade. Coisas esquecidas e perigosas vivem aqui.",
        exits={"norte": "beco_de_neon"},
        room_type="hostile",
        enemy_pool=["monstrinho_de_massinha", "fantoche_desobediente"],
        loot_tier=1
    )
}