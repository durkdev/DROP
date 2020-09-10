# dungeon.py
"""
This could be the entire dungeon delving menu system. It can be placed in
a room near a town to obtain some of the town and shop benefits. 

To properly meet the spec, the menu should actual contain its own town but 
I'm going to delay that to the end.
"""

# enter dungeon command
""" 
Based on the "shop" command from the tutorial. 
A command that opens a menu
"""

from evennia import Command

class CmdEnterDungeon(Command):
    """
    Enter the dungeon. 

    Usage:
      enter the dungeon

    This will imediately take you to entry room (room 0) of the 
    first level of the dungeon. It initializes your position in the 
    dungeon at 1/0. 
    """

    key = "enter the dungeon"
    aliases = ("go to pandemonium", "take a walk on the wild side")

    def func(self):
        "Start the dungeon Evmenu Instance"
        evmenu.EvMenu(self.caller, "world.dungeon",
                      startnode="dn_entrance")

# create commandset for this one command
""" 
But I wont use it for now as I'm adding the cmd to the 
default character command set
"""
from evennia import CmdSet

class DungeonCmdSet(CmdSet):
    def at_cmdset_creation(self):
        self.add(CmdEnterDungeon())


