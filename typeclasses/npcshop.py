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
                " quit to exit:" % len(wares)

    else:
        text += "   There is nothing for sale; quit to exit."
    
    options = []
    for ware in wares:
        # add an option for every ware in store
        options.append({"desc": "%s (%s gold)" %
                            (ware.key, ware.db.gold_value or 1),
                        "goto": "menunode_inspect_and_buy"})
    return text, options

# next menu node


def menunode_inspect_and_buy(caller, raw_string):
    "Sets up the buy menu screen."

    wares = caller.location.db.storeroom.contents
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

options = ({"desc": "Buy %s for %s gold" % \
                    (ware.key, ware.db.gold_value or 1),
            "goto": "menunode_shopfront",
            "exec": buy_ware_result},
            {"desc": "Look for something else",
             "goto": "menunode_shopfromt"})

return text, options


