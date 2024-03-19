import dictionary as dt


class Translator:

    def __init__(self):
        self.diz_iniziale = dt.Dictionary()

    def printMenu(self):
        print("-" * 30)
        print("Translator Alien-Italian")
        print("-" * 30)
        print("1. Aggiungi nuova parola\n2. Cerca una traduzione\n3. Cerca con wildcard\n4. Stampa tutto il "
              "dizionario\n5. Exit")
        print("-" * 30)
        print("Scegli un numero: ")

    def loadDictionary(self, dict):
        # dict is a string with the filename of the dictionary
        with open(dict, "r") as f:
            riga = f.readline()
            while riga != "":
                elementi_riga = riga.split(" ")
                self.diz_iniziale.addWord(elementi_riga[0].strip().lower(), elementi_riga[1].strip().lower())
                riga = f.readline()
        return self.diz_iniziale

    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        elementi_entry = entry.split(" ")
        traduzioni = elementi_entry[1:len(elementi_entry)]
        self.diz_iniziale.addWord(elementi_entry[0].strip().lower(), traduzioni)
        print("Aggiunta!")
        print(f"{elementi_entry[0]} con traduzioni {traduzioni}")

    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        query_min = query.lower()
        return self.diz_iniziale.translate(query_min)

    def handleWildCard(self, query):
        # query is a string with a ? --> <par?la_aliena>
        query_min = query.lower()
        return self.diz_iniziale.translateWordWildCard(query_min)

