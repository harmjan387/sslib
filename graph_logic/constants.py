from collections import defaultdict
from typing import NewType, Dict, Callable

EXTENDED_ITEM_NAME = NewType("EXTENDED_ITEM_NAME", str)
EIN = EXTENDED_ITEM_NAME

sep = " - "

EVERYTHING = EIN("Everything")

MAX_HINTS = 32

# Logic options, runtime requirements

OPEN_THUNDERHEAD_OPTION = EIN("Open Thunderhead option")
OPEN_ET_OPTION = EIN("Open ET option")
OPEN_LMF_OPTION = EIN("Open LMF option")
LMF_NODES_ON_OPTION = EIN("LMF Nodes On option")
RANDOMIZED_BEEDLE_OPTION = EIN("Randomized Beedle option")
GONDO_UPGRADES_ON_OPTION = EIN("Gondo Upgrades On option")
HERO_MODE = EIN("Hero-mode")
NO_BIT_CRASHES = EIN("No BiT crashes")

GOT_OPENING_REQUIREMENT = EIN("GoT Opening Requirement")
GOT_RAISING_REQUIREMENT = EIN("GoT Raising Requirement")
HORDE_DOOR_REQUIREMENT = EIN("Horde Door Requirement")

BEEDLE_STALL_ACCESS = EIN("Beedle Stall Access Token")
MEDIUM_PURCHASES = EIN("Medium Purchases Token")
EXPENSIVE_PURCHASES = EIN("Expensive Purchases Token")
MAY_GET_n_CRYSTALS = lambda n: EIN(f"May Get {n} Crystals Token")

CRYSTAL_THRESHOLDS = [5, 10, 30, 40, 50, 70, 80]

LOGIC_OPTIONS = dict.fromkeys(
    [
        OPEN_THUNDERHEAD_OPTION,
        OPEN_ET_OPTION,
        OPEN_LMF_OPTION,
        LMF_NODES_ON_OPTION,
        RANDOMIZED_BEEDLE_OPTION,
        GONDO_UPGRADES_ON_OPTION,
        HERO_MODE,
        NO_BIT_CRASHES,
        GOT_OPENING_REQUIREMENT,
        GOT_RAISING_REQUIREMENT,
        HORDE_DOOR_REQUIREMENT,
        BEEDLE_STALL_ACCESS,
        MEDIUM_PURCHASES,
        EXPENSIVE_PURCHASES,
    ]
    + [MAY_GET_n_CRYSTALS(n) for n in CRYSTAL_THRESHOLDS]
)

# Locations


def with_sep_full(pre: str, loc: str) -> EXTENDED_ITEM_NAME:
    if "\\" not in loc:
        return EIN(pre + "\\" + loc)
    return EIN(loc)


make_day = lambda s: EIN(s + "_DAY")
make_night = lambda s: EIN(s + "_NIGHT")


def entrance_of_exit(exit):
    if exit.endswith(" Exit") or exit.endswith("\\Exit"):
        return exit.replace("Exit", "Entrance")
    if "Exit to " in exit:
        return exit.replace("Exit to", "Entrance from")
    raise ValueError("No pattern")


SV = "Skyview"
ET = "Earth Temple"
LMF = "Lanayru Mining Facility"
AC = "Ancient Cistern"
SSH = "Sandship"
FS = "Fire Sanctuary"
SK = "Sky Keep"

REGULAR_DUNGEONS = [SV, ET, LMF, AC, SSH, FS]
ALL_DUNGEONS = REGULAR_DUNGEONS + [SK]

SKYLOFT_TRIAL = "Skyloft Trial"
FARON_TRIAL = "Faron Trial"
ELDIN_TRIAL = "Eldin Trial"
LANAYRU_TRIAL = "Lanayru Trial"

ALL_TRIALS = [SKYLOFT_TRIAL, FARON_TRIAL, ELDIN_TRIAL, LANAYRU_TRIAL]

# Items

ITEM_COUNTS: Dict[str, int] = defaultdict(lambda: 1)


def number(name: str, index: int) -> EXTENDED_ITEM_NAME:
    if index >= ITEM_COUNTS[name]:
        raise ValueError("Index too high")
    if ITEM_COUNTS[name] == 1:
        return EIN(name)
    return EIN(f"{name} #{index}")


