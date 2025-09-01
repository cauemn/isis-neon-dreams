# -*- coding: utf-8 -*-

from ..components.skill import MemorySkill

# Este dicionário funciona como nosso banco de dados para todas as skills
# A 'chave' é o ID que usamos no código e o 'valor' é o objeto Skill completo
skills_db: dict[str, MemorySkill] = { 

    # --- SKILLS PASSIVAS (AVATARES) ---
    "escudo_do_papai": MemorySkill(
        name="Abraço do Papai Cauê",
        description="Uma forte lembrança de seu pai te envolvendo em um abraço que te fazia sentir a pessoa mais segura do mundo. A sensação é tão real que se manifesta como um escudo de energia no início de cada luta.",
        effect_id="dad_shield_effect",
        skill_type="passiva",
    ),

    "cura_da_mamae": MemorySkill(
        name="Voz da Mamãe Luiza",
        description="No momento de maior perigo, a voz calma da sua mãe ecoa em sua mente, dizendo que tudo vai ficar bem. Essa memória aciona um reparo de emergência, restaurando sua força para continuar.",
        effect_id="mom_heal_effect",
        skill_type="passiva",
    ),

    # --- SKILLS DE "BRINCADEIRAS" (DANO) ---
    "desenho_magico": MemorySkill(
        name="Desenho Mágico",
        description="Você se lembra de desenhar com giz de cera coloridos. Rabiscos de energia pura voam e atingem o alvo, ignorando parte de sua proteção.",
        effect_id="deal_armor_piercing_damage",
        skill_type="ativa",
        energy_cost=15,
        uses_per_room=3
    ),
    "bicho_papao": MemorySkill(
        name="História do Bicho-Papão",
        description="Você se lembra de uma história de terror de mentirinha. Um fantasma de dados assombra o alvo, causando dano contínuo por 3 turnos.",
        effect_id="apply_dot_damage",
        skill_type="ativa",
        energy_cost=20,
        uses_per_room=1
    ),
    "beijo_sarador": MemorySkill(
        name="Beijo Sarador",
        description="Uma lembrança de um 'beijinho para sarar' após um joelho ralado. Causa um dano leve ao inimigo e recupera metade do dano como vida para você.",
        effect_id="lifesteal_damage",
        skill_type="ativa",
        energy_cost=18,
        uses_per_room=2
    ),

    # --- SKILLS DE "TRAVESSURAS" (CONTROLE) ---
    "esconde_esconde": MemorySkill(
        name="Esconde-Esconde",
        description="Você lembra da emoção de se esconder. Você some em um piscar de luz, com chance de confundir o alvo e fazê-lo perder o próximo turno.",
        effect_id="stun_enemy",
        skill_type="ativa",
        energy_cost=20,
        uses_per_room=2
    ),
    "quebra_cabeca": MemorySkill(
        name="Quebra-Cabeça",
        description="Você lembra de montar um quebra-cabeça com seu pai. Você encontra uma 'peça faltando' na defesa do inimigo, reduzindo-a pela metade por 2 turnos.",
        effect_id="reduce_enemy_defense",
        skill_type="ativa",
        energy_cost=15,
        uses_per_room=2
    ),
    "grito_de_susto": MemorySkill(
        name="Grito de Susto!",
        description="Um 'BU!' repentino e digitalizado. O susto desorienta o alvo, reduzindo seu poder de ataque por 2 turnos.",
        effect_id="reduce_enemy_attack",
        skill_type="ativa",
        energy_cost=15,
        uses_per_room=2
    ),

    # --- SKILLS DE "CUIDADO" (SUPORTE) ---
    "band_aid_colorido": MemorySkill(
        name="Band-Aid Colorido",
        description="Você lembra de colocar um curativo de dinossauro. Nanites em forma de band-aid reparam seus sistemas, restaurando uma quantidade moderada de vida.",
        effect_id="active_heal",
        skill_type="ativa",
        energy_cost=12,
        uses_per_room=3
    ),
    "abraco_de_urso": MemorySkill(
        name="Abraço de Urso de Pelúcia",
        description="A sensação de segurança de abraçar seu urso favorito cria uma barreira protetora, aumentando sua defesa por 3 turnos.",
        effect_id="temp_defense_boost",
        skill_type="ativa",
        energy_cost=10,
        uses_per_room=2
    ),
    "doce_energetico": MemorySkill(
        name="Doce Energético",
        description="A lembrança do gosto do seu doce preferido te dá um pico de energia, garantindo uma ação extra imediatamente.",
        effect_id="gain_extra_turn",
        skill_type="ativa",
        energy_cost=30,
        uses_per_room=1
    ),
    "brincar_de_espiao": MemorySkill(
        name="Brincar de Espiã",
        description="Você lembra de brincar de espionagem. Você analisa cuidadosamente o alvo, revelando seus pontos fracos (vida e status).",
        effect_id="scan_enemy_stats",
        skill_type="ativa",
        energy_cost=5,
        uses_per_room=10
    ),
    } 

