import translator as tr

t = tr.Translator()


while(True):

    t.printMenu()

    t.loadDictionary("dictionary.txt")

    txtIniziale = input("Quale azione vuoi eseguire? ")

    # Add input control here!

    if int(txtIniziale) == 1:
        print("Ok, quale parola devo aggiungere? ")
        txtIn = input()
        controllo = txtIn.replace(" ","")
        if controllo.isalpha():
            aggiunta = t.handleAdd(txtIn)
        else:
            raise ValueError("Inserisci solo lettere!")
        pass
    if int(txtIniziale) == 2:
        print("Ok, quale parola devo cercare? ")
        txtIn = input()
        controllo = txtIn.replace(" ", "")
        if controllo.isalpha():
            cercare = t.handleTranslate(txtIn)
        else:
            raise ValueError ("Inserisci solo lettere!")
        pass
    if int(txtIniziale) == 3:
        print("Ok, quale parola devo cercare con Wildcard? ")
        txtIn = input()
        controllo = txtIn.replace("?", "")
        if controllo.isalpha():
            cercareWC = t.handleWildCard(txtIn)
        else:
            raise ValueError ("Inserisci solo lettere!")
        pass
    if int(txtIniziale) == 4:
        stampare = t.handleStampa()
    if int(txtIniziale) == 5:
        print("Chiusura traduttore!")
        break
