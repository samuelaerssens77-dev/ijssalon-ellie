prijzen = {
    "aardbei" : 3,  # prijs van aardbei-ijs is €3
    "vanille" : 4,  # prijs van vanille-ijs is €4
    "chocolade" : 5  # prijs van chocolade-ijs is €5
}
aanbieding = prijzen ["aardbei"] * 0.8  # 3 * 0.8 = €2.40
reclame_tekst = f"Vandaag in de aanbieding: vanille-ijs, 1 liter - slechts € {aanbieding}"
reclame_tekst2 = reclame_tekst[:63]
reclame_tekst3 = reclame_tekst2.upper()
reclame_tekst4 = reclame_tekst3.split()
for k, v in prijzen.items():
    print(k, v)
print(reclame_tekst4)
for l in reclame_tekst4:
    print(l.lower())



    



   
  
   
