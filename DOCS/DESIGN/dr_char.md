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

## DRC Code Step by Step

 1. [X] dr_char typeclass 
 Modify the default character object with 6 ability scores and all features above.
 2. [ ] drchar command
 Trigger an evmenu that offers the player a list of live DRCs in the gem that they can puppet. Or
 allowes them to create a new DRC. It would then gather player input for bonus ability, character class, 
 and name. Then store that in a temp object. Then confirm for the player and spawn that object in the db.
 It should be stored in the dungem object so that players activating the gem can puppet the DRC.
   + In order to list the live DRC... I need to learn how to store a list of character objects in an objects' db
   + Before I do that, however, I'll need to make some DRC objects.
 3.  [ ] making a DRC
   + Ask user to pick a stat to get a bonus.  Stats are stored world.dr_rules.py
   + Then pick a profession
   + pick a name and you're done
   + [ ] behind the scenes picking ability scores stats and class should generate some other stats
     + [ ] base AC, max HP
     + [ ] attack and sneak bonus
   + This creates a new DRC object base on the DR typeclass.
 4. [X] play as a DRC
   Solving this involves learning how to call the puppet_character function from within my DR command. Ths works now.
 5. DRC clean up.
   + in the game DRC's are subject to permadeath.  Might as well build this soon.
   + create a test command "die" to use for cleaning up indiviudal test chars.
   + delete the DB object... but add to a graveyard file.
   + create a "retire" command as well... archive the char for possible re-use later or monumentalize?
   
