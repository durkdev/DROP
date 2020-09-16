# dr_commands.py
'''
These are the commands needed for running the Dungeon Rip-off mini game.
Many of these commands will be attached to DR objects and rooms.
'''
from evennia.utils import evmenu
from evennia import Command
# from typeclasses.dr_characters import DR_char
from world.dr_rules import ABILITIES

##########################################################
#                                                        #
#   Character Creation - for Dungeon Rip-off Artists     #
#                                                        #
##########################################################


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
                      "commands.dr_commands",  # menu nodes here.
                      startnode="mn_dr_start")


def mn_dr_start(caller):
    "start node of dr character creation menu"

    live_chars = caller.location.db.lives
    # a list of current characters in play in this dungen

    text = "***Welcome to the Dungeon Sim***"
    if live_chars:
        text += "  These are the living characters:" \
                " choose 1-%i to live their lives." % len(live_chars)
    else:
        text += " No living character here." \
                " Choose [n]ew to start a new life" \
                " or [q]uit to quit."
    options = []
    if live_chars:
        for char in live_chars:
            # add an option for each live character
            options.append({"desc": "%s" % char.key},
                           {"exec": "enter_dungeon()"})

    options.append({"key": ("new", "n"),
                    "goto": "mn_stat"})
    return text, options


def mn_stat(caller, raw_string, **kwargs):
    "choose the bonus stat"
    text = "You can choose a single bonus ability score. All your abilities" \
           " will be average except this one.\n\n" \
           "Choose a number to enhance that ability."
    options = []
    # TODO: put in ability scores

    for stat in ABILITIES:
        # create an opt from each ability score
        choice = ABILITIES[stat]
        options.append({  # "key": "%s" % stat,
                        "desc": "%s: %s" % (choice[0],
                                            choice[1]),
                        "goto": ("mn_confirmstat", {stat: choice[0]})
                        })
    return text, options


def mn_confirmstat(caller, raw_string, **kwargs):
    "Lets the player decide to lock in this ability bonus"
    choice = ""
    bonus = ""
    for key in kwargs:
        choice = kwargs[key]
        bonus = key
    text = "You chose %s to be your one bonus ability.\n" % choice
    text += "Press 'b' to go back, or [enter]  to continue."

    def save_bonus(caller, bonus):
        #  TODO WHY ISNT THIS WORKING ?
        #  While at it find out what I'm suposed to do instead
        text = "You saved %s as your bonus ability" % bonus
        print(text)
        caller.msg(text)

    options = ({"key": "_default",
                "goto": ("mn_choose_class", {bonus: choice}),
                },
               {"key": ("back", "b", "B"),
                "goto": "mn_stat",
                #  I knot this is deprecated. So what should I do?
                })
    caller.msg("You're trying to set %s as the bonus" % bonus)
    return text, options


def mn_choose_class(caller, raw_string, **kwargs):
    "Maybe you can choose a class.  Depending."
    for key in kwargs:
        choice = kwargs[key]
        #  bonus = key
    text = "You saved %s as your one bonus ability.\n" % choice
    #  TODO: work on classes based on the rules. But first create only
    #  the Dungeon Rip-off class.  The rest can come much later in dev.
    #  I think.
    return text


######################################################
# open a menu to ask the player to make some choices #
######################################################
# Name DONE

# Bonus Stat DONE almost

# Class

#####################################################
# Initialize a new drc with these values and def.   #
#####################################################


def newdrc(self):
    "initialize a typeclass dr_character"


#####################################################
# Display chacter sheet                             #
#####################################################
