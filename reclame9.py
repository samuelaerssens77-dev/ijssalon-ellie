def gemiddelde(mijn_lijst):
    totaal = sum(mijn_lijst)
    aantal = len(mijn_lijst)
    gemiddelde = totaal / aantal
    return gemiddelde
inkomsten_lijst = [220, 430, 125, 160, 205, 90, 345]
print(gemiddelde(inkomsten_lijst))