###########################################################################################
# Name: Adam Stafford
# Date: 4/8/2024
# Description:A text-adventure-turned GUI RPG with lore and puzzles throughout.
###########################################################################################

###########################################################################################
# import libraries
from tkinter import *


###########################################################################################
# constants
VERBS = [ "go", "look", "take" ]                    # the supported vocabulary verbs
QUIT_COMMANDS = [ "exit", "quit", "bye" ]           # the supported quit commands

###########################################################################################
# the blueprint for a room
class Room:
    # the constructor
    def __init__(self, name, image):
        # rooms have a name, image, description, exits (e.g., south), exit locations (e.g., to the
        # south is room n), items (e.g., table), item descriptions (for each item), and grabbables
        # (things that can be taken into inventory)
        self._name = name
        self._image = image
        self._description = ""
        self._exits = []
        self._exitLocations = []
        self._items = []
        self._itemDescriptions = []
        self._grabbables = []

    # getters and setters for the instance variables
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def exits(self):
        return self._exits

    @exits.setter
    def exits(self, value):
        self._exits = value

    @property
    def exitLocations(self):
        return self._exitLocations

    @exitLocations.setter
    def exitLocations(self, value):
        self._exitLocations = value

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        self._items = value

    @property
    def itemDescriptions(self):
        return self._itemDescriptions

    @itemDescriptions.setter
    def itemDescriptions(self, value):
        self._itemDescriptions = value

    @property
    def grabbables(self):
        return self._grabbables

    @grabbables.setter
    def grabbables(self, value):
        self._grabbables = value

    # adds an exit to the room
    # the exit is a string (e.g., north)
    # the room is an instance of a room
    def addExit(self, exit, room):
        # append the exit and room to the appropriate lists
        self._exits.append(exit)
        self._exitLocations.append(room)

    # adds an item to the room
    # the item is a string (e.g., table)
    # the desc is a string that describes the item (e.g., it is made of wood)
    def addItem(self, item, desc):
        # append the item and description to the appropriate lists
        self._items.append(item)
        self._itemDescriptions.append(desc)

    # adds a grabbable item to the room
    # the item is a string (e.g., key)
    def addGrabbable(self, item):
        # append the item to the list
        self._grabbables.append(item)

    # returns a string description of the room as follows:
    #  <name>
    #  <description>
    #  <items>
    #  <exits>
    # e.g.:
    #  Room 1
    #  You look around the room.
    #  You see: chair table 
    #  Exits: east south 
    def __str__(self):
        # first, the room name and description
        s = "{}\n".format(self._name)
        s += "{}\n".format(self._description)

        # next, the items in the room
        s += "You see: "
        for item in self._items:
            s += item + " "
        s += "\n"

        # next, the exits from the room
        s += "Exits: "
        for exit in self._exits:
            s += exit + " "

        return s

###########################################################################################
# the blueprint for a Game
# inherits from the Frame class of Tkinter
class Game(Frame):
    # the constructor
    def __init__(self, parent):
        # call the constructor in the Frame superclass
        Frame.__init__(self, parent)

    # creates the rooms
    def createRooms(self):
        # a list of rooms will store all of the rooms
        # r1 through r4 are the four rooms in the "mansion"
        # currentRoom is the room the player is currently in (which can be one of r1 through r4)
        Game.rooms = []

        # first, create the room instances so that they can be referenced below
        r1 = Room("Windswept Crag", "craggy.gif")
        r2 = Room("Traveler's Respite", "respite.gif")
        r3 = Room("Icebound Oubliette", "dungeon.gif")
        r4 = Room("The Rimfell Snowfields", "snowfields.gif")
        r5 = Room("Harbinger's Seclude","library.gif" )
        r6 = Room("Warlord's Ruin, Tainted by Cold", "ruins.gif")
        r7 = Room("Warlord's Menagerie, Untouched by Time", "trove.gif")


        # room 1
           # Windswept Crag
        r1.description = "A snowy precipice, burdened by an eternal winter. To the East you see a desolate lodging..."
        r1.addExit("east", r2)
        r1.addGrabbable("torch")
        r1.addItem("frozen_wayfarer", "An unfortunate soul bearing an eternal flame in this frigid world. Perhaps the torch he posseses can be used later?")
        r1.addItem("ruined_map", "Tattered and torn, the map is of no use, save for a warning on its only legible side: 'There is only death East of the Rimfell Fields'.")
        Game.rooms.append(r1)

    # Traveler's Respite
        r2.description = "A refrain from the chill of the tundra, yet you know you can not linger. To the North you hear a screeching warcry"
        r2.addExit("west", r1)
        r2.addExit("north", r3)
