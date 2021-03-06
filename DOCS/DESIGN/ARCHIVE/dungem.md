github.com/durkdev/DROP/blob/master/DOCS/DESIGN/dungem.md

# Needs: concerns raised during work on other projects
- the dungeon character project reminds me I need a way of keeping everything inside a dungem inside that dungem. For example,
right now the drchar command runs a menu that creates a DRC but it exists at large in the DB and is not connected to any particular
dungem.  Same goes for "town" and related rooms. None of them are confined within the  dungem object at this time.

Consider how far we got with this during the vessel project in Mutiny.

## Talk through the requirement
Creating a dungem should create an object with a couple of default values, ie. described as a gem, has a certain cmd_set.
(Review Mutiny's vessel objects to see how we restricted object cmd_sets to characters inside them.)
On creation it gets a unique name or tag. (how to enforce this? Just use #dbref or something else?)
Inside it should have a build town command that creates rooms that are tagged as in the zone of this dungem's unique name. 
In other words everything created by internal dungem build commands or by procedural generation (in shops or in the dungeon) 
will get tagged.

Is there a way to define the "create object" function and have every create in the gem use it?  


# Helpful advice from discord Kovitikus:

<pre>
KovitikusToday at 9:32 PM
Or, in at_before_move, it should have the destination passed along. So just check if destination != obj.home: return
[9:32 PM]
That would probably be better.
[9:33 PM]
Or you can restrict it to zone, cause you want a larger area of movement, but not cross pollinated zones?
[9:33 PM]
Tag all objects in a certain zone with the zone tag and simply check if the destination has the same tag as the object being moved.
[9:33 PM]
If not then abort the move.

j3bToday at 9:34 PM
Also if I delete a "world" I want all of its contents to leave at the same time.   Yes, can I dynamically create a zone, as part of the at_creation of my "world object"

KovitikusToday at 9:34 PM
So then write some cleanup handler for getting rid of a world. It should be easy. Search for all objects with that zone tag then delete them.

j3bToday at 9:35 PM
Okay yes I like this.  Zone are my answer for now. I will meditate upon this. Thanks!
</pre>

See: https://github.com/evennia/evennia/wiki/Zones


