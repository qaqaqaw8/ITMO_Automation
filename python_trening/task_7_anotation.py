def indent(s: str, width: int) -> str:
    return ' '*(max(0, width -len(s))) + s
print(indent('123', 123))

def func3(s: str="") ->int:
    return len(s)
print(func3())

def func4(a: list, b: list) ->int:
    return max(len(a), len(b))
print(func4([1, 2, 3, 4], [1, 2]))

def func5(a, b):
    a.append(b)
    return a
print(func5([1,'H',3,4], "F"))

def func6(a):
    b=0
    for elem in a:
        b=b+elem
    return b
print(func6([1,2,3,4]))