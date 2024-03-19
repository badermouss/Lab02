import translator as tr
import dictionary as dt

t = tr.Translator()

finisci = False

while not finisci:

    t.printMenu()

    diz_caricato = t.loadDictionary("dictionary.txt")
    txtIn = input()

    # Add input control here!
    try:
        if int(txtIn) == 1:
            parola = input("Quale parola vuoi aggiungere?")
            t.handleAdd(parola)
        if int(txtIn) == 2:
            aliena = input("Quale parola vuoi tradurre?")
            traduzione = t.handleTranslate(aliena)
            if traduzione is not None:
                print(f"La traduzione della parola cercata è {traduzione}")
            else:
                print("La parola aliena non è presente nel dizionario.")
        if int(txtIn) == 3:
            alienaWild = input("Quale parola vuoi tradurre? (max un punto interrogativo)")
            traduzione = t.handleWildCard(alienaWild)
            if traduzione is not None:
                print(f"La traduzione WildCard della parola cercata è {traduzione}")
            else:
                print("La parola aliena non è presente nel dizionario")
        if int(txtIn) == 4:
            print("DIZIONARIO COMPLETO:")
            diz_caricato.stampati()
        if int(txtIn) == 5:
            finisci = True
    except ValueError:
        print("Valore inserito non valido")
