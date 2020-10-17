# Honour Project Planning Page
In which we sketch out the big picture and then break it into little chunks for working on in a sporadic but systematic manner. 

# Vision
A fantasy MUD where players role-play characters who seek fame and fortune by
exploring dungeons. Role-play is facilitated by the "honour system". The honour
system allows players to make up rules as they go along but also holds them
accountable to those rules by interrogating and recording the reasoning behind
the players personal rulings. These records become stories and narratives that 
are shared with and reviewed by other players. 

# Definitions
I notice I'm making up terms here so I should start defining them.

ruling: a decision by a player about rules of the game that gets recorded

journal:  a "black box" system that records the players actions and rulings

gazette: a system that publishes the adventures of other player characters so 
    that they can be reviewed and discussed


# Play proposition
This is what it should be like to play the minimal implementation of this game
now: 
1. Log in through the webclient. Create a player character by choosing a name.
2. Arrive in a lobby room.
    1. help/intro information
    2. read the "gazette"
    3. enter the dungeon
3. There is an exit from the lobby to enter a dungeon. 
4. The Dungeon is a series of rooms, some contain objects. Some objects are
   obstacles. The player can navigate through the rooms, pick up or interact
   with the objects and engage with obstacles. The final "obstacle" is the
   task of returning home. (To the lobby for now)
5. Interactions:
    An obstacle is interacted with when the player runs a command. 
6. Game arc:
    So basic game play will be about going on an adventure into the dungeon and
    then returning to tell the tale. Loot and experience and progression are at
    the discretion of the player when they choose to apply a status or condition
    effect to their own character.

# Minimum Requirements
0. A prompt to guide players when making rulings
0. A journal to record these rulings
0. A publishing system to share the resulting narratives with others.
0. An actual dungeon complete with obstacles and encounters to play in.

# Evennia Implementation Plan
Start by relying as much as possible on the default objects, characters,
commands to make life easier. Implement each of the minimum requirements.

## The Prompt
The player can launch the prompt at will to begin an interaction with a dungeon
object. Optionally the game can launch the prompt to force a player to begin an
interaction. I see the prompt as being an EvMenu. 

### command
key engage

aliases: attack; solve; escape etc.

Have lots of aliases so that the command makes sense vis-a-vis a particular
object

usage:  engage <target>

The target is an object in the dungeon.  If not, Prompt will warn the player
(in case of a typo) but  .... no (see feature creeper). Instead just suggest the
player can create the object if they wish (and if they have builder permission).

### menu



## The Journal
The Journal get updated by the prompt and optionally the player can add to it
manually (possibly through another menu or editor command). But there should be
no substantial editing of the journal. It is more of a black box or flight
recorder.

Players can and should be able to review their journal and perhaps even annotate
it for fun and entertainment.

## The Gazette
The Gazette is the system that makes some or all contents of players journals
available to other players. It will have some heavy lifting to present journals
in an interesting manner. (Likely trimming and formatting the journal content).

## The Dungeon
The simplest dungeon I think, is merely a series of rooms containing zero or
more objects. Objects can represent anything from monsters, to treasure, to
traps or more exotic dungeon features. For proof of concept the dungeon can be
built using Evennia default commands. 

### Persistance and change
Do players actually affect the dungeon or its objects as part of their
adventure? If they do, this will require some kind of system. With default
Evennia commands they can pick up unlocked objects. 

# Feature Creepers
This is a dump for cool features that are not part of the minimal specification

## Calling "engage" command on non-existent objects
After warngin the player give the player the option of simply creating an
object.(Call the create command)


## Dungeon building tools
So the DROP+ project began as a random dungeon generation tool, but ideally I
would like a tool that facilitates easy building by players.

## Build by ruling
Instead of rulings only applying to the player's journal, rulings could create
properties and aspects of other game objects that will persist. For example a
player might decide they died while dueling a goblin because it had poisoned its
dagger. That goblin object persists in game, but now "poisoned dagger" becomes
one of its attributes. Future players who encounter that object will be informed
at the right moment about this.  

The rulings could apply to rooms and traps as well. 

Finally, certain rulings could have implications for all objects of a certain
type (even yet to be created). Perhaps in the above example, the player could
say this goblin had a poisoned dagger... because thats typical for goblins.
This should result in all future goblins having at least a chance of spawning
with a poisoned dagger in their possession. 

Passive rulings building: Players aren't explicitly told they are building but
when a new player meets a goblin object they can be told during the prompt that
past players have enountered poisoned daggers on these things. The player then
can decide if the current goblin shares that feature.
