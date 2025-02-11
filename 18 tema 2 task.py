def prideti_zenkliuka(tekstas):
    return tekstas + "*"

def apversti_teksta(tekstas):
    return tekstas[::-1]

def apdoroti_teksta(tekstas, funkcija=None):
    if funkcija:
        return funkcija(tekstas)
    return tekstas.lower()

def keli_apdorojimai(tekstas, *funkcijos):
    for funkcija in funkcijos:
        tekstas = funkcija(tekstas)
    return tekstas

print(prideti_zenkliuka("Labas"))
print(apversti_teksta("Labas"))
print(apdoroti_teksta("LABAS", prideti_zenkliuka))
print(apdoroti_teksta("LABAS"))
print(keli_apdorojimai("LABAS", str.lower, prideti_zenkliuka, apversti_teksta))