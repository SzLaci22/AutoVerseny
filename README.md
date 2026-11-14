# Autóverseny-szimulátor

## Hallgatói adatok

- Név: Szántó László
- Neptun-kód: K35Y2Q

## A feladat leírása

A program egy egyszerű, 2D-s autóverseny-szimulátor. A játékos egy autót irányít egy felülnézetes versenypályán.

A cél egy teljes kör megtétele úgy, hogy az autó ne ütközzön a pálya szélével vagy a belső területtel.

A program funkciói:

- Autó irányítása a nyílbillentyűkkel.
- Ütközések ellenőrzése.
- Egy teljes kör megtételének ellenőrzése.
- A versenyidő mérése.
- Sikeres kör vagy sikertelen verseny jelzése.
- Autó színének megváltoztatása.
- Új verseny indítása.

## Használati útmutató

**Szükséges programok:**
- Python 3.
- Tkinter grafikai modul.

**A program indítása:**

A `main.py` fájl futtatásával indul a program.

**Irányítás:**

| Billentyű | Funkció |
|---|---|
| Fel nyíl | Mozgás felfelé |
| Le nyíl | Mozgás lefelé |
| Bal nyíl | Mozgás balra |
| Jobb nyíl | Mozgás jobbra |
| C | Autó színének megváltoztatása |

Az „Új verseny” gombbal újra lehet kezdeni a játékot.

## A program felépítése

A projekt három fájlból áll:

- `main.py` – A főprogram, a grafikus felület, az eseménykezelés, az időmérés és a verseny logikája.
- `sajatmodul_SzL.py` – Saját modul, amely az autó osztályát és annak metódusait tartalmazza.
- `README.md` – A projekt dokumentációja.

### Saját osztály

**AutoSzL**

Az autó tulajdonságait és műveleteit tartalmazó saját osztály.

Metódusai:

- `mozgatSzL()` – Az autó mozgatása.
- `alaphelyzetSzL()` – Az autó visszaállítása a rajthoz.
- `autoPozicioSzL()` – Az autó aktuális pozíciójának lekérdezése.
- `autoSzinValtasSzL()` – Az autó színének megváltoztatása.

### A main.py fontosabb függvényei

- `autoMozgatasaSzL()` – Az autó mozgatásának és az ütközés ellenőrzésének kezelése.
- `billentyuKezelesSzL()` – A billentyűzet eseményeinek kezelése.
- `ujrainditasSzL()` – A verseny újraindítása.
- `korEllenorzesSzL()` – A teljes kör megtételének ellenőrzése.
- `utkozesEllenorzesSzL()` – Az ütközések ellenőrzése.
- `idoMeresSzL()` – A versenyidő mérése.

### Felhasznált modul

- `tkinter` – Grafikus felület és eseménykezelés.
- `time` – Időmérés.

## Program indítása

A program a `main.py` fájl futtatásával indítható.