# The Prompt

This is an evemenu command and tool that helps players resolve and record
conflicts and challenges. Once triggered with a target it will ask the player
a series of questions about the target and the player's strategy or approach
to dealing with it. The players responses are recorded (and there will be 
some attempt to parse and collate the text) and saved in a journal. 

The final output of the prompt should simply be a string or data structure
to be sent to a journalling function. 

# Prompt Models
The prompt can be simple or complex.  The plan is to start as simple as we can
get away with and still be fun. 

# Prompt Modes
The idea is that to get best results players will need to build some habits
and develop some writing/authoring routines to use the right verb forms so 
that the collated journal will read nicely.  So at first a player will want
more guidance from the prompt to walk them through the input. Later a player
may find it faster and easier to have less guidance (less steps) when 
composing a stategy and a ruling. The way to build this in will be 'modes'.

# Model A
Model A (alpha) this model is the bare minimum for testing. It assumes all
players have builder privileges. For example if the player targets a
non-existent object the prompt will suggest the player create it if desired.

## Model A prompt features
* callable command with aliases - 
* takes a target 
* no target = usage info
* ask user to describe the approach
* ask user to decide on success
* pass/fail/roll 
* for "roll" ask user for dice size and number and EITHER 
    * ask for target number in advance OR
    * roll, show result and ask player to interpret.
    * in either event follow b
* After pass/fail is decided ask for explanation.
* ask for a reference ie. an existing or new status that explains success or
  failure
* Ask user for consequences: 
    * none
    * condition/status update
    * externality
* unlock the object that was engaged
    * this is stand in for better externalities in the future 
* record it all
    * Create a string along these lines: 
    On (date/time) (character) encountered (obstacle) in (dungeon). They
    (approach) -ed it by (approach action description). This was a
    (success/failure) because (sucess/failure explanation). 
    [(character) was affected by (pre-existing condition or status).]
    As a consequence (character)  is now (character consequence) [(condition)].
    [And (obstacle) is (obstacle consequence)]
    [And (externalitiy)].

