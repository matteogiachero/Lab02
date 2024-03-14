import dictionary as d
class Translator:

    def __init__(self):
        self.dizionario = d.Dictionary()
        pass

    def printMenu(self):
        print("---------------------")
        print("Translator Alien-Italian")
        print("---------------------")
        # 1. Aggiungi nuova parola
        print("1) Aggiungi nuova parola")
        # 2. Cerca una traduzione
        print("2) Cerca una traduzione")
        # 3. Cerca con wildcard
        print("3) Cerca con wildcard")
        # 4. Stampa tutto il dizionario
        print("4) Stampa tutto il dizionario")
        # 5. Exit
        print("5) Exit")
        print("---------------------")
        pass

    def loadDictionary(self, dict):
        # dict is a string with the filename of the dictionary
        file = open (dict, "r")
        for line in file:
            line.rstrip()
            s = line.split(" ")
            self.dizionario.addWord(s[0].rstrip(),s[1].rstrip())
        file.close()
        pass

    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        list = []
        trad = entry.split(" ")
        for word in trad:
            list.append(word.rstrip())
        list.pop(0)
        self.dizionario.addWord(trad[0].rstrip(), list)
        pass

    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        traduzione = self.dizionario.translate(query.lower())
        if traduzione is not None:
            print(f"La tua traduzione è {traduzione}")
        else:
            print("La parola che hai cercato non è nel dizionario!")
        pass

    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        c = query.count("?")
        if c == 1:
            traduzione = self.dizionario.translateWordWildCard(query)
            if traduzione is not None:
                print(f"La tua traduzione è {traduzione}")
            else:
                print("La parola che hai cercato non è nel dizionario!")

        else:
            print("Hai inserito troppi '?' nella ricerca con WildCard")
        pass

    def handleStampa(self):
        self.dizionario.stampaDizionario()