def strip_item_number(item: EXTENDED_ITEM_NAME) -> str:
    if "#" not in item:
        return item
    return item[: item.index("#") - 1]


def group(name: str, count: int) -> Dict[EXTENDED_ITEM_NAME, None]:
    ITEM_COUNTS[name] = count
    return {number(name, i): None for i in range(count)}


HINT = "Hint"
HINTS = group(HINT, MAX_HINTS)

BOMB_BAG = EIN("Bomb Bag")
GUST_BELLOWS = EIN("Gust Bellows")
WHIP = EIN("Whip")
CLAWSHOTS = EIN("Clawshots")
WATER_SCALE = EIN("Water Scale")
FIRESHIELD_EARRINGS = EIN("Fireshield Earrings")
SEA_CHART = EIN("Sea Chart")
EMERALD_TABLET = EIN("Emerald Tablet")
RUBY_TABLET = EIN("Ruby Tablet")
AMBER_TABLET = EIN("Amber Tablet")
STONE_OF_TRIALS = EIN("Stone of Trials")

BABY_RATTLE = EIN("Baby Rattle")
CAWLINS_LETTER = EIN("Cawlin's Letter")
HORNED_COLOSSUS_BEETLE = EIN("Horned Colossus Beetle")
GODDESS_HARP = EIN("Goddess Harp")
BALLAD_OF_THE_GODDESS = EIN("Ballad of the Goddess")
FARORES_COURAGE = EIN("Farore's Courage")
NAYRUS_WISDOM = EIN("Nayru's Wisdom")
DINS_POWER = EIN("Din's Power")
FARON_SOTH_PART = EIN("Faron Song of the Hero Part")
ELDIN_SOTH_PART = EIN("Eldin Song of the Hero Part")
LANAYRU_SOTH_PART = EIN("Lanayru Song of the Hero Part")
SPIRAL_CHARGE = EIN("Spiral Charge")
LIFE_TREE_SEEDLING = EIN("Life Tree Seedling")
LIFE_TREE_FRUIT = EIN("Life Tree Fruit")
TRIFORCE_OF_COURAGE = EIN("Triforce of Courage")
TRIFORCE_OF_WISDOM = EIN("Triforce of Wisdom")
TRIFORCE_OF_POWER = EIN("Triforce of Power")

GRATITUDE_CRYSTAL_PACK = "Gratitude Crystal Pack"
GRATITUDE_CRYSTAL = "Gratitude Crystal"
PROGRESSIVE_SWORD = "Progressive Sword"
PROGRESSIVE_MITTS = "Progressive Mitts"
PROGRESSIVE_SLINGSHOT = "Progressive Slingshot"
PROGRESSIVE_BEETLE = "Progressive Beetle"
PROGRESSIVE_BOW = "Progressive Bow"
PROGRESSIVE_BUG_NET = "Progressive Bug Net"
PROGRESSIVE_POUCH = "Progressive Pouch"
KEY_PIECE = "Key Piece"
EMPTY_BOTTLE = "Empty Bottle"
PROGRESSIVE_WALLET = "Progressive Wallet"
EXTRA_WALLET = "Extra Wallet"

GRATITUDE_CRYSTAL_PACKS = group(GRATITUDE_CRYSTAL_PACK, 13)
GRATITUDE_CRYSTALS = group(GRATITUDE_CRYSTAL, 15)
NUMBER_SWORDS = 6
PROGRESSIVE_SWORDS = group(PROGRESSIVE_SWORD, NUMBER_SWORDS)
PROGRESSIVE_MITTS_ALL = group(PROGRESSIVE_MITTS, 2)
PROGRESSIVE_SLINGSHOTS = group(PROGRESSIVE_SLINGSHOT, 2)
PROGRESSIVE_BEETLES = group(PROGRESSIVE_BEETLE, 4)
PROGRESSIVE_BOWS = group(PROGRESSIVE_BOW, 3)
PROGRESSIVE_BUG_NETS = group(PROGRESSIVE_BUG_NET, 2)
PROGRESSIVE_POUCHES = group(PROGRESSIVE_POUCH, 5)
KEY_PIECES = group(KEY_PIECE, 5)
EMPTY_BOTTLES = group(EMPTY_BOTTLE, 5)
PROGRESSIVE_WALLETS = group(PROGRESSIVE_WALLET, 4)
EXTRA_WALLETS = group(EXTRA_WALLET, 3)

