class Input:
    def __init__(self, loc, text):
        self.loc = loc
        self.text = text

search = Input("Место")
print(search.loc)

class Button:
    def __init__(self, loc, text):
        self.loc = loc
        self.text = text

a = Button('a1','a')
print(a.loc,a.text)

class Title:
    def __init__(self, loc, text):
        self.loc = loc
        self.text = text

b = Title('b1','b')
print(b.loc,b.text)

class Link:
    def __init__(self, loc, text):
        self.loc = loc
        self.text = text

c = Title('c1','c')
print(c.loc,c.text)






