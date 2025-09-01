# -*- coding: utf-8 -*-
# src/neon_dreams/world/loot_db.py

from ..components.item import Item

# ==============================================================================
# ITENS FIXOS (HISTÓRIA, PUZZLES, ETC.)
# ==============================================================================
fixed_items = {
    "avatar_papai_caue": Item(
        id="avatar_papai_caue",
        name="Avatar do Papai Cauê",
        description="Um pequeno avatar digital do seu pai, que emana uma aura de proteção. Traz uma sensação de segurança.",
        item_type="historia",
        tier=0,
        effect="learn_skill",
        skill_id="escudo_do_papai"
    ),
    "avatar_mamae_luiz": Item(
        id="avatar_mamae_luiz",
        name="Avatar da Mamãe Luiza",
        description="Um pequeno avatar digital da sua mãe, que pulsa com uma energia restauradora. Traz uma sensação de conforto.",
        item_type="historia",
        tier=0,
        effect="learn_skill",
        skill_id="cura_da_mamae"
    ),
    "cartao_acesso": Item(
        id="cartao_acesso",
        name="Cartão de Acesso",
        description="Um cartão magnético surrado, necessário para abrir certas portas de alta segurança.",
        item_type="chave",
        tier=0
    ),

    "memoria_do_despertar": Item(
        id="memoria_do_despertar",
        name="Lembrança do Despertar",
        description="Uma memória clara e quente do carinho dos seus pais. Segurá-la te faz sentir sonolento e seguro, como se estivesse na hora de acordar.",
        item_type="final", 
        tier=0
    )
}

