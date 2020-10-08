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


# start the menu

from evennia.utils import evmenu
import random

def dn_entrance(caller, raw_string, **kwargs):
    """
    The dungeon always starts here and initializes the character/player's
    position. A dungeon position is a tuple with two integers: level and 
    room.  Room's increase as the player moves farther away from the entrance
    or (on deeper levels) the known stairway up.  Level increases as the player
    descends.
    """
    
    # dn_pos means dungeon position 
    caller.db.dungeon_position = [1, 0]

    text = ("|r*** You're at the dungeon entrance. ***", "I'm not helping you!")
    options = (
        {"key": ("delve", "d", "D"),
         "goto": "dn_delve"},
        {"key": ("escape", "e", "E"),
         "goto": "dn_escape"})

    return text, options

def dn_escape(caller, raw_string, **kwargs):
    text = "You made it out of the dungeon!"
    

def dn_delve(caller, raw_string, **kwargs):
    """
    This is the central exploration loop. 
    """

    # every 'delve' moves the player farther from the entrance increasing room
    # (level, room)
    caller.db.dungeon_position[1] += 1

    text = "You are exploring in room %s of dungeon level %s" % \
        (caller.db.dungeon_position[0], caller.db.dungeon_position[1])

    text += "\nGenerate a result:\n "

    result = random.choice(["monster","nothing"])

    if result == "monster":
        text += "You lucky fool. You have met a |g Monster!"
        options = (
            {"key": ("attack","a", "A"),
             "goto": "dn_fight"},
            {"key": ("run away", "r", "R"),
             "goto": "dn_delve"})
        
    else:
        text += "Hmmm. That's not good.\n jk you're fine. Fine."
        options = (
            {"key": ("delve", "d", "D"),
             "desc": "go deeper into this accursed hole",
             "goto": "dn_delve"},
            {"key": ("backtrack", "b", "B"),
             "desc": "try to retrace your steps and get out of here",
             "goto": "dn_entrance"})

    return text, options

def dn_fight(caller, raw_string, **kwargs):
    """
    This is the start of a fighting looop
    """

    text = "You can win or lose fights. Later perhaps you can retreat and stuff"
    options = (
        {"key": ("win", "w", "W"),
        "goto": "dn_win"},
        {"key": ("lose", "l", "L"),
        "goto": "dn_death"})

    return text, options

def dn_win(caller, raw_string, **kwargs):
    """
    Winning the fight grants you gold.
    """
    text = "You won and get some gold from the monster"
    # not today killer, not today. caller.db.gold += 10
    options = (
        {"key": ("continue", "c", "C"),
        "goto": "dn_delve"})
        # This is so embarrassing
        # I need to figure out how to stream the MUD client instead.
       
    return text, options
