# Dungeon Rip-off character (DRC)

A DRC is a character object that should live inside a dungem object.
A regular mud character can puppet a DRC character and "live another
life" inside the dungem. 

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
    1. Okay I think eq. slot and eqpd status is a property of the item
    itself. Test this out later.
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
//Use ndb. variables for this and possibly save them in the menu instance
itself.//

 1. dungeon level
 2. dungeon room
 3. panicked
 4. lost
