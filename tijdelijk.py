prijzen = ("mijn_dictionary")
mijn_dictionary = {
    "aardbei" : "3",
    "vanille" : "4",
    "chocolade" : "5",
}
a = 3 * 0.8
mijn_dictionary ["aanbieding"] = a
mijn_dictionary ["reclame_tekst"] = f"Vandaag in de aanbieding: vanille-ijs, 1 liter - slechts € {a}"
print()
for k, v in mijn_dictionary.items():
    print(k, v)


   
  
   
