from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager, Screen


Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '700')
Builder.load_file("Perceptron.kv")


class HurufBase:
    input = [-1 for i in range(63)]
    pola = [
        [-1, -1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1,
         -1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
         -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
         1, -1, -1, -1, -1, -1, 1, 1, -1, -1, -1, -1, -1, 1, -1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
         -1, 1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, -1, 1, -1, -1,
         1, -1, -1, -1, -1, -1, 1, 1, -1, -1, -1, -1, -1, 1, -1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
         -1, -1, -1, -1, -1],
        [-1, -1, 1, 1, -1, -1, -1, -1, -1, 1, 1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1,
         -1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
         -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
         1, -1, -1, -1, -1, -1, 1, 1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
         -1, 1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, -1, 1, -1, -1,
         1, -1, -1, -1, -1, -1, 1, 1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
         -1, -1, -1, -1, -1]]
    alpha = 0.5
    tetha = 1
    bias = [0,0,0]
    bobot = [[0 for i in range(63)],
             [0 for i in range(63)],
             [0 for i in range(63)]]
    target = [[1, -1, -1, 1, -1, -1],
              [-1, 1, -1, -1, 1, -1],
              [-1, -1, 1, -1, -1, 1]]
    huruf = ['Alif', 'Ba', 'Ta']


db = HurufBase()


# Learning
def f(net):
    if net > db.tetha:
        return 1
    elif net < -db.tetha:
        return -1
    else:
        return 0


def learning(index):
    epoch = 0
    is_stop = False
    temp = [-1 for i in range(63)]
    while not is_stop:
        epoch += 1
        skip = 0
        hasil = []
        for x in range(len(db.pola)):
            for y in range(len(db.pola[x])):
                temp[y] = db.pola[x][y] * db.bobot[index][y]
            net = sum(temp) + db.bias[index]
            hasil.append(f(net))
            if hasil[x] != db.target[index][x]:
                for i in range(len(db.bobot[index])):
                    db.bobot[index][i] = db.bobot[index][i] + db.alpha * db.pola[x][i] * db.target[index][x]
                db.bias[index] = db.bias[index] + db.alpha * db.target[index][x]
            else:
                skip += 1
        if skip == 6:
            is_stop = True
    print("Epoch : ", epoch)
    print("Hasil : ", hasil)
    print("Bobot : ", db.bobot[index])


class Main(ScreenManager):
    pass


class Blank(Screen):
    pass


class Pola(Screen):
    temp = [-1 for i in range(63)]
    output = StringProperty(' ')
    fnet = [0, 0, 0]

    def ubah_input(self, a):
        if db.input[a] == -1:
            db.input[a] = 1
        else:
            db.input[a] = -1

    def cetak(self):
        print('temp = ', self.temp)
        print("target = ", self.fnet)
        if self.fnet == db.target[2][0:3]:
            self.output = str(db.huruf[2])
        elif self.fnet == db.target[1][0:3]:
            self.output = str(db.huruf[1])
        elif self.fnet == db.target[0][0:3]:
            self.output = str(db.huruf[0])

    def cek(self):
        for i in range(len(db.huruf)):
            for j in range(len(db.input)):
                self.temp[j] = db.input[j] * db.bobot[i][j]
            self.fnet[i] = f(db.bias[i] + sum(self.temp))
        self.cetak()

    def cek_pola(self, n):
        for i in range(len(db.huruf)):
            for j in range(len(db.pola[n-1])):
                self.temp[j] = db.pola[n-1][j] * db.bobot[i][j]
            self.fnet[i] = f(db.bias[i] + sum(self.temp))
        self.cetak()

    def clear(self):
        db.input = [-1 for i in range(63)]
        self.manager.current = "reset"
        self.manager.current = "main"


# Run Learning
for x in range(3):
    print("Target : ", db.huruf[x])
    learning(x)

tugas = Main()
screens = [Pola(name="main"), Blank(name="reset")]
for screen in screens:
    tugas.add_widget(screen)


class Perceptron(App):
    def build(self):
        return tugas

    # Run the App


if __name__ == '__main__':
    Perceptron().run()
