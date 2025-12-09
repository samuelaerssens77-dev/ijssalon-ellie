prijzen = {
    "aardbei" : 3,  # prijs van aardbei-ijs is €3
    "vanille" : 4,  # prijs van vanille-ijs is €4
    "chocolade" : 5  # prijs van chocolade-ijs is €5
}
aanbieding = prijzen ["aardbei"] * 0.8  # 3 * 0.8 = €2.40
reclame_tekst = f"Vandaag in de aanbieding: vanille-ijs, 1 liter - slechts € {aanbieding}"
for k, v in prijzen.items():
    print(k, v)
print(reclame_tekst)
    



   
  
   
