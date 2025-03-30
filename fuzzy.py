from fuzzywuzzy import fuzz, process

def fuzzy_search(query, choices, threshold=70):
    """
    Realiza uma pesquisa fuzzy na lista de escolhas.
    
    :param query: Termo de pesquisa inserido pelo usuário.
    :param choices: Lista de palavras disponíveis para pesquisa.
    :param threshold: Mínimo de similaridade para considerar uma correspondência.
    :return: Lista de correspondências com pontuação acima do threshold.
    """
    results = process.extract(query, choices)
    return [match for match in results if match[1] >= threshold]

# Exemplo de palavras disponíveis para pesquisa
data = [
    "Minecraft", "Grand Theft Auto V", "Tetris", "Wii Sports", "PUBG", "Super Mario Bros.", "Overwatch", 
    "League of Legends", "Fortnite", "The Legend of Zelda: Breath of the Wild", "Call of Duty: Warzone", 
    "Animal Crossing: New Horizons", "Roblox", "Among Us", "Counter-Strike: Global Offensive", "Apex Legends", 
    "Red Dead Redemption 2", "The Witcher 3: Wild Hunt", "Genshin Impact", "Call of Duty: Modern Warfare", 
    "Super Smash Bros. Ultimate", "Dota 2", "Cyberpunk 2077", "Halo Infinite", "Resident Evil Village", 
    "Elden Ring", "Battlefield 2042", "God of War (2018)", "Fall Guys", "FIFA 23", "NBA 2K23", "Valorant", 
    "Destiny 2", "Monster Hunter: World", "Hearthstone", "ARK: Survival Evolved", "The Sims 4", "Dead by Daylight", 
    "Rocket League", "World of Warcraft", "Horizon Forbidden West", "Madden NFL 23", "Rust", "Far Cry 6", 
    "Final Fantasy XIV", "The Elder Scrolls V: Skyrim", "Sea of Thieves", "Forza Horizon 5", "Splatoon 3", 
    "Diablo III", "Assassin's Creed Valhalla", "Ghost of Tsushima", "Pokémon GO", "Pokémon Scarlet and Violet", 
    "Super Mario Odyssey", "Metroid Dread", "Kirby and the Forgotten Land", "Fire Emblem: Three Houses", 
    "Mario Kart 8 Deluxe", "Persona 5 Royal", "Bloodborne", "Dark Souls III", "Sekiro: Shadows Die Twice", 
    "Nioh 2", "Hollow Knight", "Celeste", "Stardew Valley", "Terraria", "Cuphead", "Undertale", "INSIDE", 
    "Little Nightmares", "It Takes Two", "A Way Out", "The Last of Us Part II", "The Last of Us Remastered", 
    "Uncharted 4: A Thief's End", "Spider-Man (PS4/PS5)", "Spider-Man: Miles Morales", "Control", "Death Stranding", 
    "BioShock Infinite", "Portal 2", "Half-Life: Alyx", "DOOM Eternal", "XCOM 2", "Civilization VI", 
    "Age of Empires IV", "Total War: Warhammer III", "StarCraft II", "F1 22", "Gran Turismo 7", 
    "Need for Speed: Heat", "Shadow of the Tomb Raider", "NieR: Automata", "Yakuza: Like a Dragon", "Dragon Ball FighterZ", 
    "Mortal Kombat 11", "Street Fighter V", "Guilty Gear -Strive-"
]

# Entrada do usuário
query = input("Digite o termo de pesquisa: ")

# Executa a pesquisa fuzzy
matches = fuzzy_search(query, data)

# Exibe os resultados
if matches:
    print("Resultados encontrados:")
    for match in matches:
        print(f"{match[0]} (Similaridade: {match[1]}%)")
else:
    print("Nenhuma correspondência encontrada.")