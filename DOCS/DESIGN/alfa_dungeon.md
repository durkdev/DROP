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

* [x] enter dungeon command
* [ ] enter dungeon object: "dungem"
    The entrance is attached to this portable object. Create a typeclass
    for dungems.
    * [ ] this is a new project see below [dungem](#dungem)
* [x] dungeon room and level counters... initialized with enter and stored in char.
* [ ] character creation node
    Decide where this happens. 
* [ ] first node is dungeon entrance
* [ ] dungeon loop menu
* [ ] dungeon combat program

# Dungem
A dungem is a portable gem that contains an alternate universe (AU). By 
default the AU consists of Drowntown and a dungeon. Later this could be
customizable. A dungem has one command attached that lets the holder
transport themselves inside it. (tangent: throwable dungems that capture
anyone they hit like a pokeball/magic lamp) 

Inside the dungem reception area you can choose to create a new life
(character) or resume an existing. I think this will result in puppetting 
a new character object based on a dungem character typeclass. 

I think this brings me to a new TODO: create a dungeon rip-off character.

