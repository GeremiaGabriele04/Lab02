import translator as tr

t = tr.Translator()


while(True):

    t.printMenu()

    t.loadDictionary("dictionary.txt")

    txtIn = input()


    if txtIn.isdigit() and int(txtIn)<5:
        if int(txtIn) == 1:
            print("Ok, quale parola vuoi aggiungere?")
            txtIn1 = input()
        if int(txtIn) == 2:
            print("Ok, quale parola vuoi tradurre?")
            txtIn1 = input()
            t.handleTranslate(txtIn1)
        if int(txtIn) == 3:
            pass
        if int(txtIn) == 4:
            break
    else:
        raise ValueError("Valore non valido")