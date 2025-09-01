# -*- coding: utf-8 -*-
# src/neon_dreams/world/enemies_db.py

from ..components.enemy import Enemy

enemies_db = {
    # --- Nível 1
    "ursinho_remendado": Enemy(
        id="ursinho_remendado", name="Ursinho de Pelúcia Remendado",
        max_health=35, current_health=35, attack_power=7, defense_power=4,
        upgrade_points_reward=6, loot_table=["adesivo_desgastado", "biscoito_de_chocolate"]
    ),
    "soldadinho_hacker": Enemy(
        id="soldadinho_hacker", name="Soldadinho de Chumbo Hacker",
        max_health=25, current_health=25, attack_power=9, defense_power=2,
        upgrade_points_reward=7, loot_table=["tampinha_de_garrafa"]
    ),
    "palhaco_de_mola_bugado": Enemy(
        id="palhaco_de_mola_bugado", name="Palhaço de Mola Bugado",
        max_health=30, current_health=30, attack_power=10, defense_power=1,
        upgrade_points_reward=8, loot_table=["pirulito_colorido"]
    ),
    "bloco_de_montar_agressivo": Enemy(
        id="bloco_de_montar_agressivo", name="Bloco de Montar Agressivo",
        max_health=45, current_health=45, attack_power=5, defense_power=6,
        upgrade_points_reward=6, loot_table=["massinha_de_modelar"]
    ),
    "fantoche_desobediente": Enemy(
        id="fantoche_desobediente", name="Fantoche Desobediente",
        max_health=30, current_health=30, attack_power=8, defense_power=3,
        upgrade_points_reward=5, loot_table=["livro_de_colorir"]
    ),
    "piao_descontrolado": Enemy(
        id="piao_descontrolado", name="Pião Descontrolado",
        max_health=20, current_health=20, attack_power=12, defense_power=2, # Rápido e agressivo
        upgrade_points_reward=7, loot_table=["bala_de_goma"]
    ),
    "sombra_de_abajur": Enemy(
        id="sombra_de_abajur", name="Sombra de Abajur Dançarina",
        max_health=28, current_health=28, attack_power=9, defense_power=3,
        upgrade_points_reward=6, loot_table=["adesivo_desgastado"]
    ),
    "monstrinho_de_massinha": Enemy(
        id="monstrinho_de_massinha", name="Monstrinho de Massinha Deformado",
        max_health=40, current_health=40, attack_power=6, defense_power=5,
        upgrade_points_reward=7, loot_table=["massinha_de_modelar"]
    ),
    "robo_de_brinquedo_com_defeito": Enemy(
        id="robo_de_brinquedo_com_defeito", name="Robô de Brinquedo com Defeito",
        max_health=38, current_health=38, attack_power=8, defense_power=4,
        upgrade_points_reward=8, loot_table=["carrinho_de_brinquedo"]
    ),
    "carrinho_bate_bate": Enemy(
        id="carrinho_bate_bate", name="Carrinho Bate-Bate",
        max_health=30, current_health=30, attack_power=10, defense_power=3,
        upgrade_points_reward=6, loot_table=["tampinha_de_garrafa"]
    ),

    # --- Nível 2 
    "boneca_sem_rosto": Enemy(
        id="boneca_sem_rosto", name="Boneca de Porcelana sem Rosto",
        max_health=60, current_health=60, attack_power=14, defense_power=8,
        upgrade_points_reward=15, loot_table=["colar_de_micangas", "kit_de_maquiagem_infantil"]
    ),
    "bicho_papao_de_dados": Enemy(
        id="bicho_papao_de_dados", name="Bicho-Papão de Dados",
        max_health=55, current_health=55, attack_power=16, defense_power=6,
        upgrade_points_reward=18, loot_table=["patins_antigo"]
    ),
    "marionete_sem_fios": Enemy(
        id="marionete_sem_fios", name="Marionete com Fios Cortados",
        max_health=65, current_health=65, attack_power=15, defense_power=7,
        upgrade_points_reward=17, loot_table=["diario_com_cadeado"]
    ),
    "unicornio_de_pelucia_sombrio": Enemy(
        id="unicornio_de_pelucia_sombrio", name="Unicórnio de Pelúcia Sombrio",
        max_health=70, current_health=70, attack_power=12, defense_power=10,
        upgrade_points_reward=16, loot_table=["fantasia_de_princesa"]
    ),
    "super_heroi_corrompido": Enemy(
        id="super_heroi_corrompido", name="Super-Herói de Plástico Corrompido",
        max_health=50, current_health=50, attack_power=18, defense_power=5,
        upgrade_points_reward=19, loot_table=["gibi_antigo"]
    ),
    "guarda_noturno_do_armario": Enemy(
        id="guarda_noturno_do_armario", name="Guarda-Noturno do Armário",
        max_health=80, current_health=80, attack_power=10, defense_power=12,
        upgrade_points_reward=20, loot_table=["lancheira_termica"]
    ),
    "cama_monstruosa": Enemy(
        id="cama_monstruosa", name="A Cama Monstruosa",
        max_health=90, current_health=90, attack_power=8, defense_power=15, # Muito defensivo
        upgrade_points_reward=22, loot_table=["estojo_escolar"]
    ),

    # --- Nível 3 / Mini-Bosses
    "o_medo_do_escuro": Enemy(
        id="o_medo_do_escuro", name="O Medo do Escuro",
        max_health=120, current_health=120, attack_power=25, defense_power=8, # Ataca forte, mas é frágil
        upgrade_points_reward=50, loot_table=["casa_de_boneca_em_miniatura"]
    ),
    "a_baba_fantasma": Enemy(
        id="a_baba_fantasma", name="A Babá Fantasma",
        max_health=150, current_health=150, attack_power=18, defense_power=15,
        upgrade_points_reward=60, loot_table=["pulseira_da_amizade"]
    ),
    "amigo_imaginario_esquecido": Enemy(
        id="amigo_imaginario_esquecido", name="Amigo Imaginário Esquecido",
        max_health=130, current_health=130, attack_power=22, defense_power=18,
        upgrade_points_reward=70, loot_table=["relogio_quebrado_do_papai"]
    ),
    
    # --- Boss Final
    "o_rei_sonolento": Enemy(
        id="o_rei_sonolento", name="O Rei Sonolento",
        max_health=300, current_health=300, attack_power=35, defense_power=20,
        upgrade_points_reward=200, loot_table=["memoria_do_despertar"]
    ),
}