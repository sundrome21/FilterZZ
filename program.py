class Program:
    socketColorBoTe = "255 255 255 255"
    socketColorBa = "77 87 152 255"
    progColorRareBoTe = "0 0 0 255"
    progColorRareBa = "240 220 180 255"
    progColorElseBoTe = "77 87 152 255"
    progColorElseBa = "0 0 0 255"

    def createFile(self):
        setattr(self, 'f', open("filterZZ.filter", "w"))

    def addNewLine(self):
        self.f.write("\n\n")
