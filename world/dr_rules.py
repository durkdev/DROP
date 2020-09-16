# dr_rules.py

'''
Dungeon Rip-off Rules. This contains most if not all DR rules. From
character stats and abilities to treasure tables etc. Mostly dicts I
bet. I forget but I'm sure it will come back to me.  If it gets too
long snap off some of the tables to their own modules.
'''

ABILITIES = {  # short key: (long name, help desc, other information?)
        "STR": ["strength", "Gives +1 to hit, damage and open doors."],
        "INT": ["intelligence", "Allows use of magic scrolls, +1 to" +
                "avoid getting lost."],
        "WIS": ["wisdom", "Gives +1 to saving throws; religious scrolls"],
        "DEX": ["dexterity", "Bonus +1 to armour class and sneak rolld"],
        "CON": ["constitution", "Bonus +1 starting hitpoint and +1 every" +
                "other level."],
        "CHA": ["charisma", "You're more likeable. Bonus to reaction rolls" +
                " and you may hire two mooks instead of one"]
        }

CLASSES = {  # short key: (long name, help desc, ??? )
    "ROA": ["rip-off artist", "Basically a  nobody but bonus lucky" +
            "rolls and increasing bonus to running away from monsters"],
    "THF": ["thief", "Can't use heavy weapons or armout but is better at " +
            "sneaking, can sneak attack and pick locks."],
    "WAR": ["warrior", "Trained fighter, can wear heavy armour. Gains " +
            "attack bonuses with levels."]
        }
