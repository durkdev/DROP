# Tables Introduction 
A random dungeon adventure generating system intuitively consists of lots of
tables. This project itself is inspired by a set of tables originally published
in the 1st Edition Advanced Dungeons & Dragons, Dungeon Masters Guide ("DMG").
So I'm using this document to think out loud about tables. In a previous version
of this project, Apendixie. I produced a simulacrum of the DMG tables.  I've
imported that table to this project without a clear idea yet if, or how I want
to use it. [tables.py](world/tables.py) tables.py currently has one dictionary
or "book" of tables named GYGAX. 

## Digression about GYGAX
GYGAX is as or more complex than I think I can tolerate. It is a dictionary of
about 20 arrays (tables) which contain table headings and tuples of results. It
might be more reasonable to make every table a separate data structure.  There
is no particular reason that they have to be combined.  Each structure would
have to follow a strict rubric to ensure it played properly with whichever
commands utilized it.  But that's true either way.

GYGAX succeeds in implementing some of the DMG game but does not contain the
tricks, traps, treasure or monster results.  So I'm at a crossroads (I've been
here before) where I need to decide whether to build on GYGAX and attempt to
implement the game as imagined in the DMG, or to start fresh with my own tables,
custom built to match a game of my own vision. 

The answer I think, right now, is that it is time to branch out.  For one thing,
Dungeon Robber has already done the job of faithfully implementing the DMG
vision in a mix of homage and irony.  I really don't need to do that all over
again.  I know one of my motivations has been to re-create Dungeon Robber really
just to let myself play it in a post adobe flash world. But I think I can get
over that. Okay so digression has succeeded.

## Tables or Not? 
Are there alternatives to tables as a design tool? Nothing coming to me at the
moment.

# Table Architecture Considerations
Okay I think my first requirement will be for my data structure is to support
the creative process.  It should be easy for the creative devs to start writing
up tables as stand alone projects.  This means minimizing the complex
layers of architecture we saw in GYGAX. 

On the other hand if the creative content of a table leads to
technical results I imagine it makes sense to be able to add that into the table
itself.  That is a unique result should only need to be looked up once. 

Can tables be probabilitly and game rule agnostic? That is should I be able to
create a table of common and uncommon results without deciding on the weight of
each result till later?  In GYGAX which itself was based on table top roll
playing games the tables assumed the player would roll polyhedral dice of
certain sizes in order to pick results. The table creator chose probabilities
while composing results. In a more abstracted environment the table creator
could merely enter results with no view to probabilities OR could enter relative
descriptions of the quality of results with a set of terms which can be defined
later.  Ie. I could say "emtpy room" is a "common" result and later "an
unguarded treasure is a rare result"  and even say "a magical talking pool" is
an "astronomically remote" result.    

This allows the creative dev to offer opinions about game balance that might be
easy to adjust globally later. 