#         r2.addGrabbable("enchanted_key")
        r2.addItem("grotesque_mural", "A disturbing image of a malformed knight is seen, marked with an insignia of a Warlord.")
        r2.addItem("frozen_pedestal", "An enchanted_key rests upon the pedestal, encased in ice. Maybe it can only be taken with a fiery source in your possesion?")
        Game.rooms.append(r2)

    # Icebound Oubliette
        r3.description = "A cold dungeon, bearing a remnant of the past. You feel a frigid presence lurking among the corridors..."
        r3.addExit("south", r2)
        r3.addExit("east", r4)
        r3.addGrabbable("warlords_insignia")
        r3.addItem("ancient_cell", "An old prison cell left ajar by an abundance of sharp icicles. What could have possibly been trapped in here? Nothing inside is of value, save for a bloodied warlords_insignia")
        Game.rooms.append(r3)

    # The Rimfell Snowfields
        r4.description = "An unassuming plain plagued with a relentless blizzard. Vision hindered, take you next steps wisely, as they could be your last..."
        r4.addExit("south", r5)
        r4.addExit("west", r3)
        r4.addExit("east", None)# DEATH!
        r4.addGrabbable("royal_sword")
        r4.addItem("snowy_outpost", "Amidst the snowfall you encounter an outpost with a felled royal inside. Sheathed beside her is a royal_sword too ornate for combat. You have no use for it, but it makes you wonder of the true nature of ruling parties in these frozen wastelands...")
        Game.rooms.append(r4)
    
    # Harbinger's Seclude
        r5.description = "Safe from the perils of Rimfell, you stumble into a withered library. Despite its current state, you feel a wealth of knowledge lingering here among ancient texts..."
        r5.addExit("north", r4)
        r5.addExit("west", r6)
        r5.addGrabbable("aged_riddles")
        r5.addItem("dragon_riddles", "An unassuming children's book of aged_riddles. You yawn as you sift through the pages, but maybe you should take the answers with you for your journey towards the Warlord's Ruins?")
        r5.addItem("ahamkara_scroll", "An untakeable ancient text depicting humanity barganing with Ahamkara, or Wish Dragons, for a better existence. Reading further, you discover that the treacherous Ahamkara always had a price...Not obtainable.")
        r5.addItem("king_rathil", "A storied history of King Rathil, the Violent. Many of its pages seemed to have been intentionally burned, but the few left question the legitamacy of his rule, arguring his acquisition of the crown from knighthood happened under mystcial circumstances. You cannot take it.")
        r5.addItem("fikrul,_beloved", "Seemingly a work of fiction, Fikrul, Beloved, details the symbiotic relationship of a King-turned-Warlord and a Wish Dragon in their quest for time itself. Almost fully intact, you notice the book's incessant mention of the dichotomy between the riddle-driven Dragon and the brutish Warlord. Useless to you." )
        Game.rooms.append(r5)

    # Warlord's Ruins
        r6.description = "The remnants of battles long past linger here, with the abundance of treasure and the mighty dragon looking down at you, you feel as if you could spend an eternity here..."
        r6.addExit("east", r5)
        r6.addExit("south", r7)
        r6.addGrabbable("ahamkara_armor")
        r6.addGrabbable("gold_coins")
        r6.addItem("ahamkara_armor", "Pieces of ahamkara_armor granted by the Wish Dragon, Fikrul. After the Ahamkara's death, it's cursed properties have ceased and is now free to claim.")
        r6.addItem("melting_banner", "A banner, unfrozen in time, depicting a now-forgotten warlord.")
        r6.addItem("treasure_trove", "Amidst the treasure trove is a plethora of gold_coins that only make CENTS to line your pockets!")
        Game.rooms.append(r6)

    # Warlord's Menagerie, Untouched by Time. scrapped due to time constraints. it was just gonna be a treasure room anyway.
        r7.description = "Time seems to stand still in this trove of opulence. Not even Fikrul dared venture here... CONGRATULATIONS! YOU HAVE BRAVED THE WINTER AND CONQUERED THE WARLORD's RUIN! Whenever you're ready to leave this adventure behind, please type quit! Thanks for playing!"
