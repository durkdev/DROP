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

ALIASES = ["attack", "kill", "break", "smash", "solve", "pick",
           "disarm"]


class Engage(Command):  # intereact with target object.
    """
    engage - a  generic command for interacting with obstacles and features

    Usage:
      engage <target>

    Aliases:  attack, kill, break, smash, solve, pick, disarm
    """

    key = "engage"
    aliases = ALIASES
    # Note that aliases will seem to be completely different commands but
    # under the hood they are almost all the same thing. In the future
    # perhaps a parser will do a sanity check. Or maybe not.
    lock = "cmd:all()"
    help_category = "Honour System"

    def parse(self):
        # check is there a target?
        parse = "Look in room for target object"
        self.caller.msg(parse)

    def func(self):
        "open the honour menu"
        self.caller.msg("You {} the{}".format(self.cmdstring, self.args))
        evmenu.EvMenu(self.caller,
                      "commands.honour",  # menu nodes in this file
                      startnode=("mn_start"),
                      startnode_input=(self.cmdstring, {"Target": self.args})
                      )
    # Thats the command. The rest will all play out in the menu. Good luck.


def mn_start(caller, raw_string, **kwargs):
    "start up the menu"
    caller.ndb._menutree.target = kwargs["Target"].strip()
    text = "How do you plan on {}ing the {}?".format(
            raw_string, caller.ndb._menutree.target)
    options = []
    for verb in ALIASES:
        # add a option for each of the base ALIASES
        options.append({"desc": verb,
                        "goto": ("mn_items", {"verb": verb})})
    options.append(
            {"key": ("Other", "o", "O"),
             "desc": "Write in another verb of your choosing.",
             "goto": "mn_writeverb"})
    return text, options


def _set_verb(caller, raw_string, **kwargs):
    "write in an original verb"
    inp = raw_string.strip()
    prev_entry = kwargs.get("prev_entry")

    if not inp:
        if prev_entry:
            caller.key = prev_entry
            caller.msg("Set verb to {}.".format(prev_entry))
            return "mn_items"
        else:
            caller.msg("Aborted.")
            return "node_exit"
    else:
        return None, {"prev_entry": inp}


def mn_writeverb(caller, raw_string, **kwargs):
    "check if we have a verb already"
    prev_entry = kwargs.get("prev_entry")
    Target = caller.ndb._menutree.target

    if prev_entry:
        text = "You {} the {}".format(
                prev_entry, Target)
        text += "\nEnter a new verb or <return> to accept"
    else:
        text = "Enter an original verb or <return> to abort."

    options = {"key": "_default",
               "goto": (_set_verb, {"prev_entry": prev_entry})}
    return text, options


def mn_items(caller, raw_string, **kwargs):
    "confirm main verb, choose items"
    Target = caller.ndb._menutree.target
    text = "You will {} the {}.\n".format(kwargs["verb"], Target)
    text += "You have the following items in your inventory. Choose one"
    text += " it will be instrumental in your attempt. You will have the"
    text += " chance to choose more than one item."

    options = []
    for item in caller.contents:
        options.append({"desc": item,
                       "goto": "mn_itemcheck"})
    options.append(
            {"key": ("Other", "o", "O"),
             "desc": "Write in another item of your choosing.",
             "goto": "mn_writeitem"})
    return text, options
