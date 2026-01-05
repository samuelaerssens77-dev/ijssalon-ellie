from algemene_functies import mijn_functie_2

def combinatie(invoer_lijst_2):
    def laag_en_hoog(invoer_lijst_2):
        if not invoer_lijst_2:
            return []
        laagste = min(invoer_lijst_2)
        hoogste = max(invoer_lijst_2)
        return [laagste, hoogste]
    
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    resultaat = mijn_functie_2(korte_lijst)
    return resultaat

print(combinatie(ik_kom_er_niet_uit))
