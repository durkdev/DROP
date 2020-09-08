# DROP/typeclasses/npcshop.py
"""
NPC-shop-Tutorial from evennia wiki. 
"""

from evennia.utils import evmenu


def menunode_shopfront(caller):
    "This is the top-menu screen."
    
    shopname = caller.location.key
    wares = caller.location.db.storeroom.contents

    # Wares includes all items inside the storeroom, including the door!
    # Remove the door as it is not for sale.

    wares = [ware for ware in wares if ware.key.lower() != "door"]

    # TODO: In a DROP appropriate shop, perhaps replace storeroom with 
    # a list of permant items that never go out of stock. Purchasing 
    # items creates them for the first time.

    text = "*** Welcome to %s! ***\n" % shopname
    if wares: 
        text += "   Things for sale (chose 1-%i to inspect);" \
                " [q]uit to exit:" % len(wares)
        # this relies on the built in 'quit' command.

    else:
        text += "   There is nothing for sale; quit to exit."

    text += "\n   This is working ~j3b"
    
    options = []
    for ware in wares:
        # add an option for every ware in store
        options.append({"desc": "%s (%s gold)" %
                            (ware.key, ware.db.gold_value or 1),
                        "goto": "menunode_inspect_and_buy"})
    options.append({"key": "think",
                    "goto": "nowhere"})
    return text, options

# next menu node

def menunode_consider_quit(caller):
    """
    Where you can consider the recent results before continuing 
    to shop or quit.
    """
    text = "Whatcha gonna do now?"

    options = ({"key": ("continue shopping", "c"),
                "desc": "review list of goods",
                "goto": "menunode_shopfront"},
               {"key": ("quit", "q")})

    return text, options


def menunode_inspect_and_buy(caller, raw_string):
    "Sets up the buy menu screen."

    wares = caller.location.db.storeroom.contents
    # remove the door
    wares = [ware for ware in wares if ware.key.lower() != "door"]
    iware = int(raw_string) - 1
    ware = wares[iware]
    value = ware.db.gold_value or 1
    wealth = caller.db.gold or 0
    text = "You inspect %s:\n\n%s" % (ware.key, ware.db.desc)

    def buy_ware_result(caller):
        "This will be executed first when choosing to buy."
        if wealth >= value:
            rtext = "You pay %i gold and purchase %s!" % \
                    (value, ware.key)
            caller.db.gold -= value
            ware.move_to(caller, quiet=True)
        else:
            rtext = "You cannot afford %i gold for %s!" % \
                    (value, ware.key)
        caller.msg(rtext)
        return "menunode_consider_quit"

    options = ({"desc": "Buy %s for %s gold" % \
                        (ware.key, ware.db.gold_value or 1),
                "goto": "menunode_shopfront",
                "exec": buy_ware_result},
                {"desc": "Look for something else",
                 "goto": "menunode_shopfront"})

    return text, options

def nowhere(caller, raw_string):
    "Nothing happens here except proof that something works"
    text = "You're going nowhere, a little faster now."
    return text
# Character command

from evennia import Command

class CmdBuy(Command):
    """
    Start to do some shopping

    Usage: buy 
           shop
           browse

    This will allow you to browse the wares of the 
    current shop and buy items you want.
    """

    key = "buy"
    aliases = ("shop", "browse")

    def func(self):
        "Starts the shop EvMenu instance"
        evmenu.EvMenu(self.caller,
                      "typeclasses.npcshop",
                      startnode="menunode_shopfront")

# CmdSet to grant the shopping command to characters in the
# store.

from evennia import CmdSet

class ShopCmdSet(CmdSet):
    def at_cmdset_creation(self):
        self.add(CmdBuy())


# Building the shop
from evennia import DefaultRoom, DefaultExit, DefaultObject
from evennia.utils.create import create_object

# class for our front shop room
class NPCShop(DefaultRoom):
    def at_object_creation(self):
        # we could also use add(ShopCmdSet, permanent=True)
        # looks like a new feature since last time I was here
        self.cmdset.add_default(ShopCmdSet)
        self.db.storeroom = None


# command to build a complete shop (the Command base class
# should already have been imported earlier in this file)
# I really type in almost everything from the tutorial.
class CmdBuildShop(Command):
    """
    Build a new shop

    Usage:
        buildshop shopname

    This will create a new NPCshop room as 
    well as a linked store room named 
    simply <storename>-storage for the wares
    on sale. The store room will be accessed
    through a locked door in the shop.
    """
    key = "buildshop"
    locks = "cmd:perm(Builders)"
    help_category = "Building"

    def func(self):
        "Create the shop rooms"
        if not self.args:
            self.msg("Usage buildshop <storename>")
            return
        # create the shop and storeroom
        shopname = self.args.strip()
        shop = create_object (NPCShop,
                              key=shopname,
                              location=None)
        storeroom = create_object(DefaultRoom,
                              key="%s-storage" % shopname,
                              location=None)
        shop.db.storeroom = storeroom 
        # create a door between the two
        shop_exit = create_object(DefaultExit,
                                  key="back door",
                                  aliases=["storage", "store room"],
                                  location=shop,
                                  destination=storeroom)
        storeroom_exit = create_object(DefaultExit,
                                  key="door",
                                  location=storeroom,
                                  destination=shop)
        # make a key for accessing the store room
        storeroom_key_name = "%s-storekey" % shopname
        storeroom_key = create_object(DefaultObject,
                                      key=storeroom_key_name,
                                      location=shop)
        # only allow chars with this key to enter the store room
        shop_exit.locks.add("traverse:holds(%s)" % storeroom_key_name)
        
        #inform the builder about progress
        self.caller.msg("The shop %s was created!" % shop)