#     r7.addGrabbable("")
#     r7.addItem(".")
#     r7.addItem(".")
       
        Game.rooms.append(r7)
    #had to comment out most of this properties methods to get it to accept it as the good ending game over screen. stack overflow helped me realize that.
    

    # set room 1 as the current room at the beginning of the game
        Game.currentRoom = r1
    #Sean Boyle mentioned that I could define the indivudal room classes like this to make calling them easier when I need to
#         return {"r1": Game.r1, "r2": Game.r2, "r3": Game.r3, "r4": Game.r4, "r5": Game.r5, "r6": Game.r6, "r7": Game.r7}, Game.currentRoom
  
        Game.inventory = []

    # sets up the GUI
    def setupGUI(self):
        # organize the GUI
        self.pack(fill=BOTH, expand=1)

        # setup the player input at the bottom of the GUI
        # the widget is a Tkinter Entry
        # set its background to white
        # bind the return key to the function process() in the class
        # bind the tab key to the function complete() in the class
        # push it to the bottom of the GUI and let it fill horizontally
        # give it focus so the player doesn't have to click on it
        Game.player_input = Entry(self, bg="white")
        Game.player_input.bind("<Return>", self.process)
        Game.player_input.bind("<Tab>", self.complete)
        Game.player_input.pack(side=BOTTOM, fill=X)
        Game.player_input.focus()

        # setup the image to the left of the GUI
        # the widget is a Tkinter Label
        # don't let the image control the widget's size
        img = None
        Game.image = Label(self, width=WIDTH // 2, image=img)
        Game.image.image = img
        Game.image.pack(side=LEFT, fill=Y)
        Game.image.pack_propagate(False)

        # setup the text to the right of the GUI
        # first, the frame in which the text will be placed
        text_frame = Frame(self, width=WIDTH // 2)
        # the widget is a Tkinter Text
        # disable it by default
        # don't let the widget control the frame's size
        Game.text = Text(text_frame, bg="lightblue", state=DISABLED)
        Game.text.pack(fill=Y, expand=1)
        text_frame.pack(side=RIGHT, fill=Y)
        text_frame.pack_propagate(False)

    # set the current room image on the left of the GUI
    def setRoomImage(self):
        if (Game.currentRoom == None):
            # if dead, set the skull image
            Game.img = PhotoImage(file="hole.gif")
        else:
            # otherwise grab the image for the current room
            Game.img = PhotoImage(file=Game.currentRoom.image)

        # display the image on the left of the GUI
        Game.image.config(image=Game.img)
        Game.image.image = Game.img

    # sets the status displayed on the right of the GUI
    def setStatus(self, status):
        # enable the text widget, clear it, set it, and disable it
        Game.text.config(state=NORMAL)
        Game.text.delete("1.0", END)
        if (Game.currentRoom == None):
            # if dead, let the player know
            Game.text.insert(END, "As you haphazardly venture east of the blinding Rimfell Snowfields, you realize it's a path few could ever return from. Lost, frozen, and afraid, your journey ends here...""\nquit.\n")
            
#         if (Game.currentRoom == "Warlord's Menagerie, Untouched by Time"):
#             Game.text.insert(END, "CONGRATULATIONS! You have managed to escape the endless winter and braved the Warlord's Ruin! Type quit when you are ready to end the game!")
        else:
            # otherwise, display the appropriate status
            Game.text.insert(END, "{}\n\n{}\nYou are carrying: {}\n\n".format(status, Game.currentRoom, Game.inventory))
        Game.text.config(state=DISABLED)

        # support for tab completion
        # add the words to support
        if (Game.currentRoom != None):
            Game.words = VERBS + QUIT_COMMANDS + Game.inventory + Game.currentRoom.exits + Game.currentRoom.items + Game.currentRoom.grabbables


    # play the game
    def play(self):
        # create the room instances
        self.createRooms()
        # configure the GUI
        self.setupGUI()
        # set the current room
        self.setRoomImage()
        # set the initial status
        self.setStatus("You awake from a dreamless slumber in a frozen world...")

    # processes the player's input
    def process(self, event):
        # grab the player's input from the input at the bottom of the GUI
        action = Game.player_input.get()
        # set the user's input to lowercase to make it easier to compare the verb and noun to known values
        action = action.lower().strip()

        # exit the game if the player wants to leave (supports quit, exit, and bye)
        if (action in QUIT_COMMANDS):
            exit(0)

        # if the current room is None, then the player is dead
        # this only happens if the player goes south when in room 4
        if (Game.currentRoom == None):
            # clear the player's input
            Game.player_input.delete(0, END)
            return

        # set a default response
        response = "I don't understand. Try verb noun. Valid verbs\nare {}.".format(", ".join(VERBS))
        # split the user input into words (words are separated by spaces) and store the words in a list
        words = action.split()

        # the game only understands two word inputs
        if (len(words) == 2):
            # isolate the verb and noun
            verb = words[0].strip()
            noun = words[1].strip()

            # we need a valid verb
            if (verb in VERBS):
                # the verb is: go
                if (verb == "go"):
                    # set a default response
                    response = "You can't go in that direction."

                    # check if the noun is a valid exit
                    if (noun in Game.currentRoom.exits):
                        

                        
                        if noun == "north" and Game.currentRoom.name == "Traveler's Respite" and "enchanted_key" not in Game.inventory:
                            response = "The Northward path is blocked by a mystical lock. Perhaps a key of magical proportions would unlock it?"
                            
                        elif noun == "west" and Game.currentRoom.name == "Harbinger's Seclude" and "warlords_insignia" not in Game.inventory:
                            response = "The way towards the Warlord's Ruins are closed. Looking closer, you notice an insignia-shaped hole in the gate's center..."
                            
                        elif noun == "south" and Game.currentRoom.name == "Warlord's Ruin, Tainted by Cold" and "aged_riddles" and "royal_sword" not in Game.inventory:
                            response = "Oh? Your eternity in the Warlord's Ruins has only just begun and you dare wish to leave? HA! You are no riddleman nor are you a royal, now gorge yourself on my trinkets whilst I gorge on your immortal soul..."
                        else:      
                        # get its index
                            i = Game.currentRoom.exits.index(noun)
                        # change the current room to the one that is associated with the specified exit
                            Game.currentRoom = Game.currentRoom.exitLocations[i]
                        # set the response (success)
                            response = "You venture {} and encounter another area.".format(noun)
                        
                        
                # the verb is: look
                elif (verb == "look"):
                    
                    # set a default response
                    response = "You don't see that item."

                    # check if the noun is a valid item
                    if (noun in Game.currentRoom.items):
                        # get its index
                        i = Game.currentRoom.items.index(noun)
                        # set the response to the item's description
                        response = Game.currentRoom.itemDescriptions[i]
                # the verb is: take
                
                elif (verb == "take"):
                    if noun == "torch" and "torch" in Game.currentRoom.grabbables:
                        Game.inventory.append("torch")
                        Game.currentRoom.grabbables.remove("torch")
                        response = "You take the torch and feel its radiance ebb"
                        
                        if "frozen_wayfarer" in Game.currentRoom.items:
                            Game.currentRoom.itemDescriptions[Game.currentRoom.items.index("frozen_wayfarer")] = "A now bare wayfarer, without a light to warm his eternal slumber"
                            
                            
#                         rooms["r1"].itemDescriptions[rooms["r1"].items.index("frozen_wayfarer")] = "An unfortunate soul, now without his eternal flame."
                   
                    elif noun == "enchanted_key" and "frozen_pedestal" in Game.currentRoom.items:
                        if "torch" in Game.inventory:
                            response = "Using the torch's eternal flame, you melt the ice encasing the enchanted key and take it."
                            Game.inventory.append("enchanted_key")
                        
                            Game.currentRoom.itemDescriptions[Game.currentRoom.items.index("frozen_pedestal")] = "An empty pedestal, where the enchanted key once was"
                        else:
                            response = "The enchanted key is encased in ice. You need something to melt the ice."
                            
                    elif noun == "warlords_insignia" and "warlords_insignia" in Game.currentRoom.grabbables:
                        Game.inventory.append("warlords_insignia")
                        
                        Game.currentRoom.grabbables.remove("warlords_insignia")
                        
                        response = "You feel the insignia bleed in your hands"
                        
                        if "ancient_cell" in Game.currentRoom.items:
                            
                            Game.currentRoom.itemDescriptions[Game.currentRoom.items.index("ancient_cell")] = "A now empty cell, where the Warlord's Insignia once laid."

                            

#                             Game.currentRoom.itemDescriptions[Game.currentRoom.items.index("ancient_cell")] = "A now empty cell, where the warlords_insignia once laid"
                    elif noun == "aged_riddles" and "aged_riddles" in Game.currentRoom.grabbables:
                        Game.inventory.append("aged_riddles")
                        
                        Game.currentRoom.grabbables.remove("aged_riddles")
                        
                        response = "You feel a ghastly spirit flow through the riddles"
                        
                        if "dragon_riddles" in Game.currentRoom.items:
                            
                            Game.currentRoom.itemDescriptions[Game.currentRoom.items.index("dragon_riddles")] = "A now empty shelf where riddles once were"
                    
                    elif noun == "royal_sword" and "royal_sword" in Game.currentRoom.grabbables:
                        Game.inventory.append("royal_sword")
                        
                        Game.currentRoom.grabbables.remove("royal_sword")
                        
                        response = "You feel as though a royal blessing has befallen you as you brandish the weapon"
                        
                        if "snowy_outpost" in Game.currentRoom.items:
                            
                            Game.currentRoom.itemDescriptions[Game.currentRoom.items.index("snowy_outpost")] = "The now empty outpost lacks both the royal sword as well as her fallen wielder..."
                                                     
                        
                    elif noun in Game.currentRoom.grabbables and noun not in Game.inventory:
                        Game.inventory.append(noun)
                        Game.currentRoom.grabbables.remove(noun)
                        response = "You take {}" .format(noun)       
                    else:

                    # set a default response
                        response = "You don't see that item."

                    # check if the noun is a valid grabbable and is also not already in inventory
                    if (noun in Game.currentRoom.grabbables and noun not in Game.inventory):
                        # get its index
                        i = Game.currentRoom.grabbables.index(noun)
                        # add the grabbable item to the player's inventory
                        Game.inventory.append(Game.currentRoom.grabbables[i])
                        # set the response (success)
                        response = "You take {}.".format(noun)

        # display the response on the right of the GUI
        # display the room's image on the left of the GUI
        # clear the player's input
        self.setStatus(response)
        self.setRoomImage()
        Game.player_input.delete(0, END)

    # implements tab completion in the Entry widget
    def complete(self, event):
        # get user input and the last word of input
        words = Game.player_input.get().split()
        # continue only if there are words in the user's input
        if (len(words)):
            last_word = words[-1]
            # check if the last word of input is part of a valid verb/noun
            results = [ x for x in Game.words if x.startswith(last_word) ]

            # initially, there is no matching verb/noun
            match = None

            # is there only a single valid verb/noun?
            if (len(results) == 1):
                # the result is a match
                match = results[0]
            # are there multiple valid verbs/nouns?
            elif (len(results) > 1):
                # find the longest starting substring of all verbs/nouns
                for i in range(1, len(min(results, key=len)) + 1):
                    # get the current substring
                    match = results[0][:i]
                    # find all matches
                    matches = [ x for x in results if x.startswith(match) ]
                    # if there are less matches than verbs/nouns
                    if (len(matches) != len(results)):
                        # go back to the previous substring
                        match = match[:-1]
                        # stop checking
                        break
            # if a match exists, replace the user's input
            if (match):
                # clear user input
                Game.player_input.delete(0, END)
                # add all but the last (matched) verb/noun
                for word in words[:-1]:
                    Game.player_input.insert(END, "{} ".format(word))
                # add the match
                Game.player_input.insert(END, "{}{}".format(match, " " if (len(results) == 1) else ""))

        # prevents the tab key from highlighting the text in the Entry widget
        return "break"

###########################################################################################
# START THE GAME!!!
# the default size of the GUI is 800x600
WIDTH = 800
HEIGHT = 600

# create the window
window = Tk()
window.title("WARLORD'S RUIN")

# create the GUI as a Tkinter canvas inside the window
g = Game(window)
# play the game
g.play()

# wait for the window to close
window.mainloop()

