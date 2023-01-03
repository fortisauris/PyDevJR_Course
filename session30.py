'''
SESSION30 - FASTAPI zaklady:

MONOLITICKY KOD - Obrovsky kus kodu, mala zmena, velky problem

MICROSERVIS - mensi kratsi kod, ktory komunikuje s dalsimi programami pomocou API.

API - Aplikacny programovy interfejs pomocou ktoreho komunikuju programy navzajom


používajú json. ktorý má podobnú štruktúru ako python dict()

FastApi - Stojí na dvoch hlavných súčastiach Pydantic, Starlette

Výhody FastAPI = rýchlosť developovania a servovania API, podpora Async

# VIRTUALIZÁCIA

= VM(virtuálny počítač) rozdelíme počítač na menšie počítače
= Kontajnerizácia rozdelíme počítač na viacero malých kontajnerov kde bežia programy komunikujúce
medzi sebou pomocou API.
= Cluster - spojíme veľa malých počítačov do jedného veľkého pomocou KUBERNETES. Tento im rozdeľuje
úlohy a dozerá na nich.


pokračujeme FA01 kde si predstavujeme základné HTTP metódy GET, POST, PUT, DELETE a PATCH.

Riešime zachytávanie chýb a zatiaľ databázu máme iba v zozname.

pokračujeme FA02 kde si urobíme API, ktorá číta z inej API ceny BITCONU a na požiadanie nám ich
servíruje :)

'''