# ==============================================================================
# ITENS ALEATÓRIOS (LEMBRANÇAS E BRINQUEDOS DA ÍSIS - 33 ITENS ÚNICOS)
# ==============================================================================
random_loot_pool = [
    # --- Tier 1
    # Aprimoramentos 
    Item(id="laco_de_fita", name="Laço de Fita Cor-de-Rosa", description="A lembrança de se sentir bonita e confiante te dá um pequeno reforço.", item_type="aprimoramento", tier=1, stat_boosts={"attack_power": 1}),
    Item(id="presilha_de_borboleta", name="Presilha de Cabelo de Borboleta", description="Um presente da mamãe. A lembrança do cuidado dela te torna mais resistente.", item_type="aprimoramento", tier=1, stat_boosts={"max_health": 5}),
    Item(id="gibi_antigo", name="Gibi Antigo de Super-Heroína", description="A inspiração da sua heroína favorita te dá um pouco mais de coragem.", item_type="aprimoramento", tier=1, stat_boosts={"attack_power": 1}),
    Item(id="borracha_cheirosa", name="Borracha com Cheiro de Tutti-Frutti", description="Apagar os erros no caderno te ensinou a ser mais resiliente.", item_type="aprimoramento", tier=1, stat_boosts={"max_health": 5}),
    Item(id="apontador_bichinho", name="Apontador em Forma de Joaninha", description="A paciência para apontar um lápis te dá mais foco.", item_type="aprimoramento", tier=1, stat_boosts={"max_energy": 5}),
    Item(id="ioio_simples", name="Ioiô Simples que Brilha", description="A prática para fazer o ioiô 'dormir' afiou seus reflexos.", item_type="aprimoramento", tier=1, stat_boosts={"defense_power": 1}),

    # Consumíveis 
    Item(id="caixinha_de_suco_uva", name="Caixinha de Suco de Uva", description="Uma memória doce do lanche da tarde. Restaura 15 de energia.", item_type="consumivel", tier=1, effect="restore_energy", amount=15),
    Item(id="biscoito_de_chocolate", name="Biscoito de Chocolate com Estrelinhas", description="Um lanche especial que a mamãe fazia. Restaura 20 de vida.", item_type="consumivel", tier=1, effect="heal", amount=20),
    Item(id="garrafinha_de_agua", name="Garrafinha de Água com Adesivos", description="Hidratação básica para continuar a aventura. Restaura 10 de vida.", item_type="consumivel", tier=1, effect="heal", amount=10),
    Item(id="bala_de_goma", name="Bala de Goma de Ursinho", description="Um pequeno doce que te conforta. Restaura 15 de vida.", item_type="consumivel", tier=1, effect="heal", amount=15),
    Item(id="pirulito_colorido", name="Pirulito Colorido em Espiral", description="Uma explosão de açúcar que te deixa mais alerta. Restaura 10 de energia.", item_type="consumivel", tier=1, effect="restore_energy", amount=10),
    Item(id="gelatina_colorida", name="Potinho de Gelatina Colorida", description="Uma sobremesa divertida que te dá um pouco de ânimo. Restaura 20 de vida.", item_type="consumivel", tier=1, effect="heal", amount=20),
    Item(id="barra_de_cereal", name="Barra de Cereal de Frutas", description="Um lanche rápido para recuperar o fôlego. Restaura 15 de energia.", item_type="consumivel", tier=1, effect="restore_energy", amount=15),
    
    # Sucata 
    Item(id="livro_de_colorir", name="Página de um Livro de Colorir", description="Um desenho de um castelo, pintado com capricho.", item_type="sucata", tier=1, value=8),
    Item(id="massinha_de_modelar", name="Massa de Modelar Ressecada", description="Já foi macia. Hoje é só um bloco duro.", item_type="sucata", tier=1, value=12),
    Item(id="adesivo_desgastado", name="Cartela de Adesivos Usada", description="Sobraram poucos adesivos que perderam a cola.", item_type="sucata", tier=1, value=8),
    Item(id="tampinha_de_garrafa", name="Tampinha de Refrigerante", description="Uma daquelas que você colecionava.", item_type="sucata", tier=1, value=12),
    Item(id="concha_do_mar", name="Concha do Mar", description="Uma lembrança de um dia na praia. Como ela veio parar aqui?", item_type="sucata", tier=1, value=15),
    Item(id="ingresso_de_cinema", name="Ingresso de Cinema Rasgado", description="A lembrança de um filme de desenho animado que você assistiu com seus pais.", item_type="sucata", tier=1, value=10),
    Item(id="carrinho_de_brinquedo", name="Carrinho de Brinquedo sem Roda", description="Um carrinho de metal que já viu dias melhores.", item_type="sucata", tier=1, value=10),

    # --- Tier 2
    Item(id="diario_com_cadeado", name="Diário com Cadeado de Coração", description="Seus segredos te ajudam a focar sua energia.", item_type="aprimoramento", tier=2, stat_boosts={"max_energy": 10}),
    Item(id="fantasia_de_princesa", name="Pedaço de uma Fantasia de Princesa", description="Ser a heroína da sua própria história te deixa mais valente.", item_type="aprimoramento", tier=2, stat_boosts={"defense_power": 2}),
    Item(id="kit_de_maquiagem_infantil", name="Kit de Maquiagem de Brinquedo", description="A lembrança de brincar de se arrumar como a mamãe te ensina a se proteger.", item_type="aprimoramento", tier=2, stat_boosts={"defense_power": 2}),
    Item(id="casa_de_boneca_em_miniatura", name="Casa de Boneca em Miniatura", description="Criar histórias nesse pequeno mundo expande sua imaginação.", item_type="aprimoramento", tier=2, stat_boosts={"max_energy": 10}),
    Item(id="colar_de_micangas", name="Colar de Miçangas Coloridas", description="A concentração para fazer este colar afia sua mente e seus ataques.", item_type="aprimoramento", tier=2, stat_boosts={"attack_power": 2}),
    Item(id="estojo_escolar", name="Estojo Escolar de Gatinho", description="Dentro, há um 'lanchinho de emergência' bem guardado.", item_type="consumivel", tier=2, effect="heal", amount=50),
    Item(id="lancheira_termica", name="Lancheira Térmica de Unicórnio", description="Dentro, uma bebida especial te revigora completamente.", item_type="consumivel", tier=2, effect="restore_energy", amount=40),
    Item(id="patins_antigo", name="Patins Antigo de 4 Rodas", description="A memória de aprender a se equilibrar te deixa mais ágil e evasiva.", item_type="aprimoramento", tier=2, stat_boosts={"defense_power": 2}),
    Item(id="caixinha_de_musica_especial", name="Caixinha de Música Especial", description="Toca a canção de ninar que seus pais cantavam. A melodia expande sua capacidade de usar habilidades.", item_type="aprimoramento", tier=2, stat_boosts={"skill_slots": 1}),

    # --- Tier 3 
    Item(id="relogio_quebrado_do_papai", name="Relógio Quebrado do Papai", description="É o relógio do papai. Está parado, mas a lembrança da força dele te inspira.", item_type="aprimoramento", tier=3, stat_boosts={"attack_power": 3, "defense_power": 3}),
    Item(id="perola_do_colar_da_mamae", name="Pérola do Colar da Mamãe", description="Uma pérola do colar preferido da mamãe. A lembrança do sorriso dela te enche de determinação.", item_type="aprimoramento", tier=3, stat_boosts={"max_health": 25, "max_energy": 10}),
    Item(id="pulseira_da_amizade", name="Pulseira da Amizade", description="A lembrança de uma conexão verdadeira te dá um poder inesperado.", item_type="aprimoramento", tier=3, stat_boosts={"skill_slots": 1}),
    Item(id="desenho_emoldurado", name="Desenho Emoldurado da Família", description="O desenho que ficava na geladeira. É a memória mais poderosa de todas.", item_type="aprimoramento", tier=3, stat_boosts={"attack_power": 2, "max_health": 10}),
]