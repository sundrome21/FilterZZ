import block
import program

p = program.Program()
p.createFile()
block = block.Block("Show")

# Setting up the 3 main 4-Links of the build
setattr(block, 'itemClass', "\"Helmets\" \"Boots\" \"Gloves\"")
setattr(block, 'socketGroup', "\"BBBB\" \"BBRR\" \"RRRB\"")
block.setColors(p.socketColorBoTe,p.socketColorBoTe,p.socketColorBa,45)
block.writeBlock(p.f)

p.addNewLine()

# Setting up the main 6-Links
setattr(block, 'itemClass', "\"Body Armours\"")
setattr(block, 'socketGroup', "\"BBBG\" \"BBBGG\" \"BBBBG\"")
block.writeBlock(p.f)

p.addNewLine()

# Setting up remaining sockets/1H/2H
setattr(block, 'itemClass', "\"Shields\" \"Daggers\" \"Sceptres\"")
setattr(block, 'socketGroup', "\"BBB\" \"RRG\"")
block.writeBlock(p.f)

p.addNewLine()

delattr(block, 'itemClass')
delattr(block, 'socketGroup')

# Get rid of attributes for previous session, open file for each item
# Possibly going to get this from Poe Wiki API depending in what links did you choose
file = open("~/src/helmets.txt","r")
lines = file.readlines()
for index in range(len(lines)):
    if lines[index][0].isalpha():
        setattr(block, 'rarity', "Rare")
        setattr(block, 'rarityOpe', "=")
        setattr(block, 'baseType', "\"" + lines[index].rstrip() + "\"")
        level = 0
        if index+3 < len(lines):
            if lines[index+3][0] == '=':
                level = 100
            else:
                level = int(lines[index+3][1:3])-1
        else:
            level = 100
        setattr(block, 'itemLevel', str(level))
        setattr(block, 'itemLevelOpe', "<=")
        block.setColors(p.progColorRareBoTe,p.progColorRareBoTe,p.progColorRareBa,45)
        block.writeBlock(p.f)
        p.addNewLine()

        setattr(block, 'rarity', "Magic")
        setattr(block, 'rarityOpe', "<=")
        block.setColors(p.progColorElseBoTe,p.progColorElseBoTe,p.progColorElseBa,35)
        block.writeBlock(p.f)
        p.addNewLine()
