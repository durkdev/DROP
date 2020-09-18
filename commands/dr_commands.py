# dr_commands.py
'''
These are the commands needed for running the Dungeon Rip-off mini game.
Many of these commands will be attached to DR objects and rooms.
'''
from evennia.utils import utils, evmenu, create
from evennia import Command
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


def enter_dungeon(caller, **kwargs):
    "Enter the dungeon puppeting the chosen character."
    char = kwargs["char"]
    caller.msg("You want to enter town as %s" % char)
    self.puppet_object(char)
    # TODO just make it work
    return


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
            options.append({"desc": "%s" % char,
                            "goto": ("enter_dungeon", {"char": char})})

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
    caller.ndb._menutree.bonus = bonus
    text = "You chose %s to be your one bonus ability.\n" % choice
    text += "Press 'b' to go back, or [enter]  to continue."

    options = ({"key": "_default",
                "goto": ("mn_choose_prof", {bonus: choice}),
                },
               {"key": ("back", "b", "B"),
                "goto": "mn_stat",
                })
    #  caller.msg("You're trying to set %s as the bonus" % bonus)
    return text, options


def mn_choose_prof(caller, raw_string, **kwargs):
    "Maybe you can choose a profession.  Depending."
    text = "bonus ability score: %s.\n" % caller.ndb._menutree.bonus
    text += "Now choose a class. In future this will be more interesting\n"
    text += "But right now only Rip-off Artist is available.\n"
    text += "So choose it. Choose it now!\n"
    caller.ndb._menutree.prof = "ROA"
    options = ({"key": "_default",
                "goto": "mn_confirm_prof"
                })

    #  TODO: work on classes based on the rules. But first create only
    #  the Dungeon Rip-off class.  The rest can come much later in dev.
    #  I think.
    return text, options


def mn_confirm_prof(caller, raw_string, **kwargs):
    "Confirm their choice. Not that they have a choice."
    text = "Confirm your choice of profession:\n"
    text = "%s" % caller.ndb._menutree.prof

    options = ({"key": "_default",
                "goto": "mn_name"
                })

    return text, options


def mn_name(caller):
    text = "Choose a name:"
    options = {"key": "_default",
               "goto": _set_name}
    return text, options


def _set_name(caller, raw_string, **kwargs):

    caller.ndb._menutree.name = raw_string
    caller.msg("Your name will be %s." % raw_string)
    return "mn_review"


def _save_char(caller):
    "creates a DR char using chosen information"
    #  TODO: make DRC typeclass and create command
    name = caller.ndb._menutree.name
    prof = caller.ndb._menutree.prof
    bonus = caller.ndb._menutree.bonus

    new_drc = create.create_object("dr_characters.DR_char",
                                   name, report_to=caller)

    new_drc.db.prof = prof
    new_drc.db.bonus = bonus

    report = "Created %s, a %s with especially good %s.\n" % \
        (name, prof, bonus)

    caller.msg(report)

    if caller.location.db.lives:
        caller.location.db.lives.append(name)
    else:
        caller.location.db.lives = []
        caller.location.db.lives.append(name)

    return "mn_dr_start"


def mn_review(caller):
    text = "DR Character summary:\n"
    text += "Name: %s\n" % caller.ndb._menutree.name
    text += "Profession: %s\n" % caller.ndb._menutree.prof
    text += "Bonus ability: %s\n" % caller.ndb._menutree.bonus

    options = ({"key": ("Accept", "A", "a"),
                "goto": _save_char},
               {"key": ("Restart", "R", "r"),
                "goto": "mn_dr_start"})
    return text, options
