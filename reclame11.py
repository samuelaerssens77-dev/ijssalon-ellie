def meervoudig(invoer_lijst):
    hoogste_waarde, laagste_waarde = hoog_en_laag(invoer_lijst)
    uitvoer = hoogste_waarde, laagste_waarde
    return uitvoer
def hoog_en_laag(lijst):
    hoogste = max(lijst)
    laagste = min(lijst)
    return hoogste, laagste
print(meervoudig([10, 5, 3, 2, 1, 9]))