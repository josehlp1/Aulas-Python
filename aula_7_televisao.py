class televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 2

    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_canal(self):
        if(self.ligada):
            self.canal +=1

    def diiminui_canal(self):
        if (self.ligada):
            self.canal -= 1

if __name__ == 'main':
    televisao = televisao();
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)
    print(televisao.canal)
    print(televisao.aumenta_canal())
    print(televisao.canal)
