# dr_commands.py

"""
These are the commands needed for running the Dungeon Rip-off mini game.
Many of these commands will be attached to DR objects and rooms.
"""
##########################################################
#                                                        #
#   Character Creation - for Dungeon Rip-off Artists     #
#                                                        #
##########################################################

from evennia.utils import evmenu
from evennia import Command

class MakeDRC(Command):  # Make a Dungeon Rip-off Char
    """
    Create a new Rip-off character. By openning a menu.
    """
    key = "drchar"
    aliases = ["newdr", "newd"]
    lock = "cmd:all()"
    help_category = "Dungeon Rip-off"

    def func(self):
        "open the drc menu"
        evmenu.EvMenu(self.caller,
                      "commands.dr_commands", # menu nodes here.
                      startnode="mn_dr_start")

def mn_dr_start(caller):
    "start node of dr character creation menu"

    live_chars = caller.location.db.lives
    # a list of current characters in play in this dungen

    text = "Welcome to the dungem Dungeon Sim"
    if  live_chars:
        text += "  These are the living characters:" \
                " choose 1-%i to live their lives." % len(live_chars) \
    else:
        text += "  No living character here."
    text += "choose [n]ew to create a new life\n" \
            "or [q]uit to quit."
    
    options = []
    for char in live_chars:
        # add an option for each live character
        options.append({"desc": "%s" % live_char.key),
                       {"exec": "enter_dungeon()"}

    options.append({"key": ("new", "n"),
                    "goto": "mn_stat"}           



def mn_stat(caller, raw_string, **kwargs):
    "choose the bonus stat"
    text = """
        You can choose a bonus stat for your charactter.
        All other stats will be average but this one 
        will be slightly better than average.
        Click on stat number to read a description
        """
    options = []
       #TODO: put in ability scores 



###################################################### 
# open a menu to ask the player to make some choices #
######################################################
# Name

# Bonus Stat

# Class

#####################################################
# Initialize a new drc with these values and def.   #
#####################################################

from typeclases.dr_characters import DR_char

def newdrc(self):  # 
    "initialize a typeclass dr_character"
    


#####################################################
# Display chacter sheet                             #
#####################################################


