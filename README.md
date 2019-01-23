# Avto-moto-sport-dirke

Analizirala bom dirke iz različnih tekmovalnih razredov avto-moto športa s strani:
[Motor Sport Magazine](https://www.motorsportmagazine.com/database/races).

Za vsako dirko bom zajela:
* ime dirke
* kraj dirke (država)
* čas dirke (datum)
* kateri tekmovalni razred je tekmoval na tej dirki
* zmagovalca dirke

Delovne hipoteze:
* V kateri državi je potekalo največ dirk določenih tekmovalnih razredov?
* Priljubljenost dirk v posameznih letih.
* Kdateri so najuspešnejši dirkači?
* Ali je kakšna povezava med zmagovalci in dirkališči (so nekateri dirkači res bolj uspešni na določenih stezah)?

V mapi 'avto-moto dirke' so shranje vse spletne strani, iz katerih sem črpala podatke. Shranjna pa je tudi csv datoteka, ki vsebuje podatke iz vseh shranjenih strani. V mapi 'avto_moto dirke obdelani podatki' so dodane še csv datoteke z obdelanimi podatki, potrebni za analizo.

Ker je ta csv datoteka zelo velika, sem jo razdelila na več delov zaradi lepšiga prikaza. Zato so v mapi 'avto-moto dirke csvji' shranjeni vsi csvji, ki sem jih naredila (ta velik in trije manjši, razdeljeni po straneh od 0 do 100, od 100 do 200 in od 200 do 258).

Dodana je tudi skripta zajem_podatkov.py, kjer so vse funkcije, s katerimi sem si pomagala pri zajemu podatkov in oblikovanju csvjev.