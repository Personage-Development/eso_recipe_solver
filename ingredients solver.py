class Ingredient:
    def __init__(self, ing1, ing2, ing3, ing4):
        self.ing1 = ing1
        self.ing2 = ing2
        self.ing3 = ing3
        self.ing4 = ing4

def return_effect(effect_name):
    switch = {
        "Breach": 1,
        "Increase Armor": 2,
        "Protection": 3,
        "Vitality": 4,
        "Restore Stamina": 5,
        "Increase Weapon Power": 6,
        "Ravage Health": 7,
        "Speed": 8,
        "Ravage Magicka": 9,
        "Cowardice": 10,
        "Restore Health": 11,
        "Invisible": 12,
        "Increase Spell Resist": 13,
        "Hindrance": 14,
        "Vulnerability": 15,
        "Defile": 16,
        "Restore Magicka": 17,
        "Uncertainty": 18,
        "Lingering Health": 19,
        "Timidity": 20,
        "Detection": 21,
        "Spell Critical": 22,
        "Heroism": 23,
        "Enervation": 24,
        "Gradual Ravage Health": 25,
        "Unstoppable": 26,
        "Fracture": 27,
        "Weapon Critical": 28,
        "Maim": 29,
        "Entrapment": 30
    }
    return switch.get(effect_name, "Effect not found")

def read_effect(effect_ID):
    switch = {
        1: "Breach",
        2: "Increase Armor",
        3: "Protection",
        4: "Vitality",
        5: "Restore Stamina",
        6: "Increase Weapon Power",
        7: "Ravage Health",
        8: "Speed",
        9: "Ravage Magicka",
        10: "Cowardice",
        11: "Restore Health",
        12: "Invisible",
        13: "Increase Spell Resist",
        14: "Hindrance",
        15: "Vulnerability",
        16: "Defile",
        17: "Restore Magicka",
        18: "Uncertainty",
        19: "Lingering Health",
        20: "Timidity",
        21: "Detection",
        22: "Spell Critical",
        23: "Heroism",
        24: "Enervation",
        25: "Gradual Ravage Health",
        26: "Unstoppable",
        27: "Fracture",
        28: "Weapon Critical",
        29: "Maim",
        30: "Entrapment"
    }
    return switch.get(effect_ID, "Effect ID not found")
