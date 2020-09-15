# Dungeon Rip-off character (DRC)

A DRC is a character object that should live inside a dungem object.
A regular mud character can puppet a DRC and "live another
life" inside the "dungem". A DRC can die in the dungeon interred in
the cemetary. Their epitaph will be preserved in the
archives. A DRC can also be retired to the Town in the dungem and
their acheivements will be recorded on a wall of fame.

## "Dungem" aspects of DRC
DRC's are stored in dungems and are not exclusively owned by player
characters or accounts. Any PC inside a dungem has access to all the 
living DRCs in that gem. *This implies the existence of a menu of
existing DRCs.* It should be impossible for a DRC to escape a dungem
though perhaps that rule could be transgressed for interesting 
reasons in the future.

See [dungem.md](dungem.md) spec for more details about dungems. 

## DRC Properties
DRC's have the following properties in addition to the base evennia 
character object properties:
 1. name
 2. level
 3. experience points (XP)
 4. ability scores (strength, intelligence, wisdom, dexterity
    constitution, and charisma)
 5. maximum and current hit points
 6. armour class
 7. saving throw(s)
 8. sneak bonus
 9. attack bonus

DRC's can also have attached items and item based conditions:
 1. general inventory
 2. equipped inventory
 3. containers (for carrying treasure)
 4. coins: copper, silver, gold, electrum, platinum,
 5. gems and jewelry
 6. a 'burden' rating derived from their carried items, container, and 
    possibly affected by strength and constitution

DRC's can have professions or character classes:
 1. rip-off artist (the default class)
 2. thief
 3. warrior
 4. priest
 5. mage

DRC's also have a ledger or logbook which records events during
their dungeon delving carrer. Upon the DRC's death, the contents
of the log is stored in the archives. 

Similar to the log, the DRC object store information about the character
current status conditions in the dungeon:
 1. dungeon level
 2. dungeon room
 3. panicked
 4. lost

## DRC Code projects
