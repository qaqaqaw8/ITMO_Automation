class Soda:
    def __init__(self, sirop=None):
        self.sirop = sirop

    def show_my_drink(self):
        if self.sirop == None:
            print("Обычная газировка")
        else:
            print("Газировка и " + self.sirop)
drink1 = Soda('cola')
drink2 = Soda()
drink1.show_my_drink()
drink2.show_my_drink()




