github.com/durkdev/DROP/blob/master/DOCS/DESIGN/dungem.md

# Needs: concerns raised during work on other projects
- the dungeon character project reminds me I need a way of keeping everything inside a dungem inside that dungem. For example,
right now the drchar command runs a menu that creates a DRC but it exists at large in the DB and is not connected to any particular
dungem.  Same goes for "town" and related rooms. None of them are confined within the  dungem object at this time.

Consider how far we got with this during the vessel project in Mutiny.
