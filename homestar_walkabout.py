from sys import exit
from pprint import pprint

#setup context
inv = ['quesos']
objectives = []
context = 'inside'

#setup vocabulary
move = ['go','enter','move','exit','walk','open','hover']
take = ['pickup','take','grab']
inventory = ['inv','inventory']
look = ['look','see']
use = ['use']
objectives = ['objectives']
actions = {'move': move, 'take': take, 'look': look, 'inventory': inventory, 'use': use, 'objectives': objectives}
directions = {'in': ['in','inside','enter'], 'out': ['out','outside','exit'], 'left': ['left','west'], 'right': ['right','east'], 'up': ['up','north'], 'down': ['down','south']}

# function to normalize input
def parse_input(input):
    global actions
    global context
    input = input.lower().strip()

    if('lure' in input or 'jig' in input):
        print 'You tantalizingly start to say "Come on and get in the boat, fish! Come on and get in the boat, fish fish! Come on and get in the boat, fish!" while doing a pretty sweet jig'
        print 'There are now many fish on the ground. Where they came from no one knows'
        return '',''

    if('fly' in input and 'hover' in move):
        print 'Well, you can\'t really fly ever since you put all that weight on. You can pretty much only hover an inch or two above the ground'
        return '',''
    if('sbu' in input and 'hover' in  move):
        print 'Why did you just say sbu? Are you some kind of idiot? Now you can\'t hover anymore!'
        actions['move'].remove('hover')
        return '',''

    if(input.find(' ') == -1 and input in inv):
        return 'use',input

    norm, match = match_vocab(actions, input)
    if(norm != ''):
        if(norm == 'move'):
            dir_norm, dir_match = match_vocab(directions, input)
            if(dir_norm != ''):
                return norm,dir_norm
        if(norm == 'inventory'):
            check_inv()
        remainder = input.replace(match,'').strip()
        return norm,remainder
        
    return 'error',''

def match_vocab(vocab, input):
    """Takes a dictionary of lists as a vocabulary element and an input string and returns the normalized word and matched word"""
    for dict_key in vocab:
        for list_item in vocab[dict_key]:
            if(list_item in input):
                 return dict_key,list_item
    return '',''

def check_inv():
    global inv
    if(len(inv) > 0):
        print "Here is a list of all the things your have in your inventory:"
        for i in inv:
            print i
    else:
        print "You have nothing in your inventory! This is terrible!"
    return 0

def get_input():
    input = raw_input('> ')
    return parse_input(input.strip())

def marzipan():
    print ''
    return 0

def bubs_inside():
    global context
    while(1):
        context = 'inside'
        description = 'You are inside a brick building. There are letters one might use on a movie theater sign strewn about the ground, many food items, and what appears to have been a cold one in a former life.'
        print description
        action,remainder = get_input()
        pprint(action)
        pprint(remainder)
        if(action == 'move'):
            if('out' in remainder):
                bubs_outside() 


def bubs_outside():
    global context
    while(1):
        context = 'outside'
        print 'You are outside of a small brick building, which, wait you know this place well! This is your concession stand. And even if you don\'t remember it, the sign at the top reading "Bubs\' Concession Stand" is helping out' 
        action,remainder = get_input()

print 'Welcome to Free Country, USA, home of Strongbadia-"The place where tropical breezes blow."'
print 'You are bubs, a man about town and you need to complete an adventure.'
print 'As with any good text-based adventure you will have to navigate this strange world by typing commands at the prompt.'
print 'Game experience will not change during on-line game play.'
bubs_inside()
