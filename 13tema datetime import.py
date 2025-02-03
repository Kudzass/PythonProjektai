import datetime

print(type(datetime))  # <class 'module'>

# kreipiamės į funkcionalumą aprašytą datetime faile
# todėl kode 2 kartus kartojam datetime
# antrasis datetime yra kreipimasis į klasę
# .today() metodas sukuria šio laiko momento datos-laiko objektą
# rezultatas yra datetime.datetime objektas
dt_res = datetime.datetime.today()
print(dt_res)  # 2024-10-10 10:33:24.596796
print(type(dt_res))  # <class 'datetime.datetime'>

res_year = dt_res.year
print(res_year)  # 2024
print(type(res_year))  # <class 'int'>

print(dt_res.month)
print(dt_res.day)
print(dt_res.hour)
print(dt_res.minute)
print(dt_res.second)
print(dt_res.microsecond)