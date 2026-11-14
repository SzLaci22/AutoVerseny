
class AutoSzL:

    def __init__(self, vaszon):
        self.vaszon = vaszon
        self.sebesseg = 10
        self.kezdetiX = 170
        self.kezdetiY = 325
        self.szinLista = ["red", "blue", "orange", "purple"]
        self.szinIndex = 0

    def mozgatSzL(self, irany):
        if irany == "bal":
            self.vaszon.move("auto", -self.sebesseg, 0)
        elif irany == "jobb":
            self.vaszon.move("auto", self.sebesseg, 0)
        elif irany == "fel":
            self.vaszon.move("auto", 0, -self.sebesseg)
        elif irany == "le":
            self.vaszon.move("auto", 0, self.sebesseg)

    def alaphelyzetSzL(self):
        auto = self.vaszon.bbox("auto")

        if auto is not None:
            kozepX = (auto[0] + auto[2]) / 2
            kozepY = (auto[1] + auto[3]) / 2

            self.vaszon.move(
                "auto",
                self.kezdetiX - kozepX,
                self.kezdetiY - kozepY
            )

    def autoPozicioSzL(self):
        return self.vaszon.bbox("auto")

    def autoSzinValtasSzL(self):
        self.szinIndex = (self.szinIndex + 1) % len(self.szinLista)
        ujSzin = self.szinLista[self.szinIndex]
        self.vaszon.itemconfig("autoTest", fill=ujSzin)
