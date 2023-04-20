# AUFGABE  3

class stadt:
    def __init__ (self, name, land, kontinent, einwohner, koordinate):
        self.name = str(name)
        self.land = str(land)
        self.kontinent = str(kontinent)
        self.einwohner = int(einwohner)
        self.koordinate = tuple(koordinate)


# AUFGABE 4

from PyQt5.QtWidgets import *

class fenster(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Fenster")

        self.widget=QWidget()
        layouth=QHBoxLayout(self.widget)
        
        self.Frage=QLabel("Ist dieses Datum in Ordnung")
        self.kalender=QCalendarWidget()
        self.Ja=QPushButton("Ja")
        self.Nein=QPushButton("Neiin")
        self.Abbrechen=QPushButton("Abbrechen")
        layouth.addWidget(self.Ja)
        layouth.addWidget(self.Nein)
        layouth.addWidget(self.Abbrechen)
        layout=QFormLayout()
        self.setLayout(layout)

        layout.addRow(self.kalender)
        layout.addRow(self.Frage)
        layout.addRow(self.widget) 

        center= QWidget()
        center.setLayout(layout)

        self.setCentralWidget(center)

        self.show()

app= QApplication([])
win= fenster()



# AUFGABE 5

class Dachform:
    def __init__(self, Sattel, schraeg, flach):
        self.sattel = bool(Sattel)
        self.schraeg = bool(schraeg)
        self.flach = bool(flach)

class Flach(Dachform):
    def __init__(self, flach):
        super().__init__(flach)

        
class schraeg(Dachform):
    def __init__(self, schraeg):
        super().__init__(schraeg)

class Sattel(Dachform):
    def __init__(self, Sattel):
        super().__init__(Sattel)

if Flach == "True":
    print("dies ist ein Flachdach")
if Sattel =="True":
    print("dies ist ein Satteldach")
if schraeg == "True":
    print("dies ist ein Schraegdach")


# AUFGABE 6

from PyQt5.QtWidgets import *

class fenster(QMainWindow):
    def __init__(self):
        super().__init__()

        self.createLayout()
        self.createConnects()

    def createLayout(self):
        self.setWindowTitle("Währungsumrechner")

        layout=QFormLayout()
        self.umrechnen=QPushButton("Umrechnen")
        self.CHF=QLineEdit()
        self.EUR=QLabel()

        layout.addRow("Schweizer Franken",self.CHF)
        layout.addRow("Euro:",self.EUR)
        layout.addRow(self.umrechnen)

        center= QWidget()
        center.setLayout(layout)

        self.setCentralWidget(center)

        self.show()
    def createConnects(self):
        self.umrechnen.clicked.connect(self.rechner)

    def rechner (self):
        self.EUR.setText(str((int((self.CHF.text()))/100)*87.60))

app= QApplication([])
win= fenster()
app.exec()