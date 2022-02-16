from .weapons import weapons


classes = {
    "assassin": {
        "hit die": "d8",
        "ability minimums": {"strength": 12, "dexterity": 12, "intelligence": 9},
        "bonus xp minimums": {"strength": 15, "dexterity": 15, "intelligence": 15},
        "levels": {
            1: {"min xp": 0, "proficiencies": 3},
            10: {"base attack bonus": 6, "min xp": 300000},
            11: {"min xp": 425000},
            12: {"base attack bonus": 7, "min xp": 575000},
            13: {"min xp": 750000, "proficiencies": 6},
            14: {"base attack bonus": 8, "min xp": 1000000},
            15: {"base attack bonus": 9, "min xp": 1250000},
            16: {"min xp": 1500000},
            17: {"base attack bonus": 10, "min xp": 1750000, "proficiencies": 7},
            18: {"min xp": 2000000},
            19: {"base attack bonus": 11, "min xp": 2250000},
            2: {"base attack bonus": 1, "min xp": 1500},
            20: {"base attack bonus": 12, "min xp": 2500000},
            3: {"min xp": 3000},
            4: {"base attack bonus": 2, "min xp": 6000},
            5: {"base attack bonus": 3, "min xp": 12000, "proficiencies": 4},
            6: {"min xp": 25000},
            7: {"base attack bonus": 4, "min xp": 50000},
            8: {"min xp": 100000},
            9: {"base attack bonus": 5, "min xp": 200000, "proficiencies": 5},
            "nonproficiency penalty": -2,
            "weapon choices": set(weapons),
            "armor choices": {"gambeson", "leather", "coat of plates"},
        },
    },
    "cleric": {
        "hit die": "d8",
        "ability minimums": {"wisdom": 9},
        "bonus xp minimums": {"wisdom": 16},
        "levels": {
            1: {"min xp": 0, "proficiencies": 2},
            10: {"min xp": 450000},
            11: {"base attack bonus": 5, "min xp": 675000},
            12: {"min xp": 900000},
            13: {"base attack bonus": 6, "min xp": 1125000, "proficiencies": 5},
            14: {"min xp": 1350000},
            15: {"base attack bonus": 7, "min xp": 1575000},
            16: {"min xp": 1800000},
            17: {"base attack bonus": 8, "min xp": 2025000, "proficiencies": 6},
            18: {"min xp": 2250000},
            19: {"min xp": 2475000},
            2: {"min xp": 1500},
            20: {"min xp": 2700000},
            3: {"base attack bonus": 1, "min xp": 3000},
            4: {"min xp": 6000},
            5: {"base attack bonus": 2, "min xp": 13000, "proficiencies": 3},
            6: {"min xp": 27500},
            7: {"base attack bonus": 3, "min xp": 55000},
            8: {"min xp": 110000},
            9: {"base attack bonus": 4, "min xp": 225000, "proficiencies": 4},
        },
        "nonproficiency penalty": -3,
        "weapon choices": {
            "bolas",
            "club",
            "quarterstaff",
            "goedendag",
            "flail",
            "sling",
            "sling staff",
            "mace",
            "warhammer",
        },
    },
    "druid": {
        "hit die": "d8",
        "ability minimums": {"wisdom": 12, "charisma": 12},
        "bonus xp minimums": {"wisdom": 15, "charisma": 15},
        "levels": {
            1: {"min xp": 0, "proficiencies": 2},
            10: {"min xp": 150000},
            11: {"base attack bonus": 5, "min xp": 240000, "proficiencies": 4},
            12: {"min xp": 360000},
            13: {"base attack bonus": 6, "min xp": 540000},
            14: {"min xp": 780000},
            15: {"base attack bonus": 7, "min xp": 1080000},
            16: {"min xp": 1440000, "proficiencies": 5},
            17: {"base attack bonus": 8, "min xp": 1800000},
            18: {"min xp": 2160000},
            19: {"min xp": 2520000},
            2: {"min xp": 2400},
            20: {"min xp": 2880000},
            3: {"base attack bonus": 1, "min xp": 4800},
            4: {"min xp": 9000},
            5: {"base attack bonus": 2, "min xp": 15000},
            6: {"min xp": 24000, "proficiencies": 3},
            7: {"base attack bonus": 3, "min xp": 42000},
            8: {"min xp": 72000},
            9: {"base attack bonus": 4, "min xp": 108000},
        },
        "nonproficiency penalty": -4,
        "weapon choices": {
            "bolas",
            "club",
            "dagger",
            "quarterstaff",
            "javelin",
            "scimitar",
            "spear",
            "sling",
            "sling staff",
            "mace",
            "dart",
            "warhammer",
        },
    },
    "fighter": {
        "hit die": "d10",
        "ability minimums": {"strength": 12, "constitution": 9},
        "bonus xp minimums": {
            "strength": 15
        },  # note that despite other ability scores with minimums, only str needs to be higher than minimum to gain bonus xp
        "levels": {
            1: {"base attack bonus": 1, "min xp": 0, "proficiencies": 4},
            10: {"base attack bonus": 10, "min xp": 500000, "proficiencies": 7},
            11: {"base attack bonus": 11, "min xp": 750000},
            12: {"base attack bonus": 12, "min xp": 1000000},
            13: {"base attack bonus": 13, "min xp": 1250000, "proficiencies": 8},
            14: {"base attack bonus": 14, "min xp": 1500000},
            15: {"base attack bonus": 15, "min xp": 1750000},
            16: {"base attack bonus": 16, "min xp": 2000000, "proficiencies": 9},
            17: {"min xp": 2250000},
            18: {"min xp": 2500000},
            19: {"min xp": 2750000, "proficiencies": 10},
            2: {"base attack bonus": 2, "min xp": 2000},
            20: {"min xp": 3000000},
            3: {"base attack bonus": 3, "min xp": 4000},
            4: {"base attack bonus": 4, "min xp": 8000, "proficiencies": 5},
            5: {"base attack bonus": 5, "min xp": 18000},
            6: {"base attack bonus": 6, "min xp": 35000},
            7: {"base attack bonus": 7, "min xp": 70000, "proficiencies": 6},
            8: {"base attack bonus": 8, "min xp": 125000},
            9: {"base attack bonus": 9, "min xp": 250000},
        },
        "nonproficiency penalty": -2,
        "weapon choices": set(weapons),
    },
    "illusionist": {
        "hit die": "d4",
        "ability minimums": {"dexterity": 9, "intelligence": 12},
        "bonus xp minimums": {"intelligence": 15},
        "levels": {
            1: {"min xp": 0, "proficiencies": 1},
            10: {"min xp": 220000},
            11: {"min xp": 440000},
            12: {"min xp": 660000},
            13: {"base attack bonus": 3, "min xp": 880000, "proficiencies": 3},
            14: {"min xp": 1100000},
            15: {"min xp": 1320000},
            16: {"min xp": 1540000},
            17: {"base attack bonus": 4, "min xp": 1760000},
            18: {"min xp": 1980000},
            19: {"min xp": 2200000, "proficiencies": 4},
            2: {"min xp": 2250},
            20: {"min xp": 2420000},
            3: {"min xp": 4500},
            4: {"min xp": 9000},
            5: {"base attack bonus": 1, "min xp": 18000},
            6: {"min xp": 35000},
            7: {"min xp": 60000, "proficiencies": 2},
            8: {"min xp": 95000},
            9: {"base attack bonus": 2, "min xp": 145000},
        },
        "nonproficiency penalty": -5,
        "weapon choices": {
            "dagger",
            "dart",
            "club",
            "quarterstaff",
            "sling",
        },
    },
    "mage": {
        "hit die": "d4",
        "ability minimums": {"intelligence": 9},
        "bonus xp minimums": {"intelligence": 16},
        "levels": {
            1: {"min xp": 0, "proficiencies": 1},
            10: {"min xp": 250000},
            11: {"min xp": 375000},
            12: {"min xp": 750000},
            13: {"base attack bonus": 3, "min xp": 1125000, "proficiencies": 3},
            14: {"min xp": 1500000},
            15: {"min xp": 1875000},
            16: {"min xp": 2250000},
            17: {"base attack bonus": 4, "min xp": 2625000},
            18: {"min xp": 3000000},
            19: {"min xp": 3375000, "proficiencies": 4},
            2: {"min xp": 2500},
            20: {"min xp": 3750000},
            3: {"min xp": 5000},
            4: {"min xp": 10000},
            5: {"base attack bonus": 1, "min xp": 22500},
            6: {"min xp": 40000},
            7: {"min xp": 60000, "proficiencies": 2},
            8: {"min xp": 90000},
            9: {"base attack bonus": 2, "min xp": 135000},
        },
        "nonproficiency penalty": -5,
        "weapon choices": {
            "dagger",
            "club",
            "dart",
            "quarterstaff",
            "sling",
        },
    },
    "monk": {
        "hit die": "d6",
        "ability minimums": {
            "strength": 12,
            "constitution": 12,
            "dexterity": 12,
            "wisdom": 12,
        },
        "bonus xp minimums": {
            "strength": 15,
            "constitution": 15,
            "dexterity": 15,
            "wisdom": 15,
        },
        "levels": {
            1: {"min xp": 0, "proficiencies": 2},
            10: {"min xp": 500000},
            11: {"base attack bonus": 5, "min xp": 700000, "proficiencies": 7},
            12: {"min xp": 950000},
            13: {"base attack bonus": 6, "min xp": 1250000, "proficiencies": 8},
            14: {"min xp": 1750000},
            15: {"base attack bonus": 7, "min xp": 2250000, "proficiencies": 9},
            16: {"min xp": 2750000},
            17: {"base attack bonus": 8, "min xp": 3250000, "proficiencies": 10},
            18: {"min xp": 3750000},
            19: {"min xp": 4250000},
            2: {"min xp": 2250},
            20: {"min xp": 4750000},
            3: {"base attack bonus": 1, "min xp": 4750, "proficiencies": 3},
            4: {"min xp": 10000},
            5: {"base attack bonus": 2, "min xp": 22500, "proficiencies": 4},
            6: {"min xp": 47500},
            7: {"base attack bonus": 3, "min xp": 98000, "proficiencies": 5},
            8: {"min xp": 200000},
            9: {"base attack bonus": 4, "min xp": 350000, "proficiencies": 6},
        },
        "nonproficiency penalty": -3,
    },
    "paladin": {
        "hit die": "d10",
        "ability minimums": {
            "strength": 9,
            "constitution": 9,
            "wisdom": 9,
            "charisma": 12,
        },
        "bonus xp minimums": {"strength": 15, "wisdom": 15, "charisma": 15},
        "levels": {
            1: {"base attack bonus": 1, "min xp": 0, "proficiencies": 3},
            10: {"base attack bonus": 10, "min xp": 700000, "proficiencies": 6},
            11: {"base attack bonus": 11, "min xp": 1050000},
            12: {"base attack bonus": 12, "min xp": 1400000},
            13: {"base attack bonus": 13, "min xp": 1750000, "proficiencies": 7},
            14: {"base attack bonus": 14, "min xp": 2100000},
            15: {"base attack bonus": 15, "min xp": 2450000},
            16: {"base attack bonus": 16, "min xp": 2800000, "proficiencies": 8},
            17: {"min xp": 3150000},
            18: {"min xp": 3500000},
            19: {"min xp": 3850000, "proficiencies": 9},
            2: {"base attack bonus": 2, "min xp": 2750},
            20: {"min xp": 4200000},
            3: {"base attack bonus": 3, "min xp": 5500},
            4: {"base attack bonus": 4, "min xp": 12000, "proficiencies": 4},
            5: {"base attack bonus": 5, "min xp": 24000},
            6: {"base attack bonus": 6, "min xp": 45000},
            7: {"base attack bonus": 7, "min xp": 95000, "proficiencies": 5},
            8: {"base attack bonus": 8, "min xp": 175000},
            9: {"base attack bonus": 9, "min xp": 350000},
        },
        "nonproficiency penalty": -2,
        "weapon choices": set(weapons),
    },
    "ranger": {
        "hit die": "d10",
        "ability minimums": {
            "strength": 12,
            "constitution": 9,
            "wisdom": 9,
            "intelligence": 9,
        },
        "bonus xp minimums": {"strength": 15, "wisdom": 15},
        "levels": {
            1: {"base attack bonus": 1, "min xp": 0, "proficiencies": 3},
            10: {"base attack bonus": 10, "min xp": 325000, "proficiencies": 6},
            11: {"base attack bonus": 11, "min xp": 575000},
            12: {"base attack bonus": 12, "min xp": 875000},
            13: {"base attack bonus": 13, "min xp": 1175000, "proficiencies": 7},
            14: {"base attack bonus": 14, "min xp": 1475000},
            15: {"base attack bonus": 15, "min xp": 1775000},
            16: {"base attack bonus": 16, "min xp": 2075000, "proficiencies": 8},
            17: {"min xp": 2375000},
            18: {"min xp": 2675000},
            19: {"min xp": 2975000, "proficiencies": 9},
            2: {"base attack bonus": 2, "min xp": 2250},
            20: {"min xp": 3275000},
            3: {"base attack bonus": 3, "min xp": 4500},
            4: {"base attack bonus": 4, "min xp": 10000, "proficiencies": 4},
            5: {"base attack bonus": 5, "min xp": 20000},
            6: {"base attack bonus": 6, "min xp": 40000},
            7: {"base attack bonus": 7, "min xp": 90000, "proficiencies": 5},
            8: {"base attack bonus": 8, "min xp": 150000},
            9: {"base attack bonus": 9, "min xp": 225000},
        },
        "nonproficiency penalty": -2,
        "weapon choices": set(weapons),
    },
    "thief": {
        "hit die": "d6",
        "ability minimums": {"dexterity": 9},
        "bonus xp minimums": {"dexterity": 16},
        "levels": {
            1: {"min xp": 0, "proficiencies": 2},
            10: {"min xp": 160000},
            11: {"base attack bonus": 5, "min xp": 220000},
            12: {"min xp": 440000},
            13: {"base attack bonus": 6, "min xp": 660000, "proficiencies": 5},
            14: {"min xp": 880000},
            15: {"base attack bonus": 7, "min xp": 1100000},
            16: {"min xp": 1320000},
            17: {"base attack bonus": 8, "min xp": 1540000, "proficiencies": 6},
            18: {"min xp": 1760000},
            19: {"min xp": 1980000},
            2: {"min xp": 1250},
            20: {"min xp": 2200000},
            3: {"base attack bonus": 1, "min xp": 2500},
            4: {"min xp": 5000},
            5: {"base attack bonus": 2, "min xp": 10000, "proficiencies": 3},
            6: {"min xp": 20000},
            7: {"base attack bonus": 3, "min xp": 42500},
            8: {"min xp": 70000},
            9: {"base attack bonus": 4, "min xp": 110000, "proficiencies": 4},
        },
        "nonproficiency penalty": -3,
        "weapon choices": {
            "bolas",
            "dart",
            "club",
            "dagger",
            "quarterstaff",
            "sling",
            "bow",
            "shortsword",
        },
        "armor choices": {"gambeson", "leather", "coat of plates"},
        "shields": False,
    },
}

#        "bard": {'hit die': 'd6',
#                'weapon choices': []}
# }