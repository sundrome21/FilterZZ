class Block:

    def __init__(self, toggle):
        self.toggle = toggle

    def writeBlock(self,file):
        file.write(str(self.toggle))
        if hasattr(self,'itemLevel'):
            file.write("\n\tItemLevel " + self.itemLevelOpe + " " + str(self.itemLevel))
        if hasattr(self, 'rarity'):
            file.write("\n\tRarity " + self.rarityOpe + " " + self.rarity)
        if hasattr(self,'itemClass'):
            file.write("\n\tClass " + self.itemClass)
        if hasattr(self, 'baseType'):
            file.write("\n\tBaseType " + self.baseType)
        if hasattr(self,'socketGroup'):
            file.write("\n\tSocketGroup " + self.socketGroup)
        if hasattr(self,'borderColor'):
            file.write("\n\tSetBorderColor " + self.borderColor)
        if hasattr(self,'textColor'):
            file.write("\n\tSetTextColor " + self.textColor)
        if hasattr(self,'backGroundColor'):
            file.write("\n\tSetBackgroundColor " + self.backGroundColor)
        if hasattr(self,'fontSize'):
            file.write("\n\tSetFontSize " + str(self.fontSize))

    def setColors(self,borderColor,textColor,backGroundColor,fontSize):
        self.borderColor = borderColor
        self.textColor = textColor
        self.backGroundColor = backGroundColor
        self.fontSize = fontSize
