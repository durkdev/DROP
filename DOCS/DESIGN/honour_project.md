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
