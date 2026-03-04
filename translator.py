import dictionary as d


class Translator:

    def __init__(self):
        self.dict = d.Dictionary()

    def printMenu(self):
        print("---------------------------")
        print("Translator Alien-Italian")
        print("---------------------------")
        print("1. Aggiungi nuova parola")
        print("2. Cerca una traduzione")
        print("3. Cerca con wildcard")
        print("4. Exit ")
        print("---------------------------")

    def loadDictionary(self, dict):
        # dict is a string with the filename of the dictionary
        with open(dict, "r", encoding="UTF-8") as file:
            for riga in file:
                riga = riga.rstrip()
                if " " in riga:
                    parola_aliena = riga.split(" ")[0]
                    significato = riga.split(" ")[1]
                    self.dict.addWord(parola_aliena, significato)

    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        pass

    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        query = query.strip().lower()
        if query in self.dict.dizionario:
            print("Traduzione", self.dict.dizionario[query])
        else:
            print("Parola Non Trovata")


    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        pass