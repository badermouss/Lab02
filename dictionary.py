class Dictionary:
    def __init__(self):
        self.dizzz = {}

    def addWord(self, aliena, italiana):
        if aliena not in self.dizzz:
            self.dizzz[aliena] = italiana

    def translate(self, aliena):
        return self.dizzz[aliena]

    def translateWordWildCard(self, alienaWild):
        for key in self.dizzz:
            lettere_chiave = list(key)
            lettere_aliene = list(alienaWild)
            contatore = 0
            for i in range(min(len(lettere_aliene), len(lettere_chiave))):
                if lettere_aliene[i] == lettere_chiave[i]:
                    contatore += 1
            if (contatore == len(lettere_aliene) - 1 and "?" in lettere_aliene) or key == alienaWild.lower():
                return self.dizzz[key]
        return None

    def stampati(self):
        for key in self.dizzz:
            print(f"{key}: {self.dizzz[key]}")