small_key = lambda d: d + " Small Key"
SV_SMALL_KEY = small_key(SV)
ET_SMALL_KEY = small_key(ET)
LMF_SMALL_KEY = small_key(LMF)
AC_SMALL_KEY = small_key(AC)
SSH_SMALL_KEY = small_key(SSH)
FS_SMALL_KEY = small_key(FS)
SK_SMALL_KEY = small_key(SK)

boss_key = lambda d: d + " Boss Key"
SV_BOSS_KEY = boss_key(SV)
ET_BOSS_KEY = boss_key(ET)
LMF_BOSS_KEY = boss_key(LMF)
AC_BOSS_KEY = boss_key(AC)
SSH_BOSS_KEY = boss_key(SSH)
FS_BOSS_KEY = boss_key(FS)
SK_BOSS_KEY = boss_key(SK)

dungeon_map = lambda d: EIN(d + " Map")
SV_MAP = dungeon_map(SV)
ET_MAP = dungeon_map(ET)
LMF_MAP = dungeon_map(LMF)
AC_MAP = dungeon_map(AC)
SSH_MAP = dungeon_map(SSH)
FS_MAP = dungeon_map(FS)
SK_MAP = dungeon_map(SK)

CAVES_KEY = EIN("Lanayru Caves Key")

SV_SMALL_KEYS = group(SV_SMALL_KEY, 2)
ET_SMALL_KEYS = group(ET_SMALL_KEY, 0)
LMF_SMALL_KEYS = group(LMF_SMALL_KEY, 1)
AC_SMALL_KEYS = group(AC_SMALL_KEY, 2)
SSH_SMALL_KEYS = group(SSH_SMALL_KEY, 2)
FS_SMALL_KEYS = group(FS_SMALL_KEY, 3)
SK_SMALL_KEYS = group(SK_SMALL_KEY, 1)

SV_BOSS_KEYS = group(SV_BOSS_KEY, 1)
ET_BOSS_KEYS = group(ET_BOSS_KEY, 1)
LMF_BOSS_KEYS = group(LMF_BOSS_KEY, 1)
AC_BOSS_KEYS = group(AC_BOSS_KEY, 1)
SSH_BOSS_KEYS = group(SSH_BOSS_KEY, 1)
FS_BOSS_KEYS = group(FS_BOSS_KEY, 1)
SK_BOSS_KEYS = group(SK_BOSS_KEY, 0)

WOODEN_SHIELD = EIN("Wooden Shield")
HYLIAN_SHIELD = EIN("Hylian Shield")
CURSED_MEDAL = EIN("Cursed Medal")
TREASURE_MEDAL = EIN("Treasure Medal")
POTION_MEDAL = EIN("Potion Medal")
SMALL_SEED_SATCHEL = EIN("Small Seed Satchel")
SMALL_BOMB_BAG = EIN("Small Bomb Bag")
SMALL_QUIVER = EIN("Small Quiver")
BUG_MEDAL = EIN("Bug Medal")

HEART_MEDAL = "Heart Medal"
RUPEE_MEDAL = "Rupee Medal"
HEART_PIECE = "Heart Piece"
HEART_CONTAINER = "Heart Container"
LIFE_MEDAL = "Life Medal"

HEART_MEDALS = group(HEART_MEDAL, 2)
RUPEE_MEDALS = group(RUPEE_MEDAL, 2)
HEART_PIECES = group(HEART_PIECE, 24)
HEART_CONTAINERS = group(HEART_CONTAINER, 6)
LIFE_MEDALS = group(LIFE_MEDAL, 2)

