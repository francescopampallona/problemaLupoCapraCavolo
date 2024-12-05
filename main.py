

def compiAzione(scelta, spondaSinistra, spondaDestra):
    if scelta == "0":
        if "Barca" in spondaSinistra:
            spondaSinistra[3] = ""
            spondaDestra[3] = "Barca"
        else:
            spondaDestra[3] = ""
            spondaSinistra[3] = "Barca"
    elif scelta == "1":
        if "Barca" in spondaSinistra and "Lupo" in spondaSinistra:
            spondaSinistra[3] = ""
            spondaSinistra[0] = ""
            spondaDestra[3] = "Barca"
            spondaDestra[0] = "Lupo"
        elif "Barca" in spondaDestra and "Lupo" in spondaDestra:
            spondaDestra[3] = ""
            spondaDestra[0] = ""
            spondaSinistra[3] = "Barca"
            spondaSinistra[0] = "Lupo"
    elif scelta == "2":
        if "Barca" in spondaSinistra and "Capra" in spondaSinistra:
            spondaSinistra[3] = ""
            spondaSinistra[1] = ""
            spondaDestra[3] = "Barca"
            spondaDestra[1] = "Capra"
        elif "Barca" in spondaDestra and "Capra" in spondaDestra:
            spondaDestra[3] = ""
            spondaDestra[1] = ""
            spondaSinistra[3] = "Barca"
            spondaSinistra[1] = "Capra"
    elif scelta == "3":
        if "Barca" in spondaSinistra and "Cavolo" in spondaSinistra:
            spondaSinistra[3] = ""
            spondaSinistra[2] = ""
            spondaDestra[3] = "Barca"
            spondaDestra[2] = "Cavolo"
        elif "Barca" in spondaDestra and "Cavolo" in spondaDestra:
            spondaDestra[3] = ""
            spondaDestra[2] = ""
            spondaSinistra[3] = "Barca"
            spondaSinistra[2] = "Cavolo"


def applicaRegoleAlloStato(spondaSinistra, spondaDestra):
    # Esamina spondaSinistra
    if "Lupo" in spondaSinistra and "Capra" in spondaSinistra and "Barca" not in spondaSinistra:
        spondaSinistra[1] = ""
        return True
    if "Capra" in spondaSinistra and "Cavolo" in spondaSinistra and "Barca" not in spondaSinistra:
        spondaSinistra[2] = ""
        return True
    # Esamina spondaDestra
    if "Lupo" in spondaDestra and "Capra" in spondaDestra and "Barca" not in spondaDestra:
        spondaDestra[1] = ""
        return True
    if "Capra" in spondaDestra and "Cavolo" in spondaDestra and "Barca" not in spondaDestra:
        spondaDestra[2] = ""
        return True
    return False

def obiettivoRaggiunto(spondaDestra):
    if "Lupo" in spondaDestra and "Capra" in spondaDestra and "Cavolo" in spondaDestra and "Barca" in spondaDestra:
        return True
    return False

def visualizzaStato(spondaSinistra, spondaDestra):
    print("SPONDA SINISTRA: " + str(spondaSinistra))
    print("SPONDA DESTRA: " + str(spondaDestra))

'''
def game(stato_iniziale):
    spondaSinistra, spondaDestra = stato_iniziale
    print("Scegli un'azione: ")
    print("0. Sposta solo barca")
    print("1. Sposta lupo con barca")
    print("2. Sposta capra con barca")
    print("3. Sposta cavolo con barca")
    gameOver=False
    while not obiettivoRaggiunto(spondaDestra):
      if(applicaRegoleAlloStato(spondaSinistra, spondaDestra)):
        gameOver=True
        break
      visualizzaStato(spondaSinistra, spondaDestra)
      scelta = input()
      compiAzione(scelta, spondaSinistra, spondaDestra)
    if(gameOver):
      print("GAME OVER: ")
      visualizzaStato(spondaSinistra, spondaDestra)
    else:
      print("OBIETTIVO RAGGIUNTO: ")
      visualizzaStato(spondaSinistra, spondaDestra)

spondaSx = ["Lupo", "Capra", "Cavolo", "Barca"]
spondaDx = ["", "", "", ""]
stato_iniziale = (spondaSx, spondaDx)
game(stato_iniziale)
'''

def ricercaInProfondita(stato_corrente, stati_visitati, matrice, percorso_corrente):
    spondaSinistra, spondaDestra = stato_corrente

    # Aggiungi lo stato corrente al percorso attuale
    percorso_corrente.append(stato_corrente)

    # Aggiungi il percorso alla matrice quando esplori un nuovo stato
    if percorso_corrente not in matrice:
        matrice.append(percorso_corrente[:])
    # Aggiungi lo stato corrente agli stati visitati
    stati_visitati.add(stato_corrente)

    # Controlla se l'obiettivo è stato raggiunto
    if obiettivoRaggiunto(spondaDestra):
        print("Obiettivo raggiunto")
        visualizzaStato(spondaSinistra, spondaDestra)
        return True

    # Esplora le mosse possibili
    for mossa in range(4):
        # Crea copie dello stato
        nuova_spondaSinistra = list(spondaSinistra)
        nuova_spondaDestra = list(spondaDestra)

        # Esegui la mossa sulla copia
        compiAzione(str(mossa), nuova_spondaSinistra, nuova_spondaDestra)

        # Verifica se lo stato aggiornato è valido
        if not applicaRegoleAlloStato(nuova_spondaSinistra, nuova_spondaDestra):
            # Crea un nuovo stato come tupla di tuple
            nuovo_stato = (tuple(nuova_spondaSinistra), tuple(nuova_spondaDestra))

            # Evita stati già visitati
            if nuovo_stato in stati_visitati:
                continue

            # Prova a esplorare il nuovo stato
            if ricercaInProfondita(nuovo_stato, stati_visitati, matrice, percorso_corrente):
                return True

    # Rimuovi lo stato corrente dagli stati visitati e dal percorso corrente (backtracking)
    stati_visitati.remove(stato_corrente)
    percorso_corrente.pop()
    print("Fallimento!")
    return False


stati_visitati=set()
matrice_stati=[] # Ogni riga rappresenta un percorso
spondaSx = ["Lupo", "Capra", "Cavolo", "Barca"]
spondaDx = ["", "", "", ""]
stato_iniziale = (tuple(spondaSx), tuple(spondaDx))
ricercaInProfondita(stato_iniziale, stati_visitati, matrice_stati, [])


# Stampa la matrice degli stati attraversati per la soluzione
i=0
for riga in matrice_stati:
    print(str(i)+") "+str(riga))
    i=i+1