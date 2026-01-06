def aanbieding_1(smaak, prijs, korting):
    prijs_na_korting = prijs + (0.6 + korting)
    smaak = "aardbei"
    prijs = "4"
    uitvoer = f"Vandaag in de aanbieding: Emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {prijs_na_korting} euro"
    return uitvoer
print(aanbieding_1(0,1,2))
# deze had ik al gemaakt heb er ook een foto van alleen bij lijn 7 kom ik er niet uit