GREEN_RUPEE = "Green Rupee"
BLUE_RUPEE = "Blue Rupee"
RED_RUPEE = "Red Rupee"
SILVER_RUPEE = "Silver Rupee"
GOLD_RUPEE = "Gold Rupee"
SEMI_RARE_TREASURE = "Semi Rare Treasure"
GOLDEN_SKULL = "Golden Skull"
RARE_TREASURE = "Rare Treasure"
EVIL_CRYSTAL = "Evil Crystal"
ELDIN_ORE = "Eldin Ore"
GODDESS_PLUME = "Goddess Plume"
DUSK_RELIC = "Dusk Relic"
TUMBLEWEED = "Tumbleweed"
FIVE_BOMBS = "5 Bombs"

GREEN_RUPEES = group(GREEN_RUPEE, 3)
BLUE_RUPEES = group(BLUE_RUPEE, 11)
RED_RUPEES = group(RED_RUPEE, 42)
SILVER_RUPEES = group(SILVER_RUPEE, 22)
GOLD_RUPEES = group(GOLD_RUPEE, 11)
SEMI_RARE_TREASURES = group(SEMI_RARE_TREASURE, 10)
GOLDEN_SKULLS = group(GOLDEN_SKULL, 1)
RARE_TREASURES = group(RARE_TREASURE, 12)
EVIL_CRYSTALS = group(EVIL_CRYSTAL, 2)
ELDIN_ORES = group(ELDIN_ORE, 2)
GODDESS_PLUMES = group(GODDESS_PLUME, 1)
DUSK_RELICS = group(DUSK_RELIC, 1)
TUMBLEWEEDS = group(TUMBLEWEED, 1)
FIVE_BOMBS_GROUP = group(FIVE_BOMBS, 1)


RUPOOR = "Rupoor"

PROGRESS_ITEMS = (
    dict.fromkeys(
        [
            BOMB_BAG,
            GUST_BELLOWS,
            WHIP,
            CLAWSHOTS,
            WATER_SCALE,
            FIRESHIELD_EARRINGS,
            SEA_CHART,
            EMERALD_TABLET,
            RUBY_TABLET,
            AMBER_TABLET,
            STONE_OF_TRIALS,
            BABY_RATTLE,
            CAWLINS_LETTER,
            HORNED_COLOSSUS_BEETLE,
            GODDESS_HARP,
            BALLAD_OF_THE_GODDESS,
            FARORES_COURAGE,
            NAYRUS_WISDOM,
            DINS_POWER,
            FARON_SOTH_PART,
            ELDIN_SOTH_PART,
            LANAYRU_SOTH_PART,
            SPIRAL_CHARGE,
            # LIFE_TREE_SEEDLING,
            LIFE_TREE_FRUIT,
            TRIFORCE_OF_COURAGE,
            TRIFORCE_OF_WISDOM,
            TRIFORCE_OF_POWER,
        ]
    )
    | GRATITUDE_CRYSTAL_PACKS
    | GRATITUDE_CRYSTALS
    | PROGRESSIVE_SWORDS
    | PROGRESSIVE_MITTS_ALL
    | PROGRESSIVE_SLINGSHOTS
    | PROGRESSIVE_BEETLES
    | PROGRESSIVE_BOWS
    | PROGRESSIVE_BUG_NETS
    | PROGRESSIVE_POUCHES
    | KEY_PIECES
    | EMPTY_BOTTLES
    | PROGRESSIVE_WALLETS
    | EXTRA_WALLETS
)

NONPROGRESS_ITEMS = (
    dict.fromkeys(
        [
            WOODEN_SHIELD,
            HYLIAN_SHIELD,
            CURSED_MEDAL,
            TREASURE_MEDAL,
            POTION_MEDAL,
            SMALL_SEED_SATCHEL,
            SMALL_BOMB_BAG,
            SMALL_QUIVER,
            BUG_MEDAL,
        ]
    )
    | HEART_MEDALS
    | RUPEE_MEDALS
    | HEART_PIECES
    | HEART_CONTAINERS
    | LIFE_MEDALS
)

CONSUMABLE_ITEMS = (
    GREEN_RUPEES
    | BLUE_RUPEES
    | RED_RUPEES
    | SILVER_RUPEES
    | GOLD_RUPEES
    | SEMI_RARE_TREASURES
    | GOLDEN_SKULLS
    | RARE_TREASURES
    | EVIL_CRYSTALS
    | ELDIN_ORES
    | GODDESS_PLUMES
    | DUSK_RELICS
    | TUMBLEWEEDS
    | FIVE_BOMBS_GROUP
)

