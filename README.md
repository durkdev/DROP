# Welcome to Dungeon Rip-off Plus+!

We will have FISHING!! Tricks, traps and deadly Rock Paper Scissors dueling.
Stay tuned.  Also there is some discussion in the [Wiki](https://github.com/durkdev/DROP/wiki).  Should we continue to use the Wiki for idea development?

For a detailed specification see files in the [DOCS/DESIGN](./DOCS/DESIGN/).

Ideas for design directions as well as creative content for the future game can all be found in [DOCS/CREATIVE](./DOCS/CREATIVE)

Testing server online at: http://18.189.9.99:4021/


# Current Todo list. 
With more than one person working, lets just use the readme to link to individual projects.
## j3b's current project is:
[alfa dungeon](DOCS/DESIGN/alfa_dungeon.md) an implementation of dungeon rip-off.


# DR features and long term goals, maybe.
The following features are based on the Dungeon Robber rules. They can be tweaked as we develop.

  1. Character generation command that transforms a regular character into 
rip-off artists.
      1. ability scores
      1. coins, gold, silver, copper, electrum, platinum
      1. gems etc
      1. inventory
  2. Equipment wielding - to allow player to select which equipment is active
      1. armour
      1. weapons
      1. special items like 10' pole for some reason
  3. Monsters and NPCs
      1. to fight and interact with
  4. Town - shops and services
      1. home
      2. graveyard
      3. hall of infamy
      4. market
      5. tavern

# Past todo's 
(We will probably move these out of this document before it gets too crowded.)
## [X] Create an minimal example EvMenu Dungeon
  A pure instanced Dungeon; see [How to Dungeon](./DOCS/DESIGN/howto_dungeon.md) for an idea of what I'm going for here. 
  This will require me to re-learn evmenu.
  
  1. [X] Complete the NPC shop evmenu tutorial. (Finished for this stage.)
      1. [x] tweak the NPC shop to be usable in the game for buying gear and selling off dungeon loot.
      2. [x] add a "sell" command that turns the players inventory into a stockroom and adds an offer price to each item.
        1. [x] evemenu of personal inventory [done]
        2. [x] sell value is half of buy cost
  1. [ ] Use evmenu knowledge to build menu based combat in a linear Dungeon
      1. [x] Dungeon choices are only continue or backtrack
      2. [x] Dungeon feature is only monster or nothing
 As a first step learning process this has succeeded. I think I will close this branch and return to the drawing board before trying to implement a more functional version of the dungeon.
 
  Thoughts: this would be a good place to stop and consider whether the purely instanced menu based Dungeon is good enough or whether to switch to semi-permanent dungeon generation.


# Evennia Links
From here on you might want to look at one of the beginner tutorials:
http://github.com/evennia/evennia/wiki/Tutorials.

Evennia's documentation is here:
https://github.com/evennia/evennia/wiki.

Enjoy!
