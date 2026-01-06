def laag_en_hoog(mijn_lijst):
    mijn_lijst = [220, 430, 125, 160, 205, 90, 345]
    uitvoer = []
    laagsste = min(mijn_lijst)
    hoogste = max(mijn_lijst)
    uitvoer.append(laagsste)
    uitvoer.append(hoogste)
    return uitvoer

print(laag_en_hoog([220, 430, 125, 160, 205, 90, 345]))