# Once all the items that have a fixed number per seed are used up, this list is used.
# Unlike the other lists, this one does not have items removed from it as they are placed.
# The number of each item in this list is instead its weighting relative to the other items in the list.
DUPLICABLE_ITEMS = dict.fromkeys(
    [
        BLUE_RUPEE,
        RED_RUPEE,
        SEMI_RARE_TREASURE,
        RARE_TREASURE,
    ]
)
DUPLICABLE_COUNTERPROGRESS_ITEMS = {RUPOOR: None}

# note: Lanayru Caves is technically not a dungeon, but has to be treated as such for non key sanity
SMALL_KEYS = (
    SV_SMALL_KEYS
    | ET_SMALL_KEYS
    | LMF_SMALL_KEYS
    | AC_SMALL_KEYS
    | SSH_SMALL_KEYS
    | FS_SMALL_KEYS
    | SK_SMALL_KEYS
    | {CAVES_KEY: None}
)
BOSS_KEYS = (
    SV_BOSS_KEYS
    | ET_BOSS_KEYS
    | LMF_BOSS_KEYS
    | AC_BOSS_KEYS
    | SSH_BOSS_KEYS
    | FS_BOSS_KEYS
    | SK_BOSS_KEYS
)
MAPS = dict.fromkeys([SV_MAP, ET_MAP, LMF_MAP, AC_MAP, SSH_MAP, FS_MAP, SK_MAP])

INVENTORY_ITEMS = (
    PROGRESS_ITEMS
    | NONPROGRESS_ITEMS
    | CONSUMABLE_ITEMS
    | SMALL_KEYS
    | BOSS_KEYS
    | MAPS
)

ALL_ITEM_NAMES = INVENTORY_ITEMS | DUPLICABLE_ITEMS | DUPLICABLE_COUNTERPROGRESS_ITEMS
RAW_ITEM_NAMES = dict.fromkeys(strip_item_number(EIN(k)) for k in ALL_ITEM_NAMES)

TABLETS = [EMERALD_TABLET, RUBY_TABLET, AMBER_TABLET]

SWORD_COUNT = {
    "Swordless": 0,
    "Practice Sword": 1,
    "Goddess Sword": 2,
    "Goddess Longsword": 3,
    "Goddess White Sword": 4,
    "Master Sword": 5,
    "True Master Sword": 6,
}


str_main_exit = "Main Exit"
DUNGEON_MAIN_EXITS = {
    SV: SV + sep + str_main_exit,
    ET: ET + sep + str_main_exit,
    LMF: LMF + sep + str_main_exit,
    AC: AC + sep + str_main_exit,
    SSH: SSH + sep + str_main_exit,
    FS: FS + sep + str_main_exit,
    SK: SK + sep + "First Room - Bottom Exit",
}

DUNGEON_FINAL_CHECK = {
    SV: SV + sep + RUBY_TABLET,
    ET: ET + sep + AMBER_TABLET,
    LMF: LMF + sep + GODDESS_HARP,
    AC: AC + sep + "Farore's Flame",
    SSH: SSH + sep + "Nayru's Flame",
    FS: FS + sep + "Din's Flame",
}

GHIRAHIM_I = "Ghirahim 1"
SCALDERA = "Scaldera"
MOLDARACH = "Moldarach"
KOLOKTOS = "Koloktos"
TENTALUS = "Tentalus"
GHIRAHIM_II = "Ghirahim 2"
DEMISE = "Defeat Demise"

GOALS = [GHIRAHIM_I, SCALDERA, MOLDARACH, KOLOKTOS, TENTALUS, GHIRAHIM_II]
ALL_GOALS = GOALS + [DEMISE]

DUNGEON_GOALS = {
    SV: GHIRAHIM_I,
    ET: SCALDERA,
    LMF: MOLDARACH,
    AC: KOLOKTOS,
    SSH: TENTALUS,
    FS: GHIRAHIM_II,
}

