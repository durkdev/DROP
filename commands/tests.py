# DROP/commands/tests.py

import unittest

# This is the tutorial unit test to test in game commands
"""
    We are testing CmdAbilities first. We also need to import the 
    Character typeclass in order to test the command as used by an actual 
    character in the game.
"""

from evennia.commands.default.tests import CommandTest

from commands.command import CmdAbilities
from typeclasses.characters import Character

class TestAbilities(CommandTest):

    character_typeclass = Character

    def test_simple(self):
        self.call(CmdAbilities(), "", "STR: 0, INT: 0, WIS: 0, DEX: 0, CON: 0, CHA: 0")


# Testing buildshop
from typeclasses.npcshop import CmdBuildShop, NPCShop
from evennia.commands.default import general, building
# going to need a shop and its commands

class TestBuildShop(CommandTest):
    "tests building a shop by calling the cmd with TestShop"
    "also tries to teleport to it"
    
    def test_buildshop(self):
        self.call(CmdBuildShop(), "Testmart","The shop Testmart was created!")
    # wonder if the object lingers and we can test it more.
    # tel to shop and run the commmands

    #def test_entershop(self):
    #   self.call(building.CmdTeleport(), "Testmart","Teleported to Testmart.") 

# Testing Create/Drop look
# Everything I need should be imported by now.

class TestMakeLook(CommandTest):
    """
    Tests creating and object, dropping it, then looking in the room
    to see if the object is there.
    """

    def test_create(self):
        self.call(building.CmdCreate(), "/drop mushroom", "You create a new Object: mushroom.")
    
    def test_look(self):
        self.call(general.CmdLook(), "", 
           "Room(#1)\nroom_desc\nExits: out(#3)\n"
           "You see a: Obj(#4), Obj2(#5), Char2(#7)") 

    def test_go(self):
        self.call(out, "", "I don't know what to expect")
