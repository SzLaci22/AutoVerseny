import tkinter as tk
import time
from sajatmodul_SzL import AutoSzL

ablak = tk.Tk()
ablak.title("Autóverseny - SzL")
ablak.geometry("900x650")
ablak.resizable(False, False)

vaszon = tk.Canvas(
    ablak,
    width=900,
    height=650,
    bg="green"
)

vaszon.pack()

vaszon.create_rectangle(
    100, 80, 800, 570,
    fill="gray",
    outline="white",
    width=4
)

vaszon.create_rectangle(
    250, 200, 650, 450,
    fill="green",
    outline="white",
    width=4
)

vaszon.create_line(
    100, 325, 250, 325,
    fill="white",
    width=4,
    dash=(10, 5)
)

vaszon.create_line(
    100, 325, 250, 325,
    fill="white",
    width=4,
    dash=(10, 5)
)

vaszon.create_line(
    450, 80, 450, 200,
    fill="white",
    width=3,
    dash=(10, 5)
)

vaszon.create_line(
    800, 325, 650, 325,
    fill="white",
    width=3,
    dash=(10, 5)
)

vaszon.create_line(
    450, 570, 450, 450,
    fill="white",
    width=3,
    dash=(10, 5)
)

vaszon.create_text(
    450, 325,
    text="VERSENYPÁLYA",
    fill="white",
    font=("Arial", 20, "bold")
)

vaszon.create_rectangle(
    145, 310, 195, 340,
    fill="red",
    outline="black",
    width=2,
    tags="auto autoTest"
)

vaszon.create_rectangle(
    155, 315, 185, 335,
    fill="black",
    outline="black",
    tags="auto"
)

autoObjektum = AutoSzL(vaszon)

def autoMozgatasaSzL(irany):
    global versenyVege

    if versenyVege:
        return

    autoObjektum.mozgatSzL(irany)

    if utkozesEllenorzesSzL():
        versenyVege = True
        vaszon.create_text(
            450, 150,
            text="VERSENY VÉGE!",
            fill="red",
            font=("Arial", 28, "bold"),
            tags="eredmeny"
        )
    else:
        korEllenorzesSzL()


def billentyuKezelesSzL(esemeny):
    if esemeny.keysym == "Left":
        autoMozgatasaSzL("bal")
    elif esemeny.keysym == "Right":
        autoMozgatasaSzL("jobb")
    elif esemeny.keysym == "Up":
        autoMozgatasaSzL("fel")
    elif esemeny.keysym == "Down":
        autoMozgatasaSzL("le")
    elif esemeny.keysym.lower() == "c":
        autoObjektum.autoSzinValtasSzL()

def ujrainditasSzL():
    global versenyVege
    global korSzakaszSzL
    global indulasiIdo

    versenyVege = False
    korSzakaszSzL = 0
    indulasiIdo = time.time()

    autoObjektum.alaphelyzetSzL()

    vaszon.delete("eredmeny")

    vaszon.itemconfig(
        idoFelirat,
        text="Idő: 0.0 mp"
    )

    idoMeresSzL()

ablak.bind("<KeyPress>", billentyuKezelesSzL)


versenyVege = False
korSzakaszSzL = 0

indulasiIdo = None
idoFelirat = vaszon.create_text(
    450, 40,
    text="Idő: 0.0 mp",
    fill="white",
    font=("Arial", 18, "bold")
)

def korEllenorzesSzL():
    global korSzakaszSzL
    global versenyVege

    auto = autoObjektum.autoPozicioSzL()

    if auto is None:
        return

    x1, y1, x2, y2 = auto

    kozepX = (x1 + x2) / 2
    kozepY = (y1 + y2) / 2

    if korSzakaszSzL == 0:
        if 400 < kozepX < 500 and 80 < kozepY < 200:
            korSzakaszSzL = 1

    elif korSzakaszSzL == 1:
        if 650 < kozepX < 800 and 275 < kozepY < 375:
            korSzakaszSzL = 2

    elif korSzakaszSzL == 2:
        if 400 < kozepX < 500 and 450 < kozepY < 570:
            korSzakaszSzL = 3

    elif korSzakaszSzL == 3:
        if 100 < kozepX < 250 and 275 < kozepY < 375:
            versenyVege = True

            elteltIdo = time.time() - indulasiIdo

            vaszon.create_text(
                450, 150,
                text=f"SIKERES KÖR! Idő: {elteltIdo:.1f} mp",
                fill="yellow",
                font=("Arial", 22, "bold"),
                tags = "eredmeny"
            )

def utkozesEllenorzesSzL():
    auto = autoObjektum.autoPozicioSzL()

    if auto is None:
        return False

    x1, y1, x2, y2 = auto

    if x1 < 100 or y1 < 80 or x2 > 800 or y2 > 570:
        return True

    if x2 > 250 and x1 < 650 and y2 > 200 and y1 < 450:
        return True

    return False

def idoMeresSzL():
    global indulasiIdo

    if indulasiIdo is None:
        indulasiIdo = time.time()

    if not versenyVege:
        elteltIdo = time.time() - indulasiIdo

        vaszon.itemconfig(
            idoFelirat,
            text=f"Idő: {elteltIdo:.1f} mp"
        )

        ablak.after(100, idoMeresSzL)

idoMeresSzL()

ujrainditasGomb = tk.Button(
    ablak,
    text="Új verseny",
    command=ujrainditasSzL
)

vaszon.create_window(
    790, 40,
    window=ujrainditasGomb
)
ablak.mainloop()