GOAL_CHECKS = {
    GHIRAHIM_I: DUNGEON_FINAL_CHECK[SV],
    SCALDERA: DUNGEON_FINAL_CHECK[ET],
    MOLDARACH: DUNGEON_FINAL_CHECK[LMF],
    KOLOKTOS: DUNGEON_FINAL_CHECK[AC],
    TENTALUS: DUNGEON_FINAL_CHECK[SSH],
    GHIRAHIM_II: DUNGEON_FINAL_CHECK[FS],
    DEMISE: DEMISE,
}


START = "Start"
START_ITEM = EIN("Start Item")
UNPLACED_ITEM = EIN("Unplaced Item")
SONG_IMPA_CHECK = "Sealed Grounds - Song from Impa"
COMPLETE_TRIFORCE = "Complete Triforce"

trick: Callable[[str], str] = lambda s: s + " Trick"

UPPER_SKYLOFT = "Upper Skyloft"
SKYLOFT_CENTRAL = "Skyloft Central"
SKYLOFT_VILLAGE = "Skyloft Village"
BATREAUX = "Batreaux"
BEEDLE = "Beedle"

SKY = "Sky"
THUNDERHEAD = "Thunderhead"

SEALED_GROUNDS = "Sealed Grounds"
FARON_WOODS = "Faron Woods"
LAKE_FLORIA = "Lake Floria"

ELDIN_VOLCANO = "Eldin Volcano"
MOGMA_TURF = "Mogma Turf"
VOLCANO_SUMMIT = "Volcano Summit"

LANAYRU_MINES = "Lanayru Mines"
LANAYRU_DESERT = "Lanayru Desert"
LANAYRU_CAVES = "Lanayru Caves"
LANAYRU_GORGE = "Lanayru Gorge"
SAND_SEA = "Sand Sea"

SKYLOFT_SILENT_REALM = "Skyloft Silent Realm"
FARON_SILENT_REALM = "Faron Silent Realm"
LANAYRU_SILENT_REALM = "Lanayru Silent Realm"
ELDIN_SILENT_REALM = "Eldin Silent Realm"

ALL_HINT_REGIONS = dict.fromkeys(
    [
        UPPER_SKYLOFT,
        SKYLOFT_CENTRAL,
        SKYLOFT_VILLAGE,
        BATREAUX,
        BEEDLE,
        SKY,
        THUNDERHEAD,
        SEALED_GROUNDS,
        FARON_WOODS,
        LAKE_FLORIA,
        ELDIN_VOLCANO,
        MOGMA_TURF,
        VOLCANO_SUMMIT,
        LANAYRU_MINES,
        LANAYRU_DESERT,
        LANAYRU_CAVES,
        LANAYRU_GORGE,
        SAND_SEA,
        SV,
        ET,
        LMF,
        AC,
        SSH,
        FS,
        SK,
        SKYLOFT_SILENT_REALM,
        FARON_SILENT_REALM,
        LANAYRU_SILENT_REALM,
        ELDIN_SILENT_REALM,
    ]
)

# Retro-compatibility

DUNGEON_OVERWORLD_EXITS: dict[str, list[str]] = {
    SV: ["Deep Woods - Exit to Skyview Temple"],
    ET: ["Eldin Volcano - Exit to Earth Temple"],
    LMF: ["Lanayru Desert - Exit to Lanayru Mining Facility"],
    AC: ["Floria Waterfall - Exit to Ancient Cistern"],
    SSH: ["Sand Sea - Sandship Dock Exit", "Sand Sea Docks - Exit to Sandship"],
    FS: ["Outside Fire Sanctuary - Exit to Fire Sanctuary"],
    SK: ["Skyloft - Exit to Sky Keep"],
}

LMF_SECOND_EXIT = LMF + sep + "Great Hall" + sep + "Exit to Temple of Time"

TRIAL_EXITS: dict[str, str] = {
    SKYLOFT_TRIAL: "Skyloft - Trial Gate Exit",
    FARON_TRIAL: "Faron Woods - Trial Gate Exit",
    ELDIN_TRIAL: "Eldin Volcano - Trial Gate Exit",
    LANAYRU_TRIAL: "Lanayru Desert - Trial Gate Exit",
}

