# DESIGN/alfa_dungeon.md

This little project is to build a very simple dungeon. The most basic spec is 
mentioned in the [../README.md] doc where it says this:

> Use evmenu knowledge to build menu based combat in a linear Dungeon
>> Dungeon choices are only continue or backtrack
>> Dungeon feature is only monster or nothing
>> Try to include Monster combat too.


Based on just that spec (remember to update the readme if this changes) we can 
deduce the following additional requirements:

1. a means of entering the dungeon. 
  1. either and object or a room with the "enter dungeon" command set attached.
1. a dungeon menu central loop 
  1. continue
  2. backtrack
1. a means of marking progress, location,
  1. room numbers
  2. levels
1. a combat system
  1. monster hp, attack value etc.


# Build plan

[x] enter dungeon command
[x] enter dungeon object
    The entrance is attached to this, otherwise the you can enter the dungeon
    from any place. It's all in your head. Okay now this is the spec, silly!
[ ] dungeon room and level counters... initialized with enter and stored in char.
[ ] first node is dungeon entrance
[ ] dungeon loop menu
[ ] dungeon combat program
