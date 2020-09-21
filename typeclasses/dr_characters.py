# dr_characters.py  for defining dungeon rip-off characters
# see ../DESIGN/dr_char.md

from typeclasses.characters import Character

class DR_char(Character):
    """ 
    The DR characters exist in the pocket dungeons (dungems now)
    They come with all the traits and properties needed to play
    in the  mini dungeon and make a life in their town.
    """

    def at_object_creation(self):
        "called at creation or reset (right?)"

        # set persistent attributes
        # name by the way should already be set by the 
        # creation command. 

        # every dr char should be assigned a homegem at start.
        self.db.homegem = None
       
        # level & xp
        self.db.level = 0
        self.db.xp = 0
        self.db.hpmax = 1  # zero means we're dead, but this number
                        # will be improved when the player makes 
                        # some char creation choices. in a menu.
        self.db.hp = 1
         
        # 6 ability scores are only 0 or +1 per dungeon robber
        self.db.strength = 0
        self.db.intelligence = 0
        self.db.wisdom = 0
        self.db.dexterity = 0
        self.db.constitution = 0
        self.db.charisma = 0 
        
        # armour class is a roll under target system, one ornery part 
        # of me is inclined to use the old 1st ord 2nd ed. declining
        # armour class THACO method since it doesn't really matter and
        # feels retro, but either way the base AC is 10 so I can defer 
        # this discussion till later.
        
        self.db.ac = 10

        # base saving throw. Wisdom or Dexterity, and a pole can 
        # improve this. 
        self.db.save = 4    # as per dungeon robber this is out of 6
                            # lower is better since you roll over to
                            # save

        # Bonuses
        self.db.sneak_bonus = 0 # can be improve by dex and thief levels

        self.db.attack_bonus = 0 # by strength and fighter levels.

        # character class. modelled after Dungeon Robber:
        # In the book rules, class can be chosen after
        # level 1. But in the flash game they have to be unlocked by
        # previously retiring characters. I would like to combine
        # both.
        self.db.char_class = "none" # not sure the best initial value

        # ledger or journal which records events automatically.
        # not sure best how to implement so I'll start with an array
        # of strings. 
        self.db.ledger = []

        # Inventory: equipment, gear, treasure etc.
        # so I guess a couple of arrays are best here.
        # wait the built-in character object alreasy has "contents"
        # so lets start with that.

        # For wielding see dr_char spec

        # TODO: learn how to ensure in game that the character only 
        # equips items they actually have, and that they only 
        # equip one of each thing depending on slots
        

        # TODO: complete treasure and eq.
        """
        DRC's can also have attached items and item based conditions:

        general inventory
        equipped inventory
        containers (for carrying treasure)
        coins: copper, silver, gold, electrum, platinum,
        gems and jewelry
        a 'burden' rating derived from their carried items, container, 
        and possibly affected by strength and constitution
        """