TRIALS: dict[str, str] = {
    SKYLOFT_TRIAL: "Skyloft - Silent Realm - Exit",
    FARON_TRIAL: "Faron - Silent Realm - Exit",
    ELDIN_TRIAL: "Eldin - Silent Realm - Exit",
    LANAYRU_TRIAL: "Lanayru - Silent Realm - Exit",
}

TRIAL_CHECKS: dict[str, str] = {
    SKYLOFT_TRIAL: "Skyloft - Silent Realm - Stone of Trials",
    FARON_TRIAL: "Faron - Silent Realm - Water Scale",
    ELDIN_TRIAL: "Eldin - Silent Realm - Fireshield Earrings",
    LANAYRU_TRIAL: "Lanayru - Silent Realm - Clawshots",
}

TRIAL_CHECKS_REV = {v: k for k, v in TRIAL_CHECKS.items()}


RUPEE_CHECKS = [
    "Skyloft - Waterfall Cave - Rupee in Crawlspace",
    "Great Tree - Top - Rupee on North Branch",
    "Great Tree - Top - Rupee on West Branch",
    "Faron Woods - Rupee on Platform near Floria Door",
    "Faron Woods - Rupee on Hollow Tree Root",
    "Faron Woods - Rupee on Hollow Tree Branch",
    "Lake Floria - Rupee under Central Boulder",
    "Lake Floria - Right Rupee behind Northwest Boulder",
    "Lake Floria - Left Rupee behind Northwest Boulder",
    "Lake Floria - Rupee behind Southwest Boulder",
    "Floria Waterfall - Rupee on High Ledge",
    "Eldin Volcano - Entry - Rupee on Ledge",
    "Eldin Volcano - First Room - Rupee behind Bombable Wall",
    "Eldin Volcano - First Room - Rupee in Crawlspace",
    "Eldin Volcano - Southeast Rupee above Mogma Turf Entrance",
    "Eldin Volcano - North Rupee above Mogma Turf Entrance",
    "Eldin Volcano - Near Thrill Digger Cave - Left Rupee behind Bombable Wall",
    "Eldin Volcano - Near Thrill Digger Cave - Right Rupee behind Bombable Wall",
    "Ancient Harbour - Rupee on First Pillar",
    "Ancient Harbour - Left Rupee on Entrance Crown",
    "Ancient Harbour - Right Rupee on Entrance Crown",
    "Pirate Stronghold - Rupee on West Sea Pillar",
    "Pirate Stronghold - Rupee on East Sea Pillar",
    "Pirate Stronghold - Rupee on Bird Statue Pillar or Nose",
    "Skyview - Second Hub - Rupee in Southeast Tunnel",
    "Skyview - Second Hub - Rupee in Southwest Tunnel",
    "Skyview - Second Hub - Rupee in East Tunnel",
    "Skyview - Spring - Rupee on Pillar",
    "Earth Temple - Rupee above Drawbridge",
    "Earth Temple - Rupee in Lava Tunnel",
    "Ancient Cistern - East Part - Rupee in Main Tunnel",
    "Ancient Cistern - East Part - Rupee in Cubby",
    "Ancient Cistern - East Part - Third Rupee in Short Tunnel",
    "Ancient Cistern - East Part - Second Rupee in Short Tunnel",
    "Ancient Cistern - East Part - First Rupee in Short Tunnel",
    # "Ancient Cistern - After Gutters - Rupee under Lilypad",
    "Ancient Cistern - Rupee in Left Hand",
    "Ancient Cistern - Rupee in Right Hand",
    "Sky Keep - Fire Sanctuary Room - Rupee in Alcove",
]

QUICK_BEETLE_CHECKS = [
    "Ancient Harbour - Left Rupee on Entrance Crown",
    "Ancient Harbour - Right Rupee on Entrance Crown",
    "Pirate Stronghold - Rupee on West Sea Pillar",
    "Pirate Stronghold - Rupee on East Sea Pillar",
]

GONDO_ITEMS = {
    number(PROGRESSIVE_BEETLE, 2),
    number(PROGRESSIVE_BEETLE, 3),
    number(PROGRESSIVE_SLINGSHOT, 1),
    number(PROGRESSIVE_BOW, 1),
    number(PROGRESSIVE_BOW, 2),
    number(PROGRESSIVE_BUG_NET, 1),
}
