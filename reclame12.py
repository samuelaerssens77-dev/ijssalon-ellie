from algemene_functies import mijn_functie_2

def combinatie(invoer_lijst_2):

    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0],korte_lijst[1])
    return uitvoer

def laag_en_hoog(invoer_lijst_2):
        
        laagste = min(invoer_lijst_2)
        hoogste = max(invoer_lijst_2)
        return [laagste, hoogste]
lijst=[15,9,36,4]
print(laag_en_hoog(lijst))
lijst=[14,10,24,6]
print(laag_en_hoog(lijst))
lijst=[15,5,50,2]
print(laag_en_hoog(lijst))
lijst=[120,90,2000,5]
print(laag_en_hoog(lijst))