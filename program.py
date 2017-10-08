import os

class Program:
    socketColorBoTe = "255 255 255 255"
    socketColorBa = "77 87 152 255"
    progColorRareBoTe = "0 0 0 255"
    progColorRareBa = "240 220 180 255"
    progColorElseBoTe = "77 87 152 255"
    progColorElseBa = "0 0 0 255"

    def createFile(self):
        filepath = os.path.join('~/dest', "filterZZ.filter")
        if not os.path.exists('~/dest'):
            os.makedirs('~/dest')
        setattr(self, 'f', open(filepath, "w"))

    def addNewLine(self):
        self.f.write("\n\n")
