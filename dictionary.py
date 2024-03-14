class Dictionary:
    def __init__(self):
        self.traduttore = {}
        pass

    def addWord(self, word, meaning):
        if word in self.traduttore:
            self.traduttore[word] += meaning
        else:
            self.traduttore[word] = meaning
        pass

    def translate(self, query):
        if query in self.traduttore:
            return self.traduttore.get(query)
        pass

    def translateWordWildCard(self, query):
        for wc in self.traduttore:
            counter = 0
            i = 0
            lun = 0
            for letter in wc:
                lun = lun + 1
                if letter == query[i]:
                    counter = counter + 1
                i = i + 1
            if counter == lun-1:
                return self.traduttore.get(wc)
        pass
    def stampaDizionario(self):
        print(self.traduttore)

