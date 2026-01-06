def inkomsten_totaal(inkomsten, btw):
    totaal = sum(inkomsten)
    btw = totaal * btw
    return totaal
dagelijke_inkomsten = [220, 430, 125, 160, 205, 90, 345]
totale_opbrengst = inkomsten_totaal(dagelijke_inkomsten, 0.09)
btw = totale_opbrengst * 0.09
print(f"Het totaal van alle inkomsten van deze week is {totale_opbrengst} euro, waarover {btw} euro btw moet betaald dient te worden")