# Welcome to Dungeon Rip-off Plus+! (thats a double plus)

We will have FISHING!! Tricks, traps and deadly Rock Paper Scissor dueling.
Stay tuned.  Also there is some discussion in the [Wiki](https://github.com/durkdev/DROP/wiki).  Should we continue to use the Wiki for idea development?

For a detailed specification see files in the [DOCS/DESIGN](./DOCS/DESIGN/).

Ideas for design directions as well as creative content for the future game can all be found in [DOCS/CREATIVE](./DOCS/CREATIVE)

Testing server online at: http://18.189.9.99:4021/

# Current project/to do.
## j3b4
Just writing vision and design specs.  Also hide away old stuff.


# Vision
The goal of DROP+ is to explore randomly generated dungeon adventures together or alone. Writers will
create exquisite little adventure elements and vignettes which the player can experience through 
exploration and chance. 

## Content Creation
Writers should be able to continue develop content in tiny modular chunks without worrying about the big 
picture.  Kind of like dropping adventure cards into an ever expanding deck. 

## Game mechanics and rules
The game mechanics should provide generic methods of interacting with the content with optional on-the-fly
customization. That is the player should be able to approach obstacles in the dungeon crawl through tradional
hack-n-slash methods like attacking with found weapons, using potions and scroll, sneaking away etc.  These 
actions will be well supported by code.  Adventure elements should have enough features to interact with this
system. 

### Example:
<pre>
You enter a room and find an orc. It sneers and draws a sword.
>> Attack orc.
You attack the ord with your wielded weapon.  Hit and do lethal damage killing it.  (All this is calculated
by the game engine.)  You murder the orc and obtain loot from its corpse.
</pre>

However there should also be another optional system of creative power gaming allowing players to dictate 
how they overcome or succumb to obstacles by creating new attributes and conditions on the fly in response to 
the content they encounter.  These attributes and conditions are persistent. 

### Example:
<pre>
You enter a room and note that it is completely occupied by sentient green slime. 
>powergame: "I can levitate at will.  I activate this power and float through the room just out of 
reach of the noxious slime"
What is your resulting condition?
>Levitating.
You now have the condition "levitating" which will be added to your status until you manually turn it off. 
It will be up to the player to decide how this condition affects them in future encounters.
</pre>

## Honor (*and shame*) system.
The only check on powergaming is that all powergame exploits... or perhaps all exploits are publicly shared to 
all players in a news log.  All other players will read about your encounters and what conditions you invented.
If your powergaming offends the standards of play accepted by other players you will find yourself embarrased.
If it entertains your fellow players you will gain renown. 

# Shared random adventures
The MUD will allow one or more than one player to experience adventures together.  This will use a dynamic room 
system and a group/follow system to help players stay together if they wish.  Combat and other forms or obstacle
resolution should best be turn based to make sure power gaming narratives are somewhat coherent. 

## Shared powergaming. 
Using the powergame command, players can impose or propose conditions on other players. Consent structures and
boundaries can be adjusted to taste.


# Evennia Links
From here on you might want to look at one of the beginner tutorials:
http://github.com/evennia/evennia/wiki/Tutorials.

Evennia's documentation is here:
https://github.com/evennia/evennia/wiki.

Enjoy!
