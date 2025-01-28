print('----------5 UŽDUOTIS: Loginiai jungikliai funkcijose---------------')

def skaiciuoti_sumos_tipa(x, y, tik_teigiama=False):
    suma = x + y
    return suma if not tik_teigiama or suma > 0 else 0

rezultatas1 = skaiciuoti_sumos_tipa(5, -10)
rezultatas2 = skaiciuoti_sumos_tipa(5, -10, tik_teigiama=True)
print("Suma be apribojimų:", rezultatas1)
print("Suma su tik teigiamais skaičiais:", rezultatas2)

print('-----------6 UŽDUOTIS: DOCstringai funkcijose-----------------------')

def apskaiciuok_vidurki(skaiciai: list[float]) -> float:
       return sum(skaiciai) / len(skaiciai) if skaiciai else 0.0


def prideti_zodi(tekstas: str, zodis: str) -> str:
       return f"{tekstas} {zodis}"
