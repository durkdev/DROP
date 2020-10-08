# Tables Introduction 
A random dungeon adventure generating system intuitively consists of lots of tables. This project itself is inspired by a set of tables originally 
published in the 1st Edition Advanced Dungeons & Dragons, Dungeon Masters Guide ("DMG"). So I'm using this document to think out loud about tables. In a previous
version of this project, Apendixie. I produced a simulacrum of the DMG tables.  I've imported that table to this project without a clear idea yet if, 
or how I want to use it. [tables.py](world/tables.py) tables.py currently has one dictionary  or "book" of tables named GYGAX. 

## Digression about  GYGAX
GYGAX is as or more complex than I think I can tolerate. It is a dictionary of about 20 arrays (tables) which contain table headings
 and tuples of results. It might be more reasonable to make every table a separate data structure.  There is no particular reason that they have to be combined. 
Each structure would have to follow a strict rubric to ensure it played properly with whichever commands utilized it.  But that's true either way.

GYGAX succeeds in implementing some of the DMG game but does not contain the tricks, traps, treasure or monster results.  So I'm at a crossroads (I've been here
before) where I need to decide whether to build on GYGAX and attempt to implement the game as imagined in the DMG, or to start fresh with my own tables, custom 
built to match a game of my own vision. 

The answer I think, right now, is that it is time to branch out.  For one thing, Dungeon Robber has already done the job of faithfully implementing the DMG vision
in a mix of homage and irony.  I really don't need to do that all over again.  I know one of my motivations has been to re-create Dungeon Robber really just to let
myself play it in a post adobe flash world. But I think I can get over that. Okay so digression has succeeded.

##  

# 


