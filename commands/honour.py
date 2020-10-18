# honour.py
'''
Commands used in the honour system. The centrepiece is the "prompter" called
by the "engage" command or one of its aliases. It asks users to explain with
honour if and how they overcome obstacles. The output of the prompter is a
journal entry.  A journal command will allow a player to review and comment on
their journal entries.
'''

from evennia import Command
from evennia.utils import evmenu


class Engage(Command):  # intereact with target object.
    """
    engage - a  generic command for interacting with obstacles and features

    Usage:
      engage <target>

    Aliases:  attack, kill, break, smash, get, solve, pick, disarm

    Using the most appropriate alias will make your journal more readable
    but they have no other effect.
    """

    key = "engage"
    aliases = ["attack", "kill", "break", "smash", "get", "solve", "pick",
               "disarm"]
    # Note that aliases will seem to be completely different commands but
    # under the hood they are almost all the same thing. In the future
    # perhaps a parser will do a sanity check. Or maybe not.
    lock = "cmd:all()"
    help_category = "Honour System"

    def parse(self):
        # check is there a target?
        self.caller.msg(self.args)
        # and does the target exist?

    def func(self):
        "open the honour menu"
        self.caller.msg("You plan to %s the %s" % (self.cmdstring, self.args))
        evmenu.EvMenu(self.caller,
                      "commands.honour",  # menu nodes in this file
                      startnode="mn_start")
    # Thats the command. The rest will all play out in the menu. Good luck.


def mn_start(caller, raw_string, **kwargs):
    "start up the menu"
