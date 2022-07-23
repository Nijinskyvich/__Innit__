import keyboard

abbr_dict = {
    #British
    "pounds" : ["quid",False],
    "angry" : ["aggy",False],
    "asked" : ["aksed",False],
    "mess" : ["shambles",False],
    "amazing" : ["amazeballs",False],
    "children" : ["ankle-biters",False],
    "nervous" : ["antsy",False],
    "crazy" : ["apeshit",False],
    "compliment" : ["arse-lick",False],
    "complimenting" : ["arse-licking",False],
    "complimented" : ["arse-licked",False],
    "hello" : ["ay-up",False],
    "baby" : ["babby",False],
    "lady" : ["bag",False],
    "introvert" : ["batty boy",False],
    "chat" : ["banter",False],
    "toilet" : ["loo",False],
    "very" : ["proper",False],
    "tired" : ["knackered",False],
    "upset" : ["gutted",False],
    "angry" : ["pissed",False],
    
    #Grammatical
    "your" : ["you're",False],
    "you're" : ["your",False],
    "their" : ["they're",False],
    "there" : ["their",False],
    "they're" : ["there",False],
    "to" : ["too",False],
    "too" : ["to",False],
    "of" : ["off",False],
    "off" : ["of",False],
    #"here" : ["hear",True],
    #"hear" : ["here",True],



}

def enter():
    #keyboard.write("innit")
    #keyboard.send("enter")
    pass

def abbreviate(source_text:str,replacement_text:str,suffix: bool):
    keyboard.add_abbreviation(source_text, replacement_text, match_suffix=suffix, timeout=1)

for key in abbr_dict:
    abbreviate(key,abbr_dict[key][0]+" ",abbr_dict[key][1])

keyboard.add_hotkey("enter",enter)
keyboard.wait()