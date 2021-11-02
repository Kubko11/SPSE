class Nastroj:

    druh = ""
    cena = 0.0
    zvuk = ""
    pocet = 0

    def __init__(self, druh, cena, zvuk, pocet):
        self.druh = druh
        self.cena = cena
        self.zvuk = zvuk
        self.pocet = pocet

    def setDruh(self, druh):
        self.druh = druh

    def setCena(self, cena):
        self.cena = cena

    def setZvuk(self, zvuk):
        self.zvuk = zvuk

    def setPocet(self, pocet):
        self.pocet = pocet

    def getDruh(self):
        return self.druh

    def getCena(self):
        return self.cena

    def getZvuk(self):
        return self.zvuk

    def getPocet(self):
        return self